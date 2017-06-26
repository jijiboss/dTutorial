from django.views import generic
from .models import Suppliers, Products

class IndexView(generic.ListView):
	template_name='pork02/index.html'
	context_object_name='object_list' #ListView returns "object_list" by default but cn be overridden with using this variable

	def get_queryset(self):
		return Products.objects.all() #this returns an object called "object_list"

class DetailView(generic.DetailView):
	model = Products
	template_name ='pork02/detail.html'
