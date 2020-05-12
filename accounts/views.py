from django.urls import reverse_lazy,reverse
from .forms import SignUpForm,MaterialForm
from django.views import generic
from  django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import Student
from scholarswork.models import Coursefiles,Material
from django.contrib import messages

# Create your views here.

class SignUp(generic.View):
    # form_class = SignUpForm
    # success_url = reverse_lazy('login')
    # template_name = 'accounts/signup.html'
    def get(self,*args, **kwargs):
        form = SignUpForm()
        return render(self.request,'accounts/signup.html',{'form':form})
    def post(self,*args, **kwargs):
        if self.request.method == 'POST':
            form = SignUpForm(self.request.POST)
            if form.is_valid():
                user = form.save()
                student = Student(user=user,uploads=0)
                student.save()
                messages.info(self.request,'Successful Sign  Up!')
                return redirect('accounts:login')
            messages.info(self.request,"Form is not valid")
        else:
            form = SignUpForm()
        return render(self.request,'accounts/signup.html',{'form':form})
    

            
class ByeView(generic.TemplateView):
    template_name = 'accounts/logout.html'

@login_required
def dashboard(request):
    return render(request,"accounts/dashboard.html")

@login_required
def upload_material(request,username):
    if request.method == "POST":
        form = MaterialForm(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            file = form.cleaned_data['file']
            coursefile = Material(title = title,file = file,uploader=request.user.student)
            coursefile.save()
            messages.info(request,"successfully uploaded")
            redirect('accounts:upload',username = request.user.username)
    else:
        form = MaterialForm()
    return render(request,'accounts/upload.html',{'form':form})

def self_uploads(request):
    my_uploads = Material.objects.filter(uploader = request.user.student,approved=True).all()
    return render(request,'accounts/my_uploads.html',{'uploads':my_uploads})
