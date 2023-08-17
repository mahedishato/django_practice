from django.contrib import admin
from demo.models import teaccher

# Register your models here.
class teaccherAdmin(admin.ModelAdmin):
    list_display= ('id', 't_id', 't_name', 't_email')
admin.site.register(teaccher, teaccherAdmin)