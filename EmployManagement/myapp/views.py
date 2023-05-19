from django.shortcuts import render, HttpResponse,redirect
from .models import *

# Create your views here.


####### dashboard
def index(request):
    department_num = Department.objects.count()
    meeting_num = Meeting.objects.count()
    project_num = Project.objects.count()
    service_num = Service.objects.count()
    user_num = CustomUser.objects.count()
    context = {
        'department_num' : department_num,
        #'meeting_num' : meeting_num,
        'project_num' : project_num,
        'service_num' : service_num,
        'user_num' : user_num
    }
    return render(request, 'index.html', context)
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
    return render(request, 'add_department.html')

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
    users = CustomUser.objects.filter(service=service)
    return render(request, 'service_detail.html',{'service':service, 'users':users})

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
    return render(request,'add_service.html',{'departments':departments})

# add service to department
# we wil pass the department's pk as a parameter
def add_service_department(request, pk):
    department = Department.objects.get(id=pk)
    if request.method == 'POST':
        service_name = request.POST['name']
        service_description = request.POST['description']
        service = Service(name=service_name,
                            description=service_description,
                            department=department
                        )
        service.save()
        return redirect('/department/'+str(department.id))
    return render(request,'add_service_department.html',{'department':department})

# update a service info
def update_service(request, pk):
    service = Service.objects.get(id = pk)
    return

#delete a service
def delete_service(request, pk):
    service = Service.objects.get(id = pk)
    service.delete()
    return redirect('/services/')


#delete a service from department
def delete_department_service(request,dpk, spk):
    department = Department.objects.get(id = dpk)
    service = Service.objects.get(id = spk)
    service.delete()
    return redirect('/department/'+str(department.id))

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
    return render(request,'add_meeting.html')


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
    project = Project.objects.get(id = pk)
    tasks = Task.objects.filter(project=project)
    #services = Service.objects.filter(department=department)
    return render(request, 'project_detail.html',{'project':project, 'tasks':tasks})

#add a project
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
    return render(request,'add_project.html')

# update project details
def update_project(request, pk):
    project = Project.objects.get(id = pk)
    return

#delete a project
def delete_project(request, pk):
    project = Project.objects.get(id = pk)
    project.delete()
    return redirect('/projects/')


####### post management ############
#list all posts
def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post.html',{'posts':posts})


def all_posts(request):
    posts = Post.objects.all()
    return render(request,'postList.html',{'posts':posts})

# post details
def post(request, pk):
    post = Post.objects.get(id = pk)
    return render(request, 'post_detail.html',{'post':post})

#add a post
def add_post(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        post_name = request.POST['name']
        post_description = request.POST['description']
        post = Post(name=post_name, description=post_description)
        post.save()
        return redirect('/posts/')
    return render(request, 'add_post.html')

# update post details
def update_post(request, pk):
    post = Post.objects.get(id = pk)
    return

#delete a post
def delete_post(request, pk):
    post = Post.objects.get(id = pk)
    post.delete()
    return redirect('/posts/')


####### task management ############
#list all tasks
def task_index(request):
    tasks = Task.objects.all()
    return render(request, 'task.html',{'tasks':tasks})


def all_tasks(request):
    tasks = Task.objects.all()
    return render(request,'taskList.html',{'tasks':tasks})

# task details
def task(request, pk):
    task = Task.objects.get(id = pk)
    return render(request,'task_detail.html',{'task':task})

#add task
def add_task(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    users = CustomUser.objects.all()
    if request.method == 'POST':
        task_name = request.POST['name']
        task_description = request.POST['description']
        task_project = request.POST['project']
        task_responsibility = request.user
        for project in projects:
            if project.name == task_project:
                task = Task(name=task_name,
                            description=task_description,
                            project=project,
                            responsible= task_responsibility
                            )
                task.save()
                return redirect('/tasks/')
    return render(request, 'add_task.html',{'projects':projects})

#add a task to project
def add_task_to_project(request,pk):
    project = Project.objects.get(id=pk)
    tasks = Task.objects.all()
    if request.method == 'POST':
        task_name = request.POST['name']
        task_description = request.POST['description']
        task_project = request.POST['project']
        task_responsibility = request.user
        task = Task(name=task_name,
                    description=task_description,
                    project=project,
                    responsible= task_responsibility
                    )
        task.save()
        return redirect('/project/'+str(pk))
    return render(request, 'add_task_project.html',{'project':project})

# update task details
def update_task(request, pk):
    task = Task.objects.get(id = pk)
    return

#delete a task
def delete_task(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return redirect('/tasks/')

#delete a task (ppk ->project pk, tpk ->task pk)
def delete_task_from_project(request, tpk, ppk):
    task = Task.objects.get(id = pk)
    task.delete()
    return redirect('/project/'+str(ppk))
