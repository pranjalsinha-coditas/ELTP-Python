def role_based_access_control(role_required):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                user_role = kwargs.get('role', 'none')
                assert role_required == 'any' or user_role == role_required
                return func(*args, **kwargs)
            except AssertionError:
                return f"Access Denied for role: {user_role}. Required role: {role_required}"
        return wrapper
    return decorator

user_db = []

@role_based_access_control(role_required='any')
def get_details(name, **kwargs):
    try:
        user = next(filter(lambda user: user['name'] == name, users_db))
        return user
    except StopIteration:
        return "User not found"

@role_based_access_control(role_required='any')
def post_details(details, **kwargs):
    user_db.append(details)
    return f"User {details['name']} added successfully"
    
@role_based_access_control(role_required='hr')
def deletion_details(name, **kwargs):
    try:
        global users_db
        count_before = len(list(filter(lambda user: user['name'] == name, users_db)))
        count_after = len(list(filter(lambda user: user['name'] == name, user_db)))

        while count_before != count_after:
            return f"User {name} deleted successfully"
        raise ValueError
    except ValueError:
        return f"Failed to delete {name} or user does not exist"
    