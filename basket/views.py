from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Item
from django.shortcuts import redirect
from django.contrib.auth.models import User
import requests
from bs4 import BeautifulSoup


def item_list(request):
    items = Item.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'basket/item_list.html', {'items':items})

def add_item(request):
    if request.method == "POST":
        item_Url = request.POST['link']
        if 'gmarket' in item_Url:
            thumbnaillink = BeautifulSoup(str(BeautifulSoup(
            requests.get(item_Url).text, 
            'html.parser').select("#og_image")[0]).split('\n')[0], 
            'html.parser').findAll('meta')[0].get('content')
        if '11st' in item_Url:
            thumbnaillink = BeautifulSoup(str(BeautifulSoup(
            requests.get(item_Url).text, 
            'html.parser').select("head > meta:nth-child(27)")[0]).split('\n')[0], 
            'html.parser').findAll('meta')[0].get('content')
        if 'auction' in item_Url:
            thumbnaillink = BeautifulSoup(str(BeautifulSoup(
            requests.get(item_Url).text, 
            'html.parser').select("head > meta:nth-child()")[0]).split('\n')[0], 
            'html.parser').findAll('meta')[0].get('content')
        if 'coupang' in item_Url:
            thumbnaillink = BeautifulSoup(str(BeautifulSoup(
            requests.get(item_Url).text, 
            'html.parser').select("head > meta:nth-child(22)")[0]).split('\n')[0], 
            'html.parser').findAll('meta')[0].get('content')
            thumbnaillink = 'https:'+thumbnaillink
        item = Item()
        item.name = request.POST['name']
        item.link = request.POST['link']
        item.thumbnail = thumbnaillink
        item.created_date = timezone.now()
        item.author = request.user
        item.save()
        return redirect('item_list')
    else:
        item = Item()
    return render(request, 'basket/add_item.html', {'item':item})

def error(request):
    return render(request, 'basket/error.html', {'error':'You do not have access to this cart.'})