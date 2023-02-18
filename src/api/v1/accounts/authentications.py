from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .models import CustomUser


UserModel = get_user_model()


class EmailPhoneAuthBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(CustomUser.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            username = username
            user = CustomUser.objects.get(Q(email=username) | Q(phone=username))
        except CustomUser.DoesNotExist:
            CustomUser().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user