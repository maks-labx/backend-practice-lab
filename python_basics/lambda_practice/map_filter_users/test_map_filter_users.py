import unittest

from map_filter_users import get_active_users, get_uppercase_names


class MapFilterUsersTests(unittest.TestCase):
    def test_get_uppercase_names_returns_names_in_uppercase(self):
        users = [
            {"name": "max", "age": 31, "is_active": True},
            {"name": "anna", "age": 24, "is_active": False},
            {"name": "john", "age": 18, "is_active": True},
        ]

        result = get_uppercase_names(users)

        self.assertEqual(result, ["MAX", "ANNA", "JOHN"])

    def test_get_active_users_returns_only_active_users(self):
        users = [
            {"name": "max", "age": 31, "is_active": True},
            {"name": "anna", "age": 24, "is_active": False},
            {"name": "john", "age": 18, "is_active": True},
        ]

        result = get_active_users(users)

        self.assertEqual(
            result,
            [
                {"name": "max", "age": 31, "is_active": True},
                {"name": "john", "age": 18, "is_active": True},
            ],
        )

    def test_empty_list_returns_empty_lists(self):
        self.assertEqual(get_uppercase_names([]), [])
        self.assertEqual(get_active_users([]), [])


if __name__ == "__main__":
    unittest.main()
