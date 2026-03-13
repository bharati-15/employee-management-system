from rest_framework import serializers
from .models import EmployeeDetails, Department, Skills
from .models import *

class EmployeeDetailsSerialiser(serializers.ModelSerializer):

    class Meta:
        model=EmployeeDetails
        #fields={'first_name','last_name'}

        exclude=('created_at','modified_at')

class DepartmentSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Department

        exclude=('created_at','updated_at')

class SkillsSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Skills
        fields=('name','description','dept')
        fields='__all__'
       