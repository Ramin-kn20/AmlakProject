from django.shortcuts import render
from . import models

def melk_list(request):
    AMLAK = models.Amlak.objects.all().order_by('-Publish')
    return render(request, 'melk/melk_list.html', {'AMLAK': AMLAK})

def melk_details(request, slug):
    MELK = models.Amlak.objects.get(Slug=slug)
    return render(request, 'melk/melk_details.html', {'MELK': MELK})