# tradings/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from products.models import Product
from .models import Transaction

def buy_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.stock <= 0:
        return redirect('product_list')
    Transaction.objects.create(product=product, buyer=request.user, status='pending')
    product.stock -= 1
    product.save()
    if product.stock == 0:
        product.delete()
    
    return redirect('buyer_bucket')

class BuyerBucketView(ListView):
    model = Transaction
    template_name = 'tradings/buyer_bucket.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return Transaction.objects.filter(buyer=self.request.user)

# Seller notifications: list pending transactions for products where the seller is the current user
class SellerNotificationsView(ListView):
    model = Transaction
    template_name = 'tradings/seller_notifications.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return Transaction.objects.filter(product__seller=self.request.user, status='pending')


def approve_transaction(request, transaction_id):
    """
    Seller approves a transaction.
    """
    transaction = get_object_or_404(Transaction, id=transaction_id)
    # Ensure only the seller of the product can approve
    if transaction.product.seller != request.user:
        return HttpResponse("Unauthorized", status=403)
    transaction.status = 'accepted'
    transaction.save()
    return redirect('seller_notifications')

def deny_transaction(request, transaction_id):
    """
    Seller denies a transaction.
    """
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if transaction.product.seller != request.user:
        return HttpResponse("Unauthorized", status=403)
    transaction.status = 'rejected'
    transaction.save()
    return redirect('seller_notifications')
