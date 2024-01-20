from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudentSerializer, TeacherSerializer
from .models import Student,Teacher

# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt

# Will not accept class methods only accepts functions
@api_view(['POST'])
def postStudent(request):
    try:
        request_data = request.data
        serializer = StudentSerializer(data=request_data, many= False)
        # return Response(data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': "student added successfully!"})
    except Exception as e: 
        return Response({"err": str(e)})

@api_view(['POST'])
def postTeacher(request):
    try:
        request_data = request.data
        serializer = TeacherSerializer(data=request_data, many= False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': "Teacher added successfully!"})
    except Exception as e:
        return Response({"err": str(e)})

@api_view(['GET'])
def getStudent(request):
    try:
        # get all objects of class student,or necessary information from the database
        response = Student.objects.all()
        serializer = StudentSerializer(response, many=True)
         # serializer can cause exception if the data on the server is null
        # if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)
    except Exception as e:
        return Response({"err": str(e)})

@api_view(['GET'])
def getTeacher(request):
    try:
        # get all objects of class student,or necessary information from the database
        response = Teacher.objects.all()
        serializer = TeacherSerializer(response, many=True)
        # serializer can cause exception if the data on the server is null
        # if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)
    except Exception as e:
        return Response({"err": str(e)})

@api_view(['GET'])
def oneStudnet(request,id):
    try:
        response = Student.objects.get(pk=id)
        serializer = StudentSerializer(response)
        if serializer.is_valid():
            return Response(serializer.data)
    except Exception as e:
        return Response(f'error: {e}')

@api_view(['GET'])
def oneTeacher(request,id):
    try:
        response = Teacher.objects.get(pk=id)
        serializer = TeacherSerializer(response)
        if serializer.is_valid():
            return Response(serializer.data)
    except Exception as e:
        return Response(f'error: {e}')

@api_view(['GET'])
def editStudnet(request,id):
    try:
        response = Student.objects.get(id=id)
        serializer = StudentSerializer(response,many=False,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": f"data updated successfully{serializer.data}"})
        # return Response({"message": f"data did updated"})
    except Exception as e:
        return Response(f'error: {e}')

@api_view(['GET'])
def deleteStudnet(request,id):
    try:
        response = Student.objects.get(id=id)
        # serialize garnu pardaina kina ki 
        response.delete()
        return Response(f'{response} deleted duccessfully!!')
        # return Response({"message": f"data did updated"})
    except Exception as e:
        return Response(f'error: {e}')

# Will not find postStudent as it is inside a class
# class StudentView:
#     @staticmethod
#     def postStudent(request):
#         # if request.method == 'POST':
#         data = request.data
#         return Response(data)

