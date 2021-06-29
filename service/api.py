from django.http import JsonResponse
from django.shortcuts  import get_object_or_404,redirect
import json
import stripe

from django.conf import settings
from website.cart import Cart

from service.models import Article

from checkout.models import Checkout

from checkout.utils import checkout


def create_checkout_session(request):
    # data = json.loads(request.body)

    # Coupon 

    # coupon_code = data['coupon_code']
    # coupon_value = 0

    # if coupon_code != '':
    #     coupon = Coupon.objects.get(code=coupon_code)

    #     if coupon.can_use():
    #         coupon_value = coupon.value
    #         coupon.use()

    #

    cart = Cart(request)

    stripe.api_key = settings.STRIPE_API_KEY_PRIVE 

    items = []
    
    for item in cart:
        product = item['product']

        obj = {
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.title
                },
                'unit_amount': int(product.price * 100)
            },
            'quantity': item['quantity']
        }

        items.append(obj)

        
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=items,
            mode='payment',
            success_url='{% url "checkout"%}',
            cancel_url='{% url "checkout"%}'
        )

    #
    # Create order

    # orderid = checkout(request, data['first_name'], data['last_name'], data['email'], data['address'], data['zipcode'], data['place'], data['phone'])

    # total_price = 0.00

    # for item in cart:
    #     product = item['product']
    #     total_price = total_price + (float(product.price) * int(item['quantity']))

    # if coupon_value > 0:
    #     total_price = total_price * (coupon_value / 100)
    
    # if gateway == 'razorpay':
    #     order_amount = total_price * 100
    #     order_currency = 'INR'
    #     client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY_PUBLISHABLE, settings.RAZORPAY_API_KEY_HIDDEN))
    #     data = {
    #         'amount': order_amount,
    #         'currency': order_currency
    #     }

    #     payment_intent = client.order.create(data=data)
    
    # PayPal

    # if gateway == 'paypal':
    #     order_id = data['order_id']
    #     environment = SandboxEnvironment(client_id=settings.PAYPAL_API_KEY_PUBLISHABLE, client_secret=settings.PAYPAL_API_KEY_HIDDEN)
    #     client = PayPalHttpClient(environment)

    #     request = OrdersCaptureRequest(order_id)
    #     response = client.execute(request)

    #     order = Order.objects.get(pk=orderid)
    #     order.paid_amount = total_price
    #     order.used_coupon = coupon_code

    #     if response.result.status == 'COMPLETED':
    #         order.paid = True
    #         order.payment_intent = order_id
    #         order.save()

    #         decrement_product_quantity(order)
    #         send_order_confirmation(order)
    #     else:
    #         order.paid = False
    #         order.save()
    # else:
    #     order = Order.objects.get(pk=orderid)
    #     if gateway == 'razorpay':
    #         order.payment_intent = payment_intent['id']
    #     else:
    #         order.payment_intent = payment_intent
    #     order.paid_amount = total_price
    #     order.used_coupon = coupon_code
    #     order.save()
    return JsonResponse(locals())


def api_checkout(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}

    cart = Cart(request)

    nom = data['nom']
    prenom = data['prenom']
    email = data['email']
    pays = data['pays']
    town = data['town']
    phone = data['phone']
    zipcode = data['zipcode']
    company = data['company']
    adresse = data['adresse']
    commentaire = data['commentaire']

    orderid = checkout(request ,nom, prenom, email, pays, town, phone, zipcode, company, adresse, commentaire)

    paid =True 
    if paid == True:
        order = get_object_or_404(Checkout , pk=orderid)
        order.paid = True 
        order.paid_amount =  cart.get_total_cost()
        order.save()

        cart.clear()


    return JsonResponse(jsonresponse)

def api_add_to_cart(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    update = data['update']
    quantity = data['quantity']

    cart = Cart(request)

    product = get_object_or_404(Article, pk=product_id)

    if not update:
        cart.add(product=product, quantity=1, update_quantity=False)
    else:
        cart.add(product=product, quantity=quantity, update_quantity=True)
    
    jsonresponse = {'success': True}
    return JsonResponse(jsonresponse , safe=False)

def api_remove_from_cart(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    product_id = str(data['product_id'])

    cart = Cart(request)
    cart.remove(product_id)

    return JsonResponse(jsonresponse)