from django.contrib import admin
from django.urls import path
from .views import deleteStudnet, editStudnet, getStudent, getTeacher, oneTeacher, postStudent, postTeacher, oneStudnet

urlpatterns = [
    path('add-student/',postStudent),
    path('add-teacher/',postTeacher),
    path('list-teacher/',getTeacher),
    path('list-student/',getStudent),
    path('one-student/<id>',oneStudnet),
    path('one-teacher/<id>',oneTeacher),
    # path('edit-student/<int:id>',editStudentData),
    path('edit-student/<id>',editStudnet),
    path('delete-student/<id>',deleteStudnet),
]