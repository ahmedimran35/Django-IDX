from django.contrib import admin
from .models import Chaivarity

# Register your models here.
@admin.register(Chaivarity)
class ChaivarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'cha_type')
# admin.site.register(Chaivarity)