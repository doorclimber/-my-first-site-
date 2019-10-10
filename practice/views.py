from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse
from .models import profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import posts
from .forms import postWriting, folUsers
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

def getAccountInfo(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            print(username)
            use = username
            info = profile(username = use)
            info.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('thanks'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserCreationForm()
    return render(request, 'practice/name.html', {'form': form})

def pleaselogin(request):
    return render(request, 'practice/pleaselogin.html')

def thanks(request):
    return render(request, 'practice/thanks.html')

def lout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def index(request):
    if request.user.is_authenticated:
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = postWriting(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                writing = form.cleaned_data.get('post_text')
                p1 = profile.objects.get(username=request.user.username)
                #print(username)
                info = posts(user=p1,post_text = writing)
                info.save()
                # redirect to a new URL:
                return HttpResponseRedirect('/practice')
        else:
            # postWriting() creates the correct form unpopulated
            form = postWriting()
            # Django's SQL integration that creates a list of all people p1 is following
            p1 = profile.objects.get(username=request.user.username)
            p1Follows = p1.follows.all()
            print(p1)
            print(posts.objects.filter(user__in= p1Follows))
            varPosts = posts.objects.filter(Q(user = p1)|Q(user__in= p1Follows)).order_by('-id')[:10]
        
        # renders new webpage with list of posts taken from SQL database
        return render(request, 'practice/index.html', {'form': form,'varPosts' : varPosts})
    else:
        # returns 'please login' page
        return pleaselogin(request) #HttpResponse('please login to see this page')
    
def followUsers(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = folUsers(request.POST)
            if form.is_valid():
                tUser = form.cleaned_data.get('tried_user')
                foundUser = profile.objects.filter(username=tUser)
                if foundUser.count() == 0:
                    print('no user')
                else:
                    foundUser = profile.objects.get(username=tUser)
                    p1 = profile.objects.get(username=request.user.username)
                    p1.follows.add(foundUser)
                    p1.save()
                    print(p1.follows.all())
                    
                return HttpResponseRedirect(reverse('thanks'))
        else:
            form = folUsers()
        return render(request, 'practice/follow.html', {'form': form})
    else:
        return pleaselogin(request)

def reviews(request):
    return render(request, 'practice/reviews.html')

def ridgefieldlibrary(request):
    return render(request, 'practice/reviews/ridgefield_library.html')


