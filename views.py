from django.shortcuts import render

def task_page(request):
    dynamic_data = "This is dynamic data."
    return render(request, 'myapp/task.html', {'dynamic_data': dynamic_data})






