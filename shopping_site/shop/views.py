from django.shortcuts import render, redirect
from .models import Product, Order

# Create your views here.

def product_dispaly(request):
    all_products = Product.objects.all()
    
    context = {'products':all_products}
    return render(request, "shop/index.html", context)

def more_details(request, id):
    product = Product.objects.get(id=id)
    
    # Place order
    if request.method == 'POST':
        order_product = Product.objects.get(id=id)
        order_quantity = request.POST.get('quantity')
        
        Order.objects.create(
            product= order_product,
            quantity= order_quantity, 
        )
    context = {'product': product}
    return render(request, "shop/moreDetails.html", context)

def cancelOrder(request, id):
    order = Order.objects.get(id=id)
    
    order.delete()
        
    
    return redirect('orders')

def aboutPage(request):
    
    
    context = {}
    return render(request, 'shop/about.html', context)

def orders(request):
    orders = Order.objects.all()
    no_of_orders = Order.objects.count()
    
    context = {'orders': orders, 'no_of_orders': no_of_orders}
    return render(request, 'shop/orders.html', context)

