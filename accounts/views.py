from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
#from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.views import View
from .views import DetailView
from .models import UserProfile
from django.views.generic.edit import FormView

# Create your views here.
from accounts.forms import UserRegisterForm

User = get_user_model()

class UserregisterView(FormView):
    template_name = 'accounts/userRegForm.html'
    form_class = UserRegisterForm
    success_url = '/login'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return super(UserregisterView, self).form_valid(form)

class UserDetailView(DetailView):
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()
 
    
    def get_object(self):
        return get_object_or_404( User, username__iexact=self.kwargs.get("username") )

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        following = UserProfile.objects.is_following(self.request.user, self.get_object())
        context['following'] = following
        context['recommended'] = UserProfile.objects.recommended(self.request.user)
        return context 



class UserFollowView(View):
	def get(self, request, username, *args, **kwargs):
		toggle_user = get_object_or_404(User, username__iexact=username)
		if request.user.is_authenticated():
			is_following=UserProfile.objects.toggle_follow(request.user, toggle_user)
		return redirect("profiles:detail", username=username)