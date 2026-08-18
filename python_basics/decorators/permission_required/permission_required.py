from functools import wraps


def require_role(*required_roles):
    if not required_roles:
        raise ValueError("At least one required role must be provided")

    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if not isinstance(user, dict):
                raise PermissionError("User data is required")

            user_role = user.get("role")

            if user_role not in required_roles:
                allowed_roles = ", ".join(required_roles)
                raise PermissionError(f"Required role: {allowed_roles}")

            return func(user, *args, **kwargs)

        return wrapper

    return decorator


@require_role("admin")
def delete_user(user, target_username):
    return f"{target_username} deleted by {user['username']}"


@require_role("admin", "manager")
def update_user_status(user, target_username, status):
    return f"{target_username} status changed to {status} by {user['username']}"
