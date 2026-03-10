from functools import wraps
from flask import abort
from flask_login import current_user

def rol_requerido(*roles):
    """
    Uso:
        @login_required
        @rol_requerido('admin')
        def mi_vista(): ...

        @login_required
        @rol_requerido('admin', 'operario')
        def otra_vista(): ...
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.rol not in roles:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator