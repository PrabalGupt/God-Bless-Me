from django.contrib import admin
from .models import TrainStatus, UserDetails
# Register your models here.
admin.site.register(TrainStatus)
admin.site.register(UserDetails)