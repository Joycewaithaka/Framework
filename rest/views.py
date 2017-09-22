from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from rest_framework import viewsets
from django.shortcuts import render
from .serializers.rest import StudentSerializer



# Create your views here.

def welcome(request):
    return render(request,'listing_student.html')
def students(request):
    students=Student.objects.all()
    
    context ={
        'students':students
    }
    return render(request,'listing_student.html',context)
    
     
#viewSets define the view behaviour
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

# Create your views here.
