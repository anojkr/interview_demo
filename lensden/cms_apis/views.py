from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ClassRoomSerializer, TeacherSerializer, StudentSerializer, RelativeSerializer, SubjectSerializer
from .models import Teacher, Student, Subjects, ClassRoom, Relative


from django.http import HttpResponse
from django.core import serializers
import json


@api_view(['GET'])
def show_api(request):
	data= ['api/show_teacher/', 'api/add_teacher/', 'api/show_student/', 'api/add_student/']
	return Response(data)

@api_view(['GET'])
def list_teacher_list(request):
	tasks = Teacher.objects.all()
	serializer = TeacherSerializer(tasks, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def add_teacher(request):
	serializer = TeacherSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data,  status=200)
	return Response(serializer.data,  status=400)


@api_view(['GET'])
def list_student_list(request):
	tasks = Student.objects.all()
	serializer = StudentSerializer(tasks, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def add_student(request):
	serializer = StudentSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data,  status=200)
	return Response(serializer.data,  status=400)


@api_view(['GET'])
def list_student_relative(request, student_id):
	tasks = Relative.objects.filter(enrollment_id = student_id)
	serializer = RelativeSerializer(tasks, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def add_relative(request):
	serializer = RelativeSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data,  status=200)
	return Response(serializer.data,  status=400)

@api_view(['GET'])
def list_subjects(request):
	tasks = Subjects.objects.filter()
	serializer = SubjectSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['Post'])
def add_subjects(request):
	serializer = SubjectSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data,  status=200)
	return Response(serializer.data,  status=400)

@api_view(['GET'])
def get_sum_teacher_salary(request):

		query_teacher = Teacher.objects.filter(salary__gt = '100000')
		student = Student.objects.filter()
		res = {
			'users': {}
		}

		for user in query_teacher:
			res['users'][user.teacher_id] = {
			'Teacher Id': user.teacher_id,
			'Name': user.name,
			'Salary': user.salary,
			}

		data = json.dumps(res)
		return HttpResponse(data, content_type="application/json")


