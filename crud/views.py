from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudentSerializer

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

# Will not find postStudent as it is inside a class
# class StudentView:
#     @staticmethod
#     def postStudent(request):
#         # if request.method == 'POST':
#         data = request.data
#         return Response(data)

