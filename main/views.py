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
from django.views.decorators.http import require_POST, require_http_methods
from django.utils.html import strip_tags
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

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

@login_required(login_url='/login')
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
   
def show_json_by_id(request, items_id):
    try:
        item = Items.objects.select_related('user').get(pk=items_id)
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
        messages.success(request, f'Welcome back, {user.username}!')
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
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
        "item": {
            "id": str(new_item.id),
            "title": new_item.title,
            "price": new_item.price,
            "content": new_item.content,
            "category": new_item.category,
            "thumbnail": new_item.thumbnail,
            "store_views": new_item.store_views,
            "created_at": new_item.created_at.isoformat() if new_item.created_at else None,
            "is_featured": new_item.is_featured,
            "user_id": new_item.user.id if new_item.user else None,
            "user_username": new_item.user.username if new_item.user else None,
        }
    }, status=201)

@csrf_exempt
@require_http_methods(["POST"])
def edit_item_ajax(request, id):
    """
    Edit item via AJAX. Uses ItemsForms for validation.
    """
    item = get_object_or_404(Items, pk=id)

    # optional: hanya owner yang boleh edit
    if item.user and request.user != item.user:
        return JsonResponse({"error": "Unauthorized"}, status=403)

    # gunakan ModelForm supaya validasi sama seperti edit_items
    form = ItemsForms(request.POST or None, instance=item)
    if form.is_valid():
        updated = form.save(commit=False)
        # jaga user tetap sama
        updated.user = item.user
        updated.save()

        # kembalikan data yang diperlukan frontend
        return JsonResponse({
            "status": "updated",
            "item": {
                "id": str(updated.id),
                "title": updated.title,
                "price": updated.price,
                "content": updated.content,
                "category": updated.category,
                "thumbnail": updated.thumbnail,
                "store_views": updated.store_views,
                "is_featured": updated.is_featured,
                "user_id": updated.user.id if updated.user else None,
            }
        }, status=200)
    else:
        # return errors (simple)
        return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    

@csrf_exempt
@require_http_methods(["POST"])
def delete_item_ajax(request, id):
    """
    Hapus item via AJAX dengan konfirmasi popup.
    """
    from django.shortcuts import get_object_or_404
    item = get_object_or_404(Items, pk=id)

    # pastikan hanya pemilik item yang bisa hapus
    if request.user != item.user:
        return JsonResponse({"error": "Unauthorized"}, status=403)

    item.delete()
    return JsonResponse({"status": "deleted", "id": str(id)}, status=200)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    

@csrf_exempt
def create_items_flutter(request):
    if request.method == 'POST':
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
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)