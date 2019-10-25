from django.shortcuts import render, get_object_or_404
from .models import Basket
from .forms import BasketForm
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.models import User

def basket_list(request):
    baskets = Basket.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'basket/basket_list.html', {'baskets':baskets})

def make_basket(request):
    if request.method == "POST":
        basket = Basket()
        basket.title = request.POST['title']
        basket.item.name = request.POST['name']
        basket.item.link = request.POST['link']
        basket.save()
        return redirect('basket_list')
        '''form = BasketForm(request.POST)
        if form.is_valid():
            basket = form.save(commit=False)
            basket.author = request.user
            basket.created_date = timezone.now()
            basket.save()
            return redirect('basket_list')'''
    else:
        basket = Basket()
    return render(request, 'basket/add_basket.html', {'basket':basket})

def basket_detail(request, pk):
    author = Basket.objects.get(pk=pk)
    if author.author == User.objects.get(username = request.user.get_username()):
        basket = get_object_or_404(Basket, pk=pk)
    else:
        return redirect('basket_error')
    return render(request, 'basket/basket_detail.html', {'basket':basket})

def basket_error(request):
    return render(request, 'basket/error.html', {'error': 'You do not have access to this cart.'})