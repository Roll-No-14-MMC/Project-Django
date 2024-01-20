# Creating API

> First make a virtual environment.<br>
> Then install django and djangorestframework<br>
> create app<br>
> put app and djangorestframework in setting in installed apps<br>
> create models <br>
> make migrations<br>
> migrate<br>

> create postStudent in view.py in app<br>
> create urls.py inside app<br>
> import postStudent and put inside urlpatterns<br>
> Now in project's url, we tell project that you should also check for api/ urls<br>

> Now for POST request:<br>
> make a serializer.py file inside app<br>
> create serializer for user<br>
> inside views.py of the app import serializer(that we made) and response(rest_framework.response) and api_view(rest_framework.decorators)<br>

# https://www.eraser.io/
