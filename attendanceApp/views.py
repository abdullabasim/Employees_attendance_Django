
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializersData import EmployeeDetailsSerializer ,InputDataSerializer ,ManualSerializer
from .models import employeeDetails
from .apiFetch import ApiFetch
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getEmployeeAttendance(request):


    inputSerializer = InputDataSerializer(data=request.query_params)

    if inputSerializer.is_valid():

       attendanceResponseApi = ApiFetch.fetchApiAttendance(inputSerializer)

       employeeData =  get_object_or_404(employeeDetails,emp_id =inputSerializer.data['emp_id'])

       employeeSerializer = EmployeeDetailsSerializer(employeeData,many=False)

       resultData=  ManualSerializer.resultSerialized(attendanceResponseApi , inputSerializer,employeeSerializer)

       return Response(resultData)
    else:
        return Response(inputSerializer.errors)



