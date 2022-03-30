from rest_framework import serializers
from .models import Employee, Task, Feedback, Meeting


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
            model = Employee

            fields = ('pk','name','employee_number' , 'city', 'state', 'email')

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
            model = Task
            fields = ('pk','employee', 'name', 'description', 'priority', 'deadline', 'created_date')


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
            model = Feedback
            fields = ('pk','employee', 'task', 'subject', 'comment', 'created_date', 'updated_date')


class MeetingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Meeting
    fields = ('pk', 'employee', 'subject', 'comment', 'requested_date', 'created_date')

