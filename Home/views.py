import os

from PIL.Image import Image
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView,TemplateView,ListView
from .models import Raw
from django.contrib.auth.mixins import UserPassesTestMixin,PermissionRequiredMixin,LoginRequiredMixin

from django.template import Context

def img(request):
    user=request.user
    image={'image':Raw.objects.filter(user=user).last()}
    return render(request, 'Home/su.html', context=image)
def mylib(request):
    user=request.user
    mylib={'mylib':Raw.objects.filter(user=user)}
    return render(request, 'Home/mylib.html', context=mylib)
class Upload(LoginRequiredMixin,CreateView):
    template_name = 'Home/home.html'
    # form_class = ContactForm
    model = Raw
    fields=['quality','im']
    success_url = 'success'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




