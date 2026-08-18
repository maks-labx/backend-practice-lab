import unittest

from permission_required import delete_user, require_role, update_user_status


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

    def test_manager_can_update_user_status(self):
        manager = {
            "username": "anna",
            "role": "manager",
        }

        result = update_user_status(manager, "john", "active")

        self.assertEqual(result, "john status changed to active by anna")

    def test_admin_can_update_user_status(self):
        admin = {
            "username": "max",
            "role": "admin",
        }

        result = update_user_status(admin, "john", "blocked")

        self.assertEqual(result, "john status changed to blocked by max")

    def test_user_cannot_update_user_status(self):
        user = {
            "username": "john",
            "role": "user",
        }

        with self.assertRaises(PermissionError):
            update_user_status(user, "anna", "blocked")

    def test_missing_role_raises_permission_error(self):
        user = {
            "username": "anna",
        }

        with self.assertRaises(PermissionError):
            delete_user(user, "john")

    def test_invalid_user_data_raises_permission_error(self):
        with self.assertRaises(PermissionError):
            delete_user(None, "john")

    def test_decorator_requires_at_least_one_role(self):
        with self.assertRaises(ValueError):
            require_role()

    def test_decorator_preserves_original_function_name(self):
        self.assertEqual(delete_user.__name__, "delete_user")
        self.assertEqual(update_user_status.__name__, "update_user_status")


if __name__ == "__main__":
    unittest.main()
