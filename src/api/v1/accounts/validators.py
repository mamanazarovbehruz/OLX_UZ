from django.core.validators import RegexValidator

def default_user_authentication_rule(user):
    return user is not None and user.is_active and not user.is_deleted



validate_phone = RegexValidator(
    regex=r'^\+?998?\d{9}$',
    message='Raqam 13 ta belgidan iborat bolishi kerak. P.s: +998912345678'
)
