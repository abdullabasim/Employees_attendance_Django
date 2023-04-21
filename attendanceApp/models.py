from django.db import models

# Create your models here.

class employeeDetails(models.Model):

    name = models.CharField(db_column='name',max_length=200)
    email_address = models.EmailField(db_column='email_address', max_length=200)
    emp_id = models.CharField(db_column='emp_id', max_length=50)
    division = models.CharField(db_column='division', max_length=200, blank=True, null=True)
    organization = models.CharField(db_column='organization', max_length=200, blank=True, null=True)
    position = models.CharField(db_column='position', max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'employee_details'

    def __str__(self):
        return self.name
