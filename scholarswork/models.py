from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from accounts.models import Student,Seller
from django.utils import timezone



class School(models.Model):
    name = models.CharField(max_length=120,unique=True)
    state = models.CharField(max_length=100)
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('schools')

    def __str__(self):
        return self.name


class Course(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name='courses')
    code = models.CharField(max_length=200)
    full_name = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('course_list',kwargs={'pk':self.school.pk})

    def __str__(self):
        return self.code



class Coursefiles(models.Model):
    course = models.ForeignKey(Course,related_name='files',on_delete=models.CASCADE,blank=True,null=True)
    file = models.FileField(name=course.name,upload_to='pqs')
    school = models.ForeignKey(School,related_name='coursefiles',blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=20,null=True,blank=True)
    year = models.CharField(max_length=10)
    approved = models.BooleanField(default=False)
    uploader = models.ForeignKey(Student,on_delete=models.SET_NULL,related_name='uploaded_files',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def approve(self):
        self.approved = True
        self.uploader.uploads +=1

    class Meta:
        verbose_name = 'Coursefile'


class Material(models.Model):
    title = models.CharField(max_length=40)
    file = models.FileField(upload_to='materials',unique=True)
    uploader = models.ForeignKey(Student,on_delete=models.SET_NULL,related_name='uploaded_materials',null=True,blank=True)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        

    def approve(self):
        self.approved = True
        self.uploader.uploads+=1
        self.uploader.save()
        self.save()

    def __str__(self):
        return self.title + " uploaded by " + self.uploader.user.username

PRODUCTS_CATEGORIES = (
    ("Phones and Accessories",'PAA'),
    ("Clothing",'WC'),
    ('Computers and Accessories','CAA'),
)

SEX_CHOICES = (
    ('M','Male'),
    ('F','Female'),
    ('U','Unisex')
)



###products 
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    image1 = models.ImageField(upload_to='products',null=True,blank=True)
    image2 = models.ImageField(upload_to='products',null=True,blank=True)
    seller = models.ForeignKey(Seller,null=True,blank=True,related_name='products',on_delete=models.CASCADE)
    category = models.CharField(choices=PRODUCTS_CATEGORIES,max_length=50)
    description = models.CharField(max_length=1000)
    negotiable = models.BooleanField(default=False)
    jumbo = models.BooleanField(default=False)

    ###phones##
    brand = models.CharField(max_length=200,null=True,blank=True)
    ram = models.CharField(max_length=6,null=True,blank=True)
    battery_life = models.CharField(max_length=7,null=True,blank=True)
    internal_storage = models.CharField(max_length=8,null=True,blank=True)
    screen_size = models.CharField(max_length=20,null=True,blank=True)
    sim = models.CharField(max_length=10,null=True,blank=True)
    main_camera = models.CharField(max_length=20,null=True,blank=True)
    operating_system = models.CharField(max_length=10,null=True,blank=True)

    ##clothes
    size = models.CharField(max_length=10)
    sex = models.CharField(choices=SEX_CHOICES,max_length=20)



    class Meta:
        ordering = ['-price']
        verbose_name = 'Product'

    def detail(self):
        return reverse('product_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.name


    
    
    
    











