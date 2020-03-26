from django.urls import path, include
from . import views, iviews


urlpatterns = [

	# """	-----------------Function based view ----------------"""
	path("api/", views.show_api, name ="show api"),

    path("api/add_teacher/", views.add_teacher, name="add teachers"),
    path("api/list_teacher/", views.list_teacher_list, name="show teachers"),

	path("api/add_student/", views.add_student, name="add student"),
    path("api/list_student/", views.list_student_list, name="show student"),

    path("api/add_subjects/", views.add_subjects, name="add_subjects"),
    path("api/list_subjects/", views.list_subjects, name="list_subjects"),

    path("api/add_relative/", views.add_relative, name="add_relative"),
    path("api/list_relative/", views.list_student_relative, name="show_relative"),

    path("api/query2/", views.get_sum_teacher_salary, name="show_query1"),


    # """ -----------------Class Based View ----------------------"""

	path("api/class/add_classroom/", iviews.ClassRoomList.as_view()),
	
	path("api/class/add_subject/", iviews.SubjectList.as_view()),

	path("api/class/add_teacher/", iviews.TeacherList.as_view()),

	path("api/class/add_student/", iviews.StudentList.as_view()),

	path("api/class/add_relative/", iviews.RelativeList.as_view()),


]
