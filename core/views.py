from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
import os
import mimetypes
from django.conf import settings
from django.http import HttpResponse, Http404

from .models import Material, Search
from .forms import AddMaterialForm

def home(request):
    return render(request, 'core/index.html')

def add_material(request):
    if request.method == 'POST':
        form = AddMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddMaterialForm()
    context = {'form':form}
    return render(request, 'core/add_material.html', context)


class MaterialsList(ListView):
    paginate_by = 6
    template_name = 'core/materials_list.html'
    model = Material
    context_object_name = 'materials'

    def get_queryset(self):
        return self.model.objects.all()

