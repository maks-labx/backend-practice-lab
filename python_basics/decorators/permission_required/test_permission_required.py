import unittest

from permission_required import delete_user


class PermissionRequiredTests(unittest.TestCase):
    def test_admin_can_delete_user(self):
        admin = {
            "username": "max",
            "role": "admin",
        }

        result = delete_user(admin, "john")

        self.assertEqual(result, "john deleted by max")

    def test_non_admin_cannot_delete_user(self):
        user = {
            "username": "anna",
            "role": "user",
        }

        with self.assertRaises(PermissionError):
            delete_user(user, "john")

    def test_missing_role_raises_permission_error(self):
        user = {
            "username": "anna",
        }

        with self.assertRaises(PermissionError):
            delete_user(user, "john")

    def test_invalid_user_data_raises_permission_error(self):
        with self.assertRaises(PermissionError):
            delete_user(None, "john")

    def test_decorator_preserves_original_function_name(self):
        self.assertEqual(delete_user.__name__, "delete_user")


if __name__ == "__main__":
    unittest.main()
