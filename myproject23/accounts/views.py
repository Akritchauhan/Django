from django.shortcuts import redirect, render
from .forms import ProfileForm
from .models import Profile
from django.contrib import messages
def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile uploaded successfully!')
            return redirect('view_profile')
        else:
            messages.error(request, 'Error uploading profile. Please try again.')
    else:
        form = ProfileForm()
    return render(request, 'upload_profile.html', {'form': form})

def view_profile(request):
    profiles = Profile.objects.all()
    return render(request, 'view_profile.html', {'profiles': profiles})
