def get_uppercase_names(users):
    return list(map(lambda user: user["name"].upper(), users))


def get_active_users(users):
    return list(filter(lambda user: user["is_active"], users))
