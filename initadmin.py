#!/usr/bin/env python
import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parking.settings")
    import django
    django.setup()
    from authtools.models import User
    if User.objects.count() == 0:
        User.objects.create_superuser(email='admin@parking.com', password='admin990')
