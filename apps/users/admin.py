from django.contrib import admin
from apps.users.models import User
from apps.users.models import Worker
admin.site.register(User)
admin.site.register(Worker)