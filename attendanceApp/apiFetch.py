import os
import requests
import dotenv

dotenv.read_dotenv()
class ApiFetch():

    @staticmethod
    def fetchApiAttendance(serializer):
        try:

            attendance_response = requests.get(os.environ.get('API_URL'), params=serializer.data,timeout=3000, verify=False)
                                              

            if attendance_response.status_code == 200:
                return (attendance_response.json())
            else:
                return ({"Error": "Something wrong,please try again"})

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
