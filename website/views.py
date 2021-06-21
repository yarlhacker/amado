from django.shortcuts import render , get_object_or_404
from service import models as models_service


def index(request):
    articles = models_service.Article.objects.filter(status=True)
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')


def shop(request):
    cotegory = request.GET.get('cotegory')
    if cotegory :
        articles = models_service.Article.objects.filter(categories__nom = cotegory)

    categories = models_service.Categorie.objects.filter(status=True)
    return render(request, 'shop.html', locals())

def product_detail(request,id):

    article = get_object_or_404(models_service.Article , id=id)
    images = models_service.Image.objects.filter(status=True)
    return render(request, 'product-details.html',locals())
# Create your views here.
