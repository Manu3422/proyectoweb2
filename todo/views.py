from django.shortcuts import redirect, render

from .forms import TareaForm
from .models import tarea


def inicio(request):
    Tarea = tarea.objects.all()
    contexto = {
        'Tarea':Tarea
        }
    return render (request,'home.html', contexto)

def CrearTarea (request):
    if request.method == 'GET':
        form = TareaForm()
        contexto = {
            'form':form
        }
    else:
        form = TareaForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('home')
    return render (request,'crear.html',contexto)

def EditarTarea(request,id):
    Tarea = tarea.objects.get(id = id)
    if request.method =='GET':
        form = TareaForm(instance = Tarea)
        contexto = {
            'form':form
        }
    else:
        form = TareaForm(request.POST, instance = Tarea)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request,'crear.html',contexto)

def EliminarTarea(request,id):
    Tarea = tarea.objects.get(id = id)
    Tarea.delete ()
    return redirect ('home')