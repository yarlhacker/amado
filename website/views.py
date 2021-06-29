from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage
from django.shortcuts import render , get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from service import models as models_service
from django.conf import settings 
from . import models
from website.cart import Cart 
import json
from django.http import JsonResponse


def is_email(email):
    try:
        validate_email(email)
        return True
    except:
        return False


def index(request):
    is_index =True
    category = request.GET.get('category')
    if not category :
        articles = models_service.Article.objects.filter(status=True)
    else:
        articles = models_service.Article.objects.filter(categorie__nom= category)

    return render(request, 'index.html',locals())

def cart_detail(request):
    is_cart =True   
    cart =  Cart(request)
    pub_key = settings.STRIPE_API_KEY_PUBLIC
    productsstring = ''

    for item in cart:
        product = item['product']
        url = '/%s/%s/' % (product.categorie.id, product.id)
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s','photo': '%s'}," % (product.id, product.nom, product.prix, item['quantity'], item['total_price'],product.image_principal.url)

        productsstring = productsstring + b
    
    
    return render(request, 'cart.html',locals() ,)

def checkout(request):
    is_checkout =True
    return render(request, 'checkout.html',locals())


def shop(request):
    is_shop =True
    category = request.GET.get('category')
    if not category:
        articles = models_service.Article.objects.filter(status=True)
    else:
        cat = get_object_or_404(models_service.Categorie, id=category)
        articles = cat.categorieArticle.all()
        cat_id = cat.id

    categories = models_service.Categorie.objects.filter(status=True)
    paginator = Paginator(articles,4)
    page = request.GET.get('page')
    try:
        articles_albums = paginator.page(page)
    except PageNotAnInteger : 
        articles_albums = paginator.page(1)
    except EmptyPage :
        articles_albums = paginator.page(paginator.num_pages)

    return render(request, 'shop.html', locals())

def product_detail(request,id):

    article = get_object_or_404(models_service.Article , id=id)
    images = models_service.Image.objects.filter(status=True)
    return render(request, 'product-details.html',locals())


def search(request):
    query = request.GET.get('search')
    if not query:
        print('1', query)
        articles = models_service.Article.objects.all()
    else:
        print('2', query)
        articles = models_service.Article.objects.filter(nom__icontains=query)
        
    return render(request ,'index.html', locals())  

@csrf_exempt
def newsletter(request):
    msg, success = '', False

    if request.method == 'POST':
        email = json.loads(request.POST.get('email'))
        if email.isspace():
            msg = 'veuillez remplir ce champ avant de le soumettre !!!'
        elif is_email(email):
            msg = 'Email invalide'
        else:
            news, created = models.Newsletter.objects.get_or_create(email=email)
            news.save()
            if created:
                msg = 'email enregistrer avec success'
            else:
                msg = 'Vous etes deja inscrit'
            success = True
    datas = {
        'success': success,
        'msg': msg
    }
    return JsonResponse(datas, safe=False)
# Create your views here.