import unittest

from timeout_loader import (
    load_multiple_services,
    load_service_data,
    load_service_data_with_timeout,
)


class TimeoutLoaderTests(unittest.IsolatedAsyncioTestCase):
    async def test_load_service_data_returns_loaded_status(self):
        result = await load_service_data("users")

        self.assertEqual(
            result,
            {
                "service": "users",
                "status": "loaded",
            },
        )

    async def test_load_service_data_with_timeout_returns_data_if_fast_enough(self):
        result = await load_service_data_with_timeout(
            "users",
            delay=0.01,
            timeout=0.1,
        )

        self.assertEqual(
            result,
            {
                "service": "users",
                "status": "loaded",
            },
        )

    async def test_load_service_data_with_timeout_returns_timeout_if_too_slow(self):
        result = await load_service_data_with_timeout(
            "payments",
            delay=0.1,
            timeout=0.01,
        )

        self.assertEqual(
            result,
            {
                "service": "payments",
                "status": "timeout",
            },
        )

    async def test_load_multiple_services_returns_loaded_and_timeout_statuses(self):
        services = [
            {"name": "users", "delay": 0.01},
            {"name": "payments", "delay": 0.1},
            {"name": "notifications", "delay": 0.01},
        ]

        result = await load_multiple_services(services, timeout=0.05)

        self.assertEqual(
            result,
            [
                {"service": "users", "status": "loaded"},
                {"service": "payments", "status": "timeout"},
                {"service": "notifications", "status": "loaded"},
            ],
        )

    async def test_load_multiple_services_returns_empty_list(self):
        result = await load_multiple_services([])

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
