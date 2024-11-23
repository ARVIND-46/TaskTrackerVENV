from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse 
from .models import Task 
from django.contrib.auth.decorators import login_required


# Create your views here.
def taskList(request):
    return render(request,'app1/index.html')

def addTask(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")
        priority = request.POST.get("priority")
        status = request.POST.get("status")
        Task.objects.create(
            #user=request.user,
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            status=status,
        )
        return redirect("task_list")  # Redirect to the task list view

    return render(request,'app1/addTask.html')


def display_tasks(request):
    pending_tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)
    return render(request, 'app1/displayTL.html', {
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks,
    })

def complete_Task(request,task_id):
     if request.method == 'POST':
        # Get the specific task by its ID
        task = get_object_or_404(Task,id=task_id)
        task.is_completed =True
        task.save()
    # Redirect back to the task list view
        return redirect('display_tasks')
def reset_task(request,task_id):
    if request.method =='POST':
        task = get_object_or_404(Task,id=task_id)
        task.status ="Pending"
        task.is_completed = False
        task.save()
        return redirect('display_tasks')     

def displayTL(request):
    tasks = Task.objects.all()  # Fetch all tasks
    return render(request, 'displayTL.html', {'tasks': tasks})

def delTask(request,task_id):
    if request.method == "POST":
        task =get_object_or_404(Task,id=task_id)
        task.delete()
        return redirect('display_tasks')

    



#def editTask:
