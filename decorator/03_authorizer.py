from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrappes(user_role):
        if user_role.lower() != "admin":
            print("Access Denied")
            return None
        else:
            return func(user_role)
    return wrappes

@require_admin
def access_ad(role):
    print("Access Granted To The Inventory")
access_ad("User")        
access_ad("ADmin")        