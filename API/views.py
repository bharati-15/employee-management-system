from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .serialiser import EmployeeDetailsSerialiser, DepartmentSerialiser, SkillsSerialiser
from rest_framework import permissions

from .models import EmployeeDetails, Department, Skills

# Create your views here.
def home(request):
    return HttpResponse("welcome to our home page")

class Empviewset(viewsets.ViewSet):
    permission_classes=[permissions.IsAuthenticated]
    queryset=EmployeeDetails.objects.all()
    serializer_class=EmployeeDetailsSerialiser

    def list(self, request):
        display=self.queryset
        serializer=self.serializer_class(display, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        skill = self.queryset.get(pk=pk)
        serializer = self.serializer_class(skill)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    def update(self,request, pk=None):
        mevabemp=self.queryset.get(pk=pk)
        serializer=self.serializer_class(mevabemp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    def destroy(self, request, pk=None):
        mevabemp=self.queryset.get(pk=pk)
        mevabemp.delete()
        return Response(status=204)
    
class Departmentviewset(viewsets.ViewSet):
    permission_classes=[permissions.IsAuthenticated]
    queryset=Department.objects.all()
    serializer_class=DepartmentSerialiser

    def list(self, request):
        display=self.queryset
        serializer=self.serializer_class(display, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        skill = self.queryset.get(pk=pk)
        serializer = self.serializer_class(skill)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    def update(self,request, pk=None):
        mevabemp=self.queryset.get(pk=pk)
        serializer=self.serializer_class(mevabemp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    def destroy(self, request, pk=None):
        mevabemp=self.queryset.get(pk=pk)
        mevabemp.delete()
        return Response(status=204)
    
    
class Skillsviewset(viewsets.ViewSet):
    permission_classes=[permissions.IsAuthenticated]
    queryset=Skills.objects.all()
    serializer_class=SkillsSerialiser

    def list(self, request):
        display=self.queryset
        serializer=self.serializer_class(display, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        skill = self.queryset.get(pk=pk)
        serializer = self.serializer_class(skill)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    def update(self,request, pk=None):
        mevabemp=self.queryset.get(pk=pk)
        serializer=self.serializer_class(mevabemp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    def destroy(self, request, pk=None):
        mevabemp=self.queryset.get(pk=pk)
        mevabemp.delete()
        return Response(status=204)
    
