from django.shortcuts import render

# Create your views here.
def signup_user(request):
    context = {}
    return render(request, 'accounts/register-page.html',context)

def signin_user(request):
    context = {}
    return render(request, 'accounts/signin_user.html', context)

def signout_user(request):
    context = {}
    return None

def details_profile(request, pk):
    context = {}
    return render(request, 'accounts/profile-details-page.html',context)

def edit_profile(request, pk):
    context = {}
    return render(request, 'accounts/profile-edit-page.html', context)

def delete_profile(request, pk):
    context = {}
    return render(request, 'accounts/profile-delete-page.html', context)