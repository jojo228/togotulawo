from django.contrib.auth.backends import ModelBackend, BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from account.models import User


UserModel = get_user_model()

class EmailBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        try:
            email = kwargs["email"]
        except KeyError:
            return None
        password = kwargs["password"]
        try:
            user = User.objects.get(email=email)
            if user.check_password(password) is True:
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, email):
        try:
            return User.objects.get(pk=email)
        except User.DoesNotExist:
            return None