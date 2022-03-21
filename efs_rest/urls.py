
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from portfolio import views

urlpatterns = [

  path('admin/', admin.site.urls),
  path('auth/', obtain_jwt_token),
  path('', views.employee_list),
  url(r'^api/employees/$', views.employee_list),
  url(r'^api/employees/(?P<pk>[0-9]+)$', views.getEmployee),
  path('tasks/', views.task_list),
  url(r'^api/tasks/$', views.task_list),
  url(r'^api/tasks/(?P<pk>[0-9]+)$', views.getTask),
  path('feedbacks/', views.feedback_list),
  url(r'^api/feedbacks/$', views.feedback_list),
  url(r'^api/feedbacks/(?P<pk>[0-9]+)$', views.getFeedback),
  path('meetings/', views.meeting_list),
  url(r'^api/meetings/$', views.meeting_list),
  url(r'^api/meetings/(?P<pk>[0-9]+)$', views.getMeeting),
  path('managers/', views.manager_list),
  url(r'^api/managers/$', views.manager_list),
  url(r'^api/managers/(?P<pk>[0-9]+)$', views.getManager)
]


