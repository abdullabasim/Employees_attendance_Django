from rest_framework import serializers
from .models import employeeDetails

class EmployeeDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = employeeDetails
        fields = '__all__'

class InputDataSerializer(serializers.Serializer):
    emp_id = serializers.CharField(max_length=100,required = True)
    start_date = serializers.DateField(required = True,format="%Y-%m-%d")
    end_date = serializers.DateField(required = True,format="%Y-%m-%d")





class ManualSerializer():


    @staticmethod
    def resultSerialized(attendanceResponseApi, inputSerializer, employeeSerializer):
        attendanceList = list()
        for result in attendanceResponseApi:
            attendanceList.append({
                "Date": result['C_Date'],
                "Time In": result['time_in'],
                "Time Out": result['time_out'],
                "Working Hours": result['working_hours'],
                "Late": result['late'],
                "Exception Type": result['Exception_type'],
                "Justification": result['Justification'],
                "PA Comment": result['pa_comment'],
                "Absence Creation Date": result['absence_creation_date'],
                "Absence Start Date": result['start_date'],
                "Absence End Date": result['end_date'],
                "Absence Days": result['absence_days'],
                "Normal OverTime": result['over_time'],
                "Holiday Normal OverTime": result['holiday_over_time'],

            })
        dispalyData = {
            "Employee ID": inputSerializer.data['emp_id'],
            "Employee Full Name": employeeSerializer.data['name'],
            "Employee Email Address": employeeSerializer.data['email_address'],
            "Employee Position": employeeSerializer.data['position'],
            "Employee Division": employeeSerializer.data['division'],
            "Employee Organization": employeeSerializer.data['organization'],
            "Supervisor Full Name": attendanceResponseApi[0]['supervisor_full_name'],
            "Shift": attendanceResponseApi[0]['shift'] if attendanceResponseApi else None,
            "Shift Start Date": attendanceResponseApi[0]['shift_start_date'] if attendanceResponseApi else None,
            "Shift End Date": attendanceResponseApi[0]['shift_end_date'] if attendanceResponseApi else None,
            "Attendance Details": attendanceList
        }
        return dispalyData