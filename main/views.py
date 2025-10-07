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
from django.http import HttpResponseRedirect, JsonResponse
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
    items_list = Items.objects.all()
    data = [
        {
            'id': str(items.id),
            'title': items.title,
            'content': items.content,
            'category': items.category,
            'thumbnail': items.thumbnail,
            'items_views': items.items_views,
            'created_at': items.created_at.isoformat() if items.created_at else None,
            'is_featured': items.is_featured,
            'user_id': items.user_id,
        }
        for items in items_list
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
        items = Items.objects.select_related('user').get(pk=items_id)
        data = {
            'id': str(items.id),
            'title': items.title,
            'content': items.content,
            'category': items.category,
            'thumbnail': items.thumbnail,
            'items_views': items.items_views,
            'created_at': items.created_at.isoformat() if items.created_at else None,
            'is_featured': items.is_featured,
            'user_id': items.user_id,
            'user_username': items.user.username if items.user_id else None,
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
def add_items_entry_ajax(request):
    title = strip_tags(request.POST.get("title"))
    content = strip_tags(request.POST.get("content"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_items = Items(
        title=title, 
        content=content,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_items.save()

    return HttpResponse(b"CREATED", status=201)