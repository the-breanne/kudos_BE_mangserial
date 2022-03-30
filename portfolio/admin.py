from django.contrib import admin
from .models import Employee, Task, Feedback, Meeting, Manager

class EmployeeList(admin.ModelAdmin):
    list_display = ('employee_number', 'name', 'city', 'email')
    list_filter = ('employee_number', 'name', 'city')
    search_fields = ('employee_number', 'name')
    ordering = ['employee_number']


class TaskList(admin.ModelAdmin):
    list_display = ('name', 'description', 'priority', 'deadline')
    list_filter = ('name', 'priority', 'deadline')
    search_fields = ('name', 'priority')
    ordering = ['name']


class FeedbackList(admin.ModelAdmin):
    list_display = ('employee', 'task', 'subject', 'comment')
    list_filter = ('task','subject')
    search_fields = ('task','subject')
    ordering = ['task']


class MeetingList(admin.ModelAdmin):
  list_display = ('employee', 'subject', 'comment', 'requested_date', 'created_date')
  list_filter = ('subject', 'employee')
  search_fields = ('employee', 'subject')
  ordering = ['subject']

class ManagerList(admin.ModelAdmin):
  list_display = ('employee', 'name', 'manager_number', 'city', 'email')
  list_filter = ('employee', 'name', 'city')
  search_fields = ('employee', 'name')
  ordering = ['employee']


admin.site.register(Employee, EmployeeList)
admin.site.register(Task, TaskList)
admin.site.register(Feedback, FeedbackList)
admin.site.register(Meeting, MeetingList)
admin.site.register(Manager, ManagerList)
