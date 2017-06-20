Fresh Django virtual environment

	1.	Create a new folder called "freshDjango" and CD into it
	2.	virtualenv virt_env
	3.	"cd virt_env" once done and ".\scripts\activate.bat"
	4.	"pip install django"
	5.	Startup the virtual environment
	
			scripts\actvate.bat
			
	6.	May want to check for updates to Django before stating

			"pip install django -U"
		
	7.	Create a Django project to get started

			django-admin startproject <proj_name>

	8.	To start the web server, go to the folder with manage.py then
	
			python manage.py runserver
			
	9.	Go into this new project folder and create your app

			"python manage.py startapp <app_name>"

	10.	Don't forget to create the admin user
	
			python manage.py createsuperuser
			
			