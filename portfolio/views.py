from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


@csrf_exempt
@api_view(['GET', 'POST'])
def employee_list(request):
  permission_classes = (IsAuthenticatedOrReadOnly)
  if request.method == 'GET':
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, context={'request': request}, many=True)
    return Response({'data': serializer.data})

  elif request.method == 'POST':
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getEmployee(request, pk):
  """
  Retrieve, update or delete a employee instance.
  """
  try:
    employee = Employee.objects.get(pk=pk)
  except Employee.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = EmployeeSerializer(employee, context={'request': request})
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = EmployeeSerializer(employee, data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def task_list(request):
  permission_classes = (IsAuthenticatedOrReadOnly)
  if request.method == 'GET':
    task = Task.objects.all()
    serializer = TaskSerializer(task, context={'request': request}, many=True)
    return Response({'data': serializer.data})

  elif request.method == 'POST':
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getTask(request, pk):
  """
  Retrieve, update or delete a employee instance.
  """
  try:
    task = Task.objects.get(pk=pk)
  except Task.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = TaskSerializer(task, context={'request': request})
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = TaskSerializer(task, data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def feedback_list(request):
  permission_classes = (IsAuthenticatedOrReadOnly)
  if request.method == 'GET':
    feedback = Feedback.objects.all()
    serializer = FeedbackSerializer(feedback, context={'request': request}, many=True)
    return Response({'data': serializer.data})

  elif request.method == 'POST':
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getFeedback(request, pk):
  """
  Retrieve, update or delete a employee instance.
  """
  try:
    feedback = Feedback.objects.get(pk=pk)
  except Feedback.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = FeedbackSerializer(feedback, context={'request': request})
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = FeedbackSerializer(feedback, data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    feedback.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)







@csrf_exempt
@api_view(['GET', 'POST'])
def meeting_list(request):
  permission_classes = (IsAuthenticatedOrReadOnly)
  if request.method == 'GET':
    meetings = Meeting.objects.all()
    serializer = MeetingSerializer(meetings, context={'request': request}, many=True)
    return Response({'data': serializer.data})

  elif request.method == 'POST':
    serializer = MeetingSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getMeeting(request, pk):
  """
  Retrieve, update or delete a meeting instance.
  """
  try:
    meeting = Meeting.objects.get(pk=pk)
  except Meeting.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = MeetingSerializer(meeting, context={'request': request})
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = MeetingSerializer(meeting, data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    meeting.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
