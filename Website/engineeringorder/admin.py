from django.contrib import admin
import engineeringorder

# Register your models here.
from engineeringorder.models import *

admin.site.register(EngineeringOrder);
admin.site.register(MaterialEO);