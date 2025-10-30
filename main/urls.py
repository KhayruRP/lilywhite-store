from django.urls import path
from main.views import show_main, create_items, show_items, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_items, delete_items, add_item_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('', show_main, name='show_main'),
    path('create-items/', create_items, name='create_items'),
    path('items/<str:id>/', show_items, name='show_items'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:items_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:items_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('items/<uuid:id>/edit', edit_items, name='edit_items'),
    path('items/<uuid:id>/delete', delete_items, name='delete_items'),
    path('create-item-ajax', add_item_ajax, name='add_item_ajax'),
]
