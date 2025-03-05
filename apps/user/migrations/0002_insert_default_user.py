# Django
from django.db import migrations



# Main Section
def forwards_insert_default_user(apps, schema_editor):
    from apps.user.serializers import AuthSignupSerializer
    user_data_list = [
        {
            "email" : "admin@google.com",
            "password" : "admin1234",
            "admin_code" : "abcd"
        },
        {
            "email": "user@google.com",
            "password": "user1234"
        }
    ]
    for user_data in user_data_list:

        serializer = AuthSignupSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


def reverse_insert_default_user(apps, schema_editor):
    User = apps.get_model('user', 'User')
    User.objects.filter(email__in=["admin@google.com", "user@google.com"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            code=forwards_insert_default_user,
            reverse_code=reverse_insert_default_user,
        ),
    ]
