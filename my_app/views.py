from django.shortcuts import render

def task_view(request):
    data = {'dynamic_data': 'Hello, this is dynamic data!'}
    return render(request, 'task.html', context=data)
