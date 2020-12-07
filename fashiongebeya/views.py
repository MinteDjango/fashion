from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from .models import Item, MyCart, Wishlist

# Create your views here.
def home(request):
    items = Item.objects.all()
    context = {
        "items":items,
        }
    return render(request, 'fashiongebeya/gebeyahome.html', context)

def search(request):
    if request.method == "GET":
        search = request.GET.get("search")
        if search:
            items = Item.objects.filter(Q(caption__icontains=search) | Q(brand__icontains=search) | Q(what__icontains=search)).distinct()
            context = {
            "items":items
        }
            if items:
                return render(request, 'fashiongebeya/gebeyasearch.html', context)
            else:
                messages.error(request, "No result found for your search")
    return render(request, 'fashiongebeya/gebeyasearch.html')

def profile(request):
    return render(request, 'fashiongebeya/gebeyaprofile.html')

def cart(request):
    items = MyCart.objects.filter(user=request.user)
    context = {"items":items}
    return render(request, 'fashiongebeya/gebeyacart.html', context)

def wishlist(request):
    items = Wishlist.objects.filter(user=request.user)
    context = {"items":items}
    return render(request, 'fashiongebeya/gebeyawhishlist.html', context)

def item(request, what):
   items =  Item.objects.filter(what=what)
   if items is None:
       items = Item.objects.filter(what="other")
   context = { "items":items}
   return render(request, 'fashiongebeya/gebeyawhat.html', context)

def addcart(request):
    if request.method == "POST":
        id = request.POST.get("id")
        MyCart.objects.create(user=request.user, item_id=id)
        return JsonResponse({"added":True})

def createwishlist(request):
    if request.method == "POST":
        id = request.POST.get("id")
        Wishlist.objects.create(user=request.user, item_id=id)
        return JsonResponse({"added":True})
