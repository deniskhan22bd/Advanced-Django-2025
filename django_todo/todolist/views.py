from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    return render(request, "base.html", {"todo_list": todos})

@require_http_methods(["POST"])
def add(request):
    title = request.POST["title"]
    todo = Todo(title=title)
    todo.save()
    return redirect("index")

@require_http_methods(["POST"])
def update(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    new_title = request.POST.get("title")

    if new_title:
        todo.title = new_title  # Update title if provided
    todo.save()
    
    return redirect("index")

def toggle(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect("index")

def delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect("index")
