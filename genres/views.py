from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import coll,piece
from django.views import generic
from .forms import UserForm
from django.contrib.auth import authenticate,login
from django.views.generic import View

class genres_view(generic.ListView):
    template_name = "genres/genresTemplates.html"

    def get_queryset(self):
        return coll.objects.all()

class details(generic.DetailView):
    model = coll
    template_name = "genres/detailsTemplates.html"

class UserFormView(View):
    formCls = UserForm
    templateName = "genres/formTemplate.html"

    def get(self,request):
        form = self.formCls(None)
        return render(request,self.templateName,{'form':form})
    
    def post(self,request):
        form = self.formCls(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            newUser = authenticate(username=username,password=password)

            if newUser is not None:
                if newUser.is_active:
                    login(request,newUser)  
                    return redirect("/genres")
        return render(request,self.templateName,{'form':form})