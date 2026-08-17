from functools import wraps


def require_role(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if not isinstance(user, dict):
                raise PermissionError("User data is required")

            if user.get("role") != required_role:
                raise PermissionError(f"Required role: {required_role}")

            return func(user, *args, **kwargs)

        return wrapper

    return decorator


@require_role("admin")
def delete_user(user, target_username):
    return f"{target_username} deleted by {user['username']}"
