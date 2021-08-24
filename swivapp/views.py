from django.shortcuts import render, get_object_or_404, redirect
from .models import Swiv
from django.db.models import Q
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)
from .forms import SwivModelForm
from .mixins import FormUserNeededMixin,OwnerUserMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect



from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.
#create view
class ReshareView(View):
	def get(self, request, pk, *args, **kwargs):
		swiv = get_object_or_404(Swiv, pk=pk)
		if request.user.is_authenticated():
			new_swiv=Swiv.objects.reshare(request.user, swiv)
			return HttpResponseRedirect("/")
		return HttpResponseRedirect(swiv.get_absolute_url())

class Create(FormUserNeededMixin,CreateView):
	form_class = SwivModelForm
	template_name = "swiv/create_view.html"	
	#success_url ="/swivapp/create"

#up date 
#mixture of detail and create view
class Update(LoginRequiredMixin,OwnerUserMixin,UpdateView):
	queryset= Swiv.objects.all()
	form_class = SwivModelForm
	template_name = "swiv/update.html"	
	#success_url ="/swivapp/"

#delete

class Delete(LoginRequiredMixin,DeleteView):
	model = Swiv
	template_name = "swiv/delete.html"	
	success_url =reverse_lazy("swivapp:list")



class SwivListView(LoginRequiredMixin, ListView):
	template_name = "swiv/list_view.html"
	def get_queryset(self,*args, **kwargs):
		qs = Swiv.objects.all()
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(content__icontains=query) | #complex lookups, check making queries doc
				Q(user__username__icontains=query)
				
				)
		return qs


	
	def get_context_data(self,*args, **kwargs):
		context = super(SwivListView,self).get_context_data(*args, **kwargs)
		context['create_form']= SwivModelForm()
		context['create_url']= reverse_lazy("swivapp:create")
		return context

class SwivDetailView(DetailView):
	queryset= Swiv.objects.all()
	template_name = "swiv/detail_view.html"
	
	#def get_object(self):
	#	print(self.kwargs)
	#	pk = self.kwargs.get("pk")
	#	return Swiv.objects.all()




#def  detail_view(request, id=1):
	#obj = Swiv.objects.get(id=id)
	#print(obj)
	#context = {
	#"object": obj
	#}
	#return render(request,"swiv/detail_view.html", context)


##def  list_view(request, id=1):
#	queryset = Swiv.objects.all()
#	print(queryset)
#	for obj in queryset:
#		print(obj.content)
#	context = {
#	"object": queryset
#	}
#	return render(request,"swiv/list_view.html", context)