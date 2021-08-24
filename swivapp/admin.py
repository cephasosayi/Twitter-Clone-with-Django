from django.contrib import admin
from .models import Swiv
from .forms import SwivModelForm

# Register your models here.

	


class SwivModelAdmin(admin.ModelAdmin):
	
	class Meta:
		model 	= Swiv


admin.site.register(Swiv, SwivModelAdmin)  