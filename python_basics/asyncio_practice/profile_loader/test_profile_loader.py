import unittest

from profile_loader import load_profile, load_profiles


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

    async def test_load_profiles_returns_empty_list_for_empty_input(self):
        result = await load_profiles([])

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
