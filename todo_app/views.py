from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse



# Create your views here.

# having data in database how to get collect and how to interaction data use model and model create data and data tabel and data fields into database. use here this model for interaction and collect and show in html page by using function
# model use: data add,modification,delete and update
# model is like as phone to call or conversation with database
# python ORM connet python with database and it convert python object to data for database and arrage data for database 


def task_list(request):
    task = Task.objects.all() #takeing all data from Task class which containing in model

    completed = request.GET.get('complete') #get url string/query string
    if completed == 'true':
        task = task.filter(completed=True) # filter and reasine task value in task
    if completed == "false":
        task = task.filter(completed = False)


    data = {
        "tasks":task
    }
    return render(request,'task_list.html',context=data) #sent data to html to view


def task_details(request,pk):
    tasks = Task.objects.get(pk = pk)
    print(type(tasks))
    
    data = {
        'task':tasks
    }
    
    return render(request,'task_details.html',context=data)

# add data using model
def add_task(request):
    _title = "Let's have dinner together X"
    _description = "Dinner invitation at Chefs Table X"
    _completed = False
    _created_at = "2024-08-28"
    _due_date ='2024-08-28'
    task = Task(title = _title,description = _description,completed = _completed,created_at = _created_at)
    task.save()
    return redirect('task_list')

 #CRUD: create , rearch  , update , delete: can operation any database  



def delete_task(request,pk):
    try:
        task = Task.objects.get(pk=pk)
        task.delete()
        return redirect("task_list")
    except Task.DoesNotExist:
        return HttpResponse("Task does not exist")
        # return render(request,'error_html',context={"data":data})
    

def update_task(request):
    task = Task.objects.get(pk=2)
    task.title = "this is update task"
    task.save()
    return redirect('task_list')
    

# connet form with model after completing form create model.model collect data , write data from form
# for every model need one form

def add_form(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        
    else:
        form = TaskForm()
        return render(request,'task_form.html',{'form':form})
    