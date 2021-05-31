from django.contrib import admin

from IT_Team.models import empdetails

# Register your models here.

class details(admin.ModelAdmin):
	lisst=['EmployeeNo','EmployeeName','	EmployeeAddress']
	
admin.site.register(empdetails,details)
	
