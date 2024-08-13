from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView 
from .models import Articale

class ArticaleList(ListView):
    def get_queryset(self):
        return Articale.objects.filter(status=True)
    
class ArticaleDetail(DetailView):
    def get_object(self):
        return get_object_or_404(Articale.objects.filter(status=True), slug=self.kwargs.get('slug'))
