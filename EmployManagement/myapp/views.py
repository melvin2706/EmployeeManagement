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


#list all meetings
def meeting_index(request):
    meetings = Meeting.objects.all()
    return render(request, 'meeting.html',{'meetings':meetings})


def all_meetings(request):
    meetings = Meeting.objects.all()
    return render(request,'meetingList.html',{'meetings':meetings})

# meeting details
def meeting(request, pk):
    meeting = Meeting.objects.get(id = pk)
    #services = Service.objects.filter(department=department)
    return render(request, 'meeting_detail.html',{'meeting':meeting})

#add a meeting
def add_meeting(request):
    meetings = Department.objects.all()
    if request.method == 'POST':
        meeting_subject = request.POST['subject']
        meeting_description = request.POST['description']
        meeting_date = request.POST['date']
        meeting_start = request.POST['start_time']
        meeting_end = request.POST['end_time']
        meeting = Meeting(subject=meeting_subject, description=meeting_description, date=meeting_date, start_time=meeting_start, end_time=meeting_end)
        meeting.save()
        return redirect('/meetings/')

# update meeting details
def update_meeting(request, pk):
    meeting = Meeting.objects.get(id = pk)
    return

#delete a meeting
def delete_meeting(request, pk):
    meeting = Meeting.objects.get(id = pk)
    meeting.delete()
    return redirect('/meetings/')



#list all projects
def project_index(request):
    projects = Project.objects.all()
    return render(request, 'project.html',{'projects':projects})


def all_projects(request):
    projects = Project.objects.all()
    return render(request,'projectList.html',{'projects':projects})

# project details
def project(request, pk):
    project = Meeting.objects.get(id = pk)
    #services = Service.objects.filter(department=department)
    return render(request, 'project_detail.html',{'project':project})

#add a meeting
def add_project(request):
    projects = Project.objects.all()
    if request.method == 'POST':
        project_name = request.POST['name']
        project_description = request.POST['description']
        project_start = request.POST['date_start']
        project_end = request.POST['date_end']
        project = Project(name=project_name, description=project_description, date_start=project_start, date_end=project_end)
        project.save()
        return redirect('/projects/')

# update project details
def update_project(request, pk):
    project = Project.objects.get(id = pk)
    return

#delete a project
def delete_project(request, pk):
    project = Project.objects.get(id = pk)
    project.delete()
    return redirect('/projects/')
