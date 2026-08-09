import unittest

from profile_loader import load_profile, load_profile_safe, load_profiles


class ProfileLoaderTests(unittest.IsolatedAsyncioTestCase):
    async def test_load_profile_returns_profile_data(self):
        result = await load_profile("max")

        self.assertEqual(
            result,
            {
                "username": "max",
                "status": "loaded",
            },
        )

    async def test_load_profile_raises_error_for_empty_username(self):
        with self.assertRaises(ValueError):
            await load_profile("")

    async def test_load_profile_safe_returns_error_status_for_empty_username(self):
        result = await load_profile_safe("")

        self.assertEqual(
            result,
            {
                "username": "",
                "status": "error",
                "error": "username is required",
            },
        )

    async def test_load_profiles_returns_multiple_profiles(self):
        result = await load_profiles(["max", "anna", "john"])

        self.assertEqual(
            result,
            [
                {"username": "max", "status": "loaded"},
                {"username": "anna", "status": "loaded"},
                {"username": "john", "status": "loaded"},
            ],
        )

    async def test_load_profiles_handles_invalid_usernames(self):
        result = await load_profiles(["max", "", "anna"])

        self.assertEqual(
            result,
            [
                {"username": "max", "status": "loaded"},
                {
                    "username": "",
                    "status": "error",
                    "error": "username is required",
                },
                {"username": "anna", "status": "loaded"},
            ],
        )

    async def test_load_profiles_returns_empty_list_for_empty_input(self):
        result = await load_profiles([])

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
