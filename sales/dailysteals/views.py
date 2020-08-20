from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView,TemplateView
import pdb
from .models import Item
from .forms.on_sale_form import SaleItem
from django.urls import reverse
# class HomePage(ListView):
#     template_name = 'client/index.html'
#     model = Item
#
#     def get_context_data(self,**kwargs):
#         context = super(HomePage,self).get_context_data(**kwargs)
#         context['items'] = Item.objects.all().count()
#         print(self.request.user.uuid)
#         return context


class test(TemplateView):
    template_name = 'client/test.html'
#
#
#
#
# class ItemOnSaleCreateView(CreateView):
#     template_name = 'client/index.html'
#     model = Item
#     success_url = reverse('dailysteals:test_page.html')
#
#
#     def get_form_kwargs(self):
#         return pass
#
#     def get_context_data(self, **kwargs):
#         context = super(ItemOnSaleCreateView,self).get_context_data(**kwargs)
#         context['item'] = Item.objects.all().filter(uuid=self.kwargs['first_name'])
#         return context
#
#     def form_valid(self, form):
#         return form
#
#
#
#     def post(self, request, *args, **kwargs):
#             if 'file_name' in request.POST:
#                 x='form.error'
#                 x
#
