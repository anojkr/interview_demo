Readme.

Step1. pip3 install requirement.txt

Step2. Setup Postgres Database

Go to lensden/setting.py

//Make changes to file according to database setup
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME' : 'database_name',
        'USER' : 'user_name',
        'PASSWORD' : 'user_password',
        'HOST' : 'localhost',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


Step3 : Run Migration

cd  lensden

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver


Step 3. Api calls


Class based class
	1. Add classroom
		api/class/add_classroom/
	2. Add subject
		api/class/add_subject/
	3. Add Teacher
		api/class/add_teacher/
	4. Add Student
		api/class/add_student/
	5. Add Relative
		api/class/add_relative/


Function based API calls

	1. Add teacher to school 
		api/add_teacher/

	2. List all teacher in school
		api/list_teacher/
	
	3. Add Student to school
		api/add_student/

	4. Add subject to  school
		api/add_subjects/
		
	5. List all available subjects	
	 	api/list_subjects/

	6. Add relative of students 
		api/add_relative/
	
	7. List all relatives 
		api/list_relative/




