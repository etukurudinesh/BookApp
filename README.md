# BookApp
This is an app to manage books and authors.

This read me file guides the users on how to download and run the application on your pc (windows OS)

<h3>Important</h3>

**Have python 3.8 or higher installed on the local machine / PC**

run the following command in terminal to check the python version
```
python --version
```
<hr>


<h3>Instructions on running the application</h3>

1. Open the file path in the terminal or command prompt
2. go into BookApp folder (cd BookApp)

Run the following commands in command promp or vs terminal (in order) to setup a virtual environment

In the wagtailTest folder path (C:\\....\BookApp> )

```
python -m venv bookapp\env
```
```
bookapp\env\Scripts\activate
```
```
pip install wagtail
```
```
cd bookapp
```
```
pip install -r requirements.txt
```
<hr>

<h3>Commands to run the web server and applicaton</h3>

run the commands in order

```
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

