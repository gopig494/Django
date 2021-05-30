from django.contrib import admin
from modelapp.models import list

# Register your models here.
class abc(admin.ModelAdmin):
	list=['RollNo','StudentName']
admin.site.register(list,abc)
