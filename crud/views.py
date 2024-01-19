from django.shortcuts import render

class StudentView:
    @staticmethod
    def postStudent(request):
        data = request.data
        print(data)

