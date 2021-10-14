from typing import List
from django.http.response import HttpResponse

from myapp.forms import CreateComicForm
from .models import Chapter,Comic,Review,Subscription, User
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.urls import reverse

'''from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import datetime
from django.template.context import RequestContext
from myapp.models import Dreamreal
from django.core.mail import send_mail
from django.views.generic import TemplateView
from myapp.forms import LoginForm

def formView(request):
   if 'username' in request.COOKIES and 'last_connection' in request.COOKIES:
      username = request.COOKIES['username']
      
      last_connection = request.COOKIES['last_connection']
      last_connection_time = datetime.datetime.strptime(last_connection[:-7], 
         "%Y-%m-%d %H:%M:%S")
      
      if (datetime.datetime.now() - last_connection_time).seconds < 10:
         return render(request, 'loggedin.html', {"username" : username})
      else:
         return render(request, 'login.html', {})
			
   else:
      return render(request, 'login.html', {})

def login(request):
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
   else: 
      MyLoginForm = LoginForm()
	
   response = HttpResponse(username)
   
   response.set_cookie('last_connection', datetime.datetime.now())
   response.set_cookie('username', username)
   
   return response

def hello(request):
   today = datetime.datetime.now().date()
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "hello.html", {"today" : today,"days_of_week" : daysOfWeek})

def viewArticle(request, articleId):
   text = "Displaying article Number : %s" % articleId
   return redirect(viewArticles,month = "12",year = "2021")

def viewArticles(request, month, year):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)

def sendSimpleEmail(request,emailto):
   res = send_mail("hello paul", "comment tu vas?", "ahmed1el1adly@gmail.com", [emailto])
   return HttpResponse('%s'%res)

def crudops(request):
   #Creating an entry
   
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   
   #Read ALL entries
   objects = Dreamreal.objects.all()
   res ='Printing all Dreamreal entries in the DB : <br>'
   
   for elt in objects:
      res += elt.name+"<br>"
   
   #Read a specific entry:
   sorex = Dreamreal.objects.get(name = "sorex")
   res += 'Printing One entry <br>'
   res += sorex.name
   
   #Delete an entry
   res += '<br> Deleting an entry <br>'
   sorex.delete()
   
   #Update
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   res += 'Updating entry<br>'
   
   dreamreal = Dreamreal.objects.get(name = 'sorex')
   dreamreal.name = 'thierry'
   dreamreal.save()
   
   return HttpResponse(res)
   
def datamanipulation(request):
   res = ''
   
   #Filtering data:
   qs = Dreamreal.objects.filter(name = "paul")
   res += "Found : %s results<br>"%len(qs)
   
   #Ordering results
   qs = Dreamreal.objects.order_by("name")
   
   for elt in qs:
      res += elt.name + '<br>'
   
   return HttpResponse(res)
'''

class UserCreate(CreateView):
  
    # specify the model for create view
    model = User
    # specify the fields to be displayed
    
    def get_context_data(self, *args, **kwargs):
        context = super(UserCreate,
             self).get_context_data(*args, **kwargs)
        # add extra field 
        context["title"] = 'Sign up'
        return context

    fields = ['username', 'password']
    
    def get_success_url(self):
      obj = User.objects.last()
      return reverse('user_details', kwargs={'pk': getattr(obj,'id')})

class UserList(ListView):
  
    # specify the model for create view
    model = User
    
    # specify the fields to be displayed
  
    fields = ['username']

class UserDetails(DetailView):
   model = User

   def get_context_data(self, *args, **kwargs):
        context = super(UserDetails,
             self).get_context_data(*args, **kwargs)
        # add extra field 
        comicList = []
        subsList = Subscription.objects.filter(user_id = context["object"].id)
        for subs in subsList:
           comicList += Comic.objects.filter(id = subs.comic_id_id)
        
        context["comiclist"] = comicList
        context["recommendedComics"] = Comic.objects.all()
        return context

class UserUpdate(UpdateView):
   model = User

   fields = [
      "password"
   ]

   def get_context_data(self, *args, **kwargs):
        context = super(UserUpdate,
             self).get_context_data(*args, **kwargs)
        # add extra field 
        context["title"] = 'Update Password'
        return context

   success_url = '/'

class UserDelete(DeleteView):
   model = User

   success_url = '/myapp/user/details'

class ComicCreate(CreateView):
   model = Comic

   form_class = CreateComicForm

   def get_context_data(self, *args, **kwargs):
        context = super(ComicCreate,
             self).get_context_data(*args, **kwargs)
        # add extra field
        context["title"] = 'Create Comic'
        return context
        
   def form_valid(self, form):
      form.instance.creator = User.objects.get(id = self.kwargs['uid'])
      return super().form_valid(form)
   
   def get_success_url(self):
      obj = Comic.objects.last()
      return reverse('comic_detail', kwargs={'pk': getattr(obj,'id')})

class ComicList(ListView):
   model = Comic

   fields = ['name','genre','creator']

class ComicDetails(DetailView):
   model = Comic

   def get_context_data(self, *args, **kwargs):
        context = super(ComicDetails,
             self).get_context_data(*args, **kwargs)
        # add extra field
        reviews = Review.objects.filter(comic_id = context["object"].id)
        context['reviews'] = reviews
        
        return context

