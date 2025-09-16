from django.forms import ModelForm
from main.models import Items

class ItemsForms(ModelForm):
    class Meta:
        model = Items
        fields = ["title", "price", "content", "category", "thumbnail", "is_featured"]