from functools import wraps

def require_ad(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role.lower() != "admin":
            print("Access Denied")
            return None
        else:
            return func(user_role)
    return wrapper

@require_ad
def admin(user):
    print("Access granted")
admin("admin")