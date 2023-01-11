from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User=get_user_model()

class Command(BaseCommand):
    help='Creates a superuser'
    if not User.objects.filter(username='example2@gmail.com').exists():
        User.objects.create_superuser(
            username='example2@gmail.com',
            password='Soltn2@5102'
        )
    print('Superuser has been created.')