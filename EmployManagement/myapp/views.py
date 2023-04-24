from django.shortcuts import render, HttpResponse,redirect
from .models import *
import json
from django.core.serializers import serialize

# Create your views here.


####### dashboard
def index(request):
    return render(request, 'index.html')
####### department management ############
#list all departments
def department_index(request):
    departments = Department.objects.all()
    return render(request, 'department.html',{'departments':departments})


def all_departments(request):
    departments = Department.objects.all()
    return render(request,'departmentList.html',{'departments':departments})

# deparment details
def department(request, pk):
    department = Department.objects.get(id = pk)
    services = Service.objects.filter(department=department)
    return render(request, 'department_detail.html',{'department':department, 'services':services})

#add a department
def add_department(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        depart_name = request.POST['name']
        depart_description = request.POST['description']
        deparment = Department(name=depart_name, description=depart_description)
        deparment.save()
        return redirect('/departments/')

# update department details
def update_department(request, pk):
    department = Department.objects.get(id = pk)
    return

#delete a department
def delete_department(request, pk):
    department = Department.objects.get(id = pk)
    department.delete()
    return redirect('/departments/')

###### service management ######

def service_index(request):
    departments = Department.objects.all()
    services = Service.objects.all()
    return render(request, 'service.html',{'services':services, 'departments':departments})


# list all services
def all_services(request):
    services = Service.objects.all()
    return render(request,'serviceList.html',{'services':services})

# service details
def service(request, pk):
    service = Service.objects.get(id = pk)
    return render(request, 'service_detail.html',{'service':service})

#add a service
def add_service(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        service_name = request.POST['name']
        service_description = request.POST['description']
        service_department = request.POST['department_name']
        for department in departments:
            if department.name == service_department:
                service = Service(name=service_name,
                                    description=service_description,
                                    department=department
                                )
                service.save()
                return redirect('/services/') 


# update a service info
def update_service(request, pk):
    service = Service.objects.get(id = pk)
    return

#delete a service
def delete_service(request, pk):
    service = Service.objects.get(id = pk)
    service.delete()
    return redirect('/services/')
