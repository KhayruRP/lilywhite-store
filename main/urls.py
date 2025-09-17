from django.urls import path
from main.views import show_main, create_items, show_items, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
]
