
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

shape_list = [('oval','Oval'), ('rectangular','Rectangular'), ('canopy','Canopy'), ('elevated','Elevated')]

class Teacher(models.Model):
	teacher_id = models.CharField("Employee ID", unique = True, max_length = 200)
	name = models.CharField("Teacher Name", max_length = 200)
	doj = models.DateField('D.O.J')
	salary = models.IntegerField('Salary') 

	def __str__(self):
		return self.name

class Subjects(models.Model):
	subject_name = models.CharField("Subject", max_length = 200)
	chapters = models.IntegerField('Chapters')
	total_duration =  models.IntegerField('Subject Duration')
	class_duration =  models.IntegerField('Class Duration', default=30, validators=[MaxValueValidator(120), MinValueValidator(30)])
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


	def __str__(self):
		return self.subject_name

class Student(models.Model):
	enrollment_id = models.CharField("Enrollment ID", unique = True, max_length = 200)
	name = models.CharField("Student Name", max_length = 100)
	doj = models.DateField('D.O.J')
	ranking = models.IntegerField('Ranking in school') 

	def __str__(self):
		return self.name

class Relative(models.Model):
	enrollment_id = models.ForeignKey(Student, on_delete = models.CASCADE)
	relative_name = models.CharField("Relative Name", max_length = 100)
	relation = models.CharField("Relation ", max_length = 100)	

class ClassRoom(models.Model):
	class_id = models.CharField("Room No.", max_length=50)
	seating_capacity = models.IntegerField('Seating Capacity')
	web_support = models.BooleanField("Web Support")
	shape =  models.CharField("Class Shape", max_length=50, choices=shape_list, default='rectangular')
	student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
	subject = models.ForeignKey(Subjects, on_delete= models.CASCADE)
