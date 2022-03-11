from django.core.management.base import BaseCommand

from authapp.models import ExamUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        i = 0
        while i <= 9:
            ExamUser.objects.create_user(f'user{i + 1}', f'user{i + 1}@gmail.com', password='password')
            i += 1
        ExamUser.objects.create_superuser('admin', 'admin@gmail.com', password='admin11')
        print('Пользователи и супер пользователь созданы')
