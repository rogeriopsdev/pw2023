from django.shortcuts import render
from .forms import Servicoform, Agendaform

# Create your views here.
def index(request):
    return render(request,'agenda/index.html')

def cad_servico(request):
    form = Servicoform()
    if request.method=="POST":
        form = Servicoform(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form = Servicoform()
    return render(request, 'agenda/criar_serv.html',{'form':form})
