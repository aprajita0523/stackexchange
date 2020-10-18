from django.shortcuts import render
from .models import Profile
from .forms import ProfileModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def my_profile_view(request):
    profile = Profile.objects.get(user=request.user) # pass this as argument below in form
    #first user in argument is of Profile and second one is request)
    
    #intansiate the form 
    form = ProfileModelForm(request.POST or None ,request.FILES or None ,instance=profile)
    confirm = False
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True



    context = {
        'profile': profile,
        'form': form,
        'confirm' : confirm
    }

    return render(request,'profiles/myprofile.html' ,context)
