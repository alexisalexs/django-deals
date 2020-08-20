from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView,TemplateView
import pdb
from .models import Item
from .forms.on_sale_form import SaleItem

class HomePage(ListView):
    template_name = 'client/index.html'
    model = Item

    def get_context_data(self,**kwargs):
        context = super(HomePage,self).get_context_data(**kwargs)
        context['items'] = Item.objects.all().count()
        print(self.request.user.uuid)
        return context