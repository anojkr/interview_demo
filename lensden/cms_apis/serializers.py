from rest_framework import serializers
from .models import Teacher, Student, Relative, Subjects, ClassRoom


class ClassRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassRoom
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subjects
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class RelativeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Relative
        fields = '__all__'