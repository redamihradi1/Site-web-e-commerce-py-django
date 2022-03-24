from django.conf.urls import url
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Category, Product
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import  redirect,render
from django.contrib import  messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


from  .forms import  *
from  .models import  *

def registerPage(request):
   if request.user.is_authenticated:
       return redirect('/')
   else:
       form = CreateUserForm()
       if request.method == 'POST':
           form =CreateUserForm(request.POST)
           if form.is_valid():
               form.save()
               user = form.cleaned_data.get('username')
               messages.success(request,'Compte crée pour '+user)

               return redirect('/')
       context ={'form':form}
       return render(request,'store/register.html',context)
        

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, password=password, username=username)

            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.info(request,'Nom de compte ou mot de passse inccorect')
        context = {}
        return render(request,'store/login.html',context)

    


def logoutUser(request):
    logout(request)
    return redirect('/')


def product_all(request):
    products = Product.products.all()
    return render(request, 'store/home.html', {'products': products})



def AdminStore(request):
    return render(request,'store/admin/mainadmin.html',{}) 


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})

@login_required(login_url='/login/')
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})


def UserPayment(request):
    return render(request, "payment.html",{})

#################################################################################################################
                                               # Coté Admin #
#################################################################################################################
@login_required(login_url='/login/')
def AdminStore(request):
    return render(request,'store/admin/mainadmin.html',{}) 

@login_required(login_url='/login/')
def CategoryListView(request):
    categories=Category.objects.all()
    return render(request,'store/admin/category_list.html',{'categories':categories})

class CategoryView(View):
    def get(self,request):
        form=CategoryForm()#pour creeer le formulaire vide
        return render(request, 'store/admin/category_form.html',{'form':form})
    def post(self,request):
        form=CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('store:categoryList')

class CategoryDeleteView(View):
    def get(self,request,idp):
        return render(request,"store/admin/categorydelete_from.html",{})
    def post(self,request,idp):
        categorie=Category.objects.get(id=idp)
        categorie.delete()
        return  redirect("store:categoryList")

class CategoryUpdateView(View):
    def get(self,request,idp):
        categorie=Category.objects.get(id=idp)
        form=CategoryForm(instance=categorie) #créer un formulaire vide
        return render(request,"store/admin/category_form.html",{'form':form})
    def post(self,request,idp):
        categorie=Category.objects.get(id=idp)
        form=CategoryForm(request.POST,request.FILES,instance=categorie) # récupérer les données saisies dans le formulaire
        if form.is_valid(): # valider les données saisies
            form.save()   # sauvegarder les données dans la base de données
        return  redirect("store:categoryList")

@login_required(login_url='/login/')
def ProductListView(request):
    products=Product.objects.all()
    return render(request,'store/admin/product_list.html',{'products':products})

class ProductView(View):
    def get(self,request):
        form=ProductForm()#pour creeer le formulaire vide
        return render(request, 'store/admin/product_form.html',{'form':form})
    def post(self,request):
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return  redirect("store:productList")

class ProductUpdateView(View):
    def get(self,request,idp):
        product=Product.objects.get(id=idp)
        form=ProductForm(instance=product) #créer un formulaire vide
        return render(request,"store/admin/product_form.html",{'form':form})
    def post(self,request,idp):
        product=Product.objects.get(id=idp)
        form=ProductForm(request.POST,request.FILES,instance=product) # récupérer les données saisies dans le formulaire
        if form.is_valid(): # valider les données saisies
            form.save()   # sauvegarder les données dans la base de données
        return  redirect("store:productList")

class ProductDeleteView(View):
    def get(self,request,idp):
        return render(request,"store/admin/productdelete_from.html",{})
    def post(self,request,idp):
        product=Product.objects.get(id=idp)
        product.delete()
        return  redirect("store:productList")

class ProductDetailsView(View):
    def get(self,request,idp):
        product=Product.objects.get(id=idp)
        return render(request,"store/admin/products_details.html",{"product":product})


        