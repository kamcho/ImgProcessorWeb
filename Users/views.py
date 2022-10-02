from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import render,redirect
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView,TemplateView
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegister,UserUpdate
# from .models import Profile,About?
from django.urls import reverse
# from .models import Posts

# from .models import Posts



from django.contrib import messages
# Create your views here.
def Register(request):

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user=form.save()
            uname = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {uname}')
            # signin=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            login(request,user)
            return redirect('home')
    else:
        form=UserRegister()
    return render(request,'Users/Register.html',{'form':form})

from django.urls import reverse_lazy


