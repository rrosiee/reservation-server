from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


# Main Section
class UserObjectManager(BaseUserManager):
    def signup_user(self, email, password, admin_code):
        is_admin = False
        if admin_code and admin_code == "abcd":  # TODO : admin_code는 임시값
            is_admin = True

        instance = self.model.objects.create(
            email=email, password=make_password(password), is_admin=is_admin
        )
        return instance
