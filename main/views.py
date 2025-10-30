from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ItemsForms
from main.models import Items
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    items_type = request.GET.get("filter", "all")  # default 'all'

    if items_type == "all":
        items_list = Items.objects.all()
    else:
        items_list = Items.objects.filter(user=request.user)
    data = {
        'Aplikasi' : 'Lilywhite Store',
        'Name': 'Khayru Rafamanda Prananta',
        'class': 'PBP F',
        'NPM' : '2406495893',
        'items_list' : items_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", data)


def create_items(request):
    form = ItemsForms(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        Items_entry = form.save(commit = False)
        Items_entry.user = request.user
        Items_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_items.html", context)

@login_required(login_url='/login')
def show_items(request, id):
    items = get_object_or_404(Items, pk=id)
    items.increment_views()

    context = {
        'items': items
    }

    return render(request, "items_detail.html", context)
#aaa
def show_xml(request):
     items_list = Items.objects.all()
     xml_data = serializers.serialize("xml", items_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    items = Items.objects.all()  # ganti nama model sesuai
    data = [
        {
            'id': str(item.id),
            'title': item.title,
            'price': item.price,
            'content': item.content,
            'category': item.category,
            'thumbnail': item.thumbnail,
            'store_views': item.store_views,
            'created_at': item.created_at.isoformat() if item.created_at else None,
            'is_featured': item.is_featured,
            'user_id': item.user.id if item.user else None,
            'username': item.user.username if item.user else None,  # optional, biar lebih informatif
        }
        for item in items
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, items_id):
   try:
       items_item = Items.objects.filter(pk=items_id)
       xml_data = serializers.serialize("xml", items_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Items.DoesNotExist:
       return HttpResponse(status=404)
   
def show_json_by_id(request, item_id):
    try:
        item = Items.objects.select_related('user').get(pk=item_id)
        data = {
            'id': str(item.id),
            'title': item.title,
            'price': item.price,
            'content': item.content,
            'category': item.category,
            'thumbnail': item.thumbnail,
            'store_views': item.store_views,
            'created_at': item.created_at.isoformat() if item.created_at else None,
            'is_featured': item.is_featured,
            'user_id': item.user.id if item.user else None,
            'user_username': item.user.username if item.user else None,
        }
        return JsonResponse(data)
    except Items.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_items(request, id):
    items = get_object_or_404(Items, pk=id)
    form = ItemsForms(request.POST or None, instance=items)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_items.html", context)


def delete_items(request, id):
    items = get_object_or_404(Items, pk=id)
    items.delete()
    return HttpResponseRedirect(reverse('main:show_main'))


@csrf_exempt
@require_POST
def add_item_ajax(request):
    """
    AJAX endpoint untuk menambahkan item baru tanpa reload halaman.
    Data dikirim via FormData dari modal.
    """
    title = strip_tags(request.POST.get("title", ""))
    price_raw = request.POST.get("price", "")
    content = strip_tags(request.POST.get("content", ""))
    category = request.POST.get("category", "new")
    thumbnail = request.POST.get("thumbnail", "").strip() or None
    is_featured = request.POST.get("is_featured") in ["on", "true", "1"]
    user = request.user if request.user.is_authenticated else None

    # Validasi harga
    try:
        price = int(price_raw) if price_raw else 0
    except ValueError:
        return JsonResponse({"error": "Invalid price value"}, status=400)

    # Buat instance Items
    new_item = Items(
        title=title,
        price=price,
        content=content,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_item.save()

    # Respon JSON agar JS tahu item berhasil dibuat
    return JsonResponse({
        "status": "created",
        "id": str(new_item.id),
        "title": new_item.title,
        "price": new_item.price,
    }, status=201)