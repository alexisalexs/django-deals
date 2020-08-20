from django.forms import ModelForm
from ..models import Item
import tweepy


class SaleItem(ModelForm):
    class Meta:
        model = Item
        fields = ['item_name',]