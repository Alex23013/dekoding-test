    
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect

from .forms import DogForm
from .models import Dog




class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        context = {}

        return render(request, self.template_name, context)


class FrontendView(View):
    template_name = "frontend.html"

    def get(self, request):
        context = {}

        return render(request, self.template_name, context)


class BackendView(View):
    template_name = "backend.html"

    def get(self, request):
        context = {}

        return render(request, self.template_name, context)

class DogListView(View):
    template_name = "dog/list.html"
    
    def get(self, request):
        dogs=Dog.objects.all()
        context = {'dogs': dogs}

        return render(request, self.template_name, context)


class DogAddView(View):    
    template_name = "dog/add.html"

    def post(self, request, **kwargs):
        form = DogForm(request.POST)
        
        if form.is_valid():
            newDog = Dog(name = request.POST["name"], breed = request.POST["breed"], age = request.POST["age"], owner = request.POST["owner"])
            newDog.save()
            return HttpResponseRedirect("/dog/list")

    def get(self, request):
        form = DogForm()
        context = {'form': form}
        return render(request, self.template_name, context)