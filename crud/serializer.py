from .models import Student
from .models import Teacher
from rest_framework import serializers

# To change the requested info into JSON format
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        field = '__all_'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        field = '__all_'