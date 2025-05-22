from django.shortcuts import render, redirect
from .models import Paciente
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def submit_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        symptoms = request.POST.get('symptoms')
        diagnosis = request.POST.get('diagnosis')
        treatment = request.POST.get('treatment')

        paciente = Paciente(
            name=name,
            age=age,
            symptoms=symptoms,
            diagnosis=diagnosis,
            treatment=treatment
        )
        paciente.save()
        return redirect('index')
    else:
        return redirect('index')
