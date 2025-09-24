from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import CustomUser
from shop.models import Item, ItemVariants, Category
from django.utils.dateparse import parse_date
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from forum.models import Author
import time

def index_page(request, *args, **kwargs):
    
    
    return render(request, "index.html")

def selectUser_page(request, *args, **kwargs):
    
    
    return render(request, "usertype.html")

def login_page(request, *args, **kwargs):
    
    
    return render(request, "login.html")

def farmerRegistration(request, *args, **kwargs):
    
    
    return render(request, "registration.html")

def userRegistration(request, *args, **kwargs):
    
    
    return render(request, "userregister.html")

def createUser(request, *args, **kwargs):
    
    if request.method == "POST":
        name = request.POST.get("fname")
        usertype = request.POST.get("usertype")
        dob = request.POST.get("dob")
        dob = parse_date(dob)
        mobile = request.POST.get("mobile")
        gender = request.POST.get("gender")
        nationality = request.POST.get("nationality")
        soilType = request.POST.get("soiltype")
        businesstype = request.POST.get("businesstype")
        primarycrops = request.POST.get("pcrops")
        primarypurpose = request.POST.get("primarypurpose")
        farmownership = request.POST.get("farmownership")
        language = request.POST.get("language")
        village = request.POST.get("village")
        state = request.POST.get("state")
        pin = request.POST.get("pin")
        uname = request.POST.get("uname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        
        user = CustomUser.objects.create(usertype=usertype, name=name, dob=dob, mobile=mobile, gender=gender, nationality=nationality, soilType=soilType, primaryCrops=primarycrops, 
                                   ownership=farmownership, businessType=businesstype, primaryPurpose=primarypurpose, language=language, town=village, state=state, pincode=pin, uname=uname ,email=email)
        user.set_password( raw_password=password)
        user.save()
        Author.objects.create(user=user)
        return redirect("/")
    else:
        return render(request, "usertype.html")
    
def login_validation(request, *args, **kwargs):
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password) 
        
        if user :
            login(request, user)
            return redirect("/")
        else :
            messages.error(request, 'Invalid Credentials')
            return redirect('/login')
        
    else:
        
        return redirect("login.html")
        

def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return HttpResponse(status=404)


@login_required
def dashboard(request):
    userType = request.user.usertype.lower()
    if userType == "farmer":
        return render(request, f"farmer/dashboard.html")
    return render(request, f"dashboard.html")


@login_required
def addProduct(request):
    context = {}
    context["categories"] = list(Category.objects.all())
    return render(request, "farmer/addProduct.html", context=context)


@login_required
def editProduct(request, id):
    context = {}
    context["product"] = Item.objects.get(pk=id)
    context["categories"] = list(Category.objects.all())
    return render(request, "farmer/editProduct.html", context=context)


@login_required
def viewProducts(request):
    context = {}
    context["products"] = list(Item.objects.filter(created_by=request.user))
    return render(request, "farmer/products.html", context=context)


@login_required
def addProductAPI(request):
    if request.method == "POST":
        title = request.POST["title"]
        price = float(request.POST["price"])
        discount_price = float(request.POST["discount-price"])
        category = int(request.POST["category"])
        label = request.POST["label"]
        desc_short = request.POST["desc-short"]
        desc_long = request.POST["desc-long"]
        stock_no = request.POST["quantity"]
        slug = slugify(f"{request.user.id}-{title}-{label}-{desc_short}-{str(time.time())}")[:49]
        item = Item(title=title, price=price, label=label, description_long=desc_long, slug=slug,
        discount_price=discount_price, category_id=category, description_short=desc_short, stock_no=stock_no)
        item.created_by = request.user
        try: 
            item.save()
        except Exception:
            return JsonResponse({"status": "-ERR"})
        additional_fields = ["image", "image2", "image3",
        "variant-1", "variant-2", "variant-3", "variant-4"]
        for field in additional_fields:
            if (field in request.POST or field in request.FILES):
                if field.startswith("image"):
                    setattr(item, field, request.FILES[field])
                else:
                    variant = ItemVariants.objects.create(quantity=request.POST[field])
                    item.variants.add(variant)
        item.save()
        return JsonResponse({"status": "+OK", "msg": "Product Created Successfully!!", "productId": item.id})


@login_required
def editProductAPI(request, id):
    if request.method == "POST":
        try:
            item = Item.objects.get(id=id)
        except Exception:
            return JsonResponse({"status": "-ERR"})
        item.title = request.POST["title"]
        item.price = float(request.POST["price"])
        item.discount_price = float(request.POST["discount-price"])
        item.category_id = int(request.POST["category"])
        item.label = request.POST["label"]
        item.description_short = request.POST["desc-short"]
        item.description_long = request.POST["desc-long"]
        item.stock_no = request.POST["quantity"]
        item.slug = slugify(f"{request.user.id}-{item.title}-{item.label}-{item.description_short}-{str(time.time())}")[:49]
        item.created_by = request.user
        try: 
            item.save()
        except Exception:
            return JsonResponse({"status": "-ERR"})
        additional_fields = ["image", "image2", "image3", "variant"]
        for field in additional_fields:
            if (field in request.POST or field in request.FILES):
                if field.startswith("image"):
                    setattr(item, field, request.FILES[field])
            if field == "variant":
                variants = [field for field in request.POST if field.startswith("variant")]
                for variantField in variants:
                    variantId = int(variantField.split("-")[1])
                    variant = ItemVariants.objects.get(id=variantId)
                    variant.quantity=request.POST[variantField]
                    variant.save()
        return JsonResponse({"status": "+OK", "msg": "Product Modified Successfully!!", "productId": item.id})


@login_required
def deleteProductAPI(request, id):
    if request.method == "POST":
        try:
            item = Item.objects.get(id=id)
        except Exception:
            return JsonResponse({"status": "-ERR"})
        item.delete()
        return JsonResponse({"status": "+OK", "msg": "Product Deleted Successfully!!"})
    