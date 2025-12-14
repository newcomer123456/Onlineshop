from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateProduct

# Create your views here.
def product_list(request):
    products = Product.objects.all().order_by('-date')
    return render(request, 'shop/product_list.html', {'products':products})

def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/product_details.html', {'product':product})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("shop:products")
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {"form":form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("shop:products")
    else:    
        form = AuthenticationForm()
    return render(request, 'shop/login.html', {"form":form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("shop:products")

@login_required(login_url="/shop/login")
def product_creation(request):
    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            newproduct = form.save(commit=False)
            newproduct.author = request.user
            newproduct.save()
            return redirect("shop:products")

    else:
        form = CreateProduct()
    return render(request, 'shop/creation_product.html', {"form":form})
    