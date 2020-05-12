from django.views import generic
from .models import School,Course,Coursefiles,Material,Products
from django.shortcuts import get_object_or_404,render,HttpResponse
from .forms import CourseDownloadForm
import datetime
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test



# HomePage
class HomePage(generic.TemplateView):
    template_name = 'index.html'

# School List
class SchoolListView(generic.ListView):
    model = School
    ordering = ['name']
    template_name = 'school_list.html'

class SchoolCreateView(generic.CreateView):
    model = School
    fields = "__all__"
    template_name = 'school_create.html'

class SchoolCourseListView(generic.DetailView):
    model = School
    template_name = 'school_course_list.html'


class ProductDetail(generic.DetailView):
    model = Products
    template_name = 'products_detail.html'

def download(request,slug,pk):
    coursefile_temp = get_object_or_404(Coursefiles,school__slug=slug,course__pk=pk)
    if request.method == 'POST':
        form = CourseDownloadForm(request.POST or None)
        if form.is_valid():
            year_given = form.cleaned_data.get('year')
            try:
               file_searched = Coursefiles.objects.get(course__pk=pk,school__slug=slug,year=year_given[0])
               files = file_searched
               return render(request, "single.html", {'coursefile': files,'year':year_given})
            except:
                messages.error(request,"File not uploaded, check again later")
    else:
        form = CourseDownloadForm()

    return render(request,'temp.html',{'form':form,'coursefiles':coursefile_temp})


def material_approve(request,pk):
    if request.user.is_superuser:
        material = get_object_or_404(Material,pk=pk)
        material.approve()
        messages.info(request,'Successfully approved')
        return redirect('admin_materials')
    else:
        return redirect('accounts:dashboard')


def coursefile_approve(request,pk):
    if request.user.is_superuser:
        coursefile = Coursefiles.get_object_or_404(pk=pk)
        coursefile.approve()
        messages.info(request,'Successfully approved')
        return redirect('accounts:dashboard')
    else:
        return redirect('accounts:dashboard')

class Materials(generic.ListView):
    model = Material
    ordering = ['title']
    template_name = 'material_list.html'

    def get_queryset(self):
        return Material.objects.filter(approved=True)

@user_passes_test(lambda x: x.is_superuser)
def adminmaterials(request):
    materials = Material.objects.all()
    past_questions = Coursefiles.objects.all()
    return render(request,"admin_materials.html",{'materials':materials})


@user_passes_test(lambda x: x.is_superuser)
def adminpqs(request):
    past_questions = Coursefiles.objects.all()
    return render(request,"admin_pqs.html",{'pqs':past_questions})    

def adverts(request):
    phones = Products.objects.filter(category="Phones and Accessories")[1:4]
    jumbos = Products.objects.filter(jumbo=True).all()
    return render(request,'adverts.html',{'phones':phones,'jumbos':jumbos})


# clothes view
class ClothesView(generic.ListView):
    model = Products
    template_name="clothes.html"
    def get_queryset(self,*args,**kwargs):
        return Products.objects.filter(category = "Clothing").all()
        super().get_queryset(self,*args,**kwargs)