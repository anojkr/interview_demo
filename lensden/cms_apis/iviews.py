from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import ClassRoomSerializer, TeacherSerializer, StudentSerializer, RelativeSerializer, SubjectSerializer
from .models import Teacher, Student, Relative, Subjects, ClassRoom

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics



class ClassRoomList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """

    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer

class TeacherList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class SubjectList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """

    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer

class StudentList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RelativeList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """

    queryset = Relative.objects.all()
    serializer_class = RelativeSerializer


    # def get(self, request, format=None):
    #     snippets = Student.objects.all()
    #     serializer = StudentSerializer(snippets, many=True)
    #     return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = StudentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)