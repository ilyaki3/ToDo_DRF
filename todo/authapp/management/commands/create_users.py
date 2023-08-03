from django.core.management.base import BaseCommand

from authapp.models import User

class Command(BaseCommand):
    help = 'Creating superuser and some test users'

    def handle(self, *args, **options):
        User.objects.all().delete()
        User(email='alsac@acvd.com', username='Cdsvs', first_name='Esdvs', last_name='Vsdvsvv').save()
        User.objects.create_user(email='adsvssv@acvd.com', username='svdfvd', first_name='gfdfv', last_name='rtgb')
        User.objects.create_user(email='gbsdv@acvd.com', username='sdbfd', first_name='rgbd', last_name='sfvbg')
        User.objects.create_superuser(username='admin',
                                      password='admin')
