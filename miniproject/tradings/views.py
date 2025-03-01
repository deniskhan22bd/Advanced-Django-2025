from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from products.models import Product
from .models import Transaction
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponseRedirect

class BuyProductView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id, format=None):
        product = get_object_or_404(Product, id=product_id)
        if product.stock <= 0:
            return Response(
                {"detail": "Product out of stock."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        Transaction.objects.create(
            product=product,
            buyer=request.user,
            status='pending'
        )
        
        product.stock -= 1
        product.save()
        
        if product.stock == 0:
            product.delete()
        
        # If the request accepts HTML (e.g., a browser request), redirect.
        return HttpResponseRedirect(redirect_to="/products/")



# API endpoint to list transactions for a buyer
class BuyerBucketView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tradings/buyer_bucket.html'
    
    def get(self, request, *args, **kwargs):
        transactions = Transaction.objects.filter(buyer=request.user)
        return Response({'transactions': transactions})

class SellerNotificationsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tradings/seller_notifications.html'

    def get(self, request, *args, **kwargs):
        transactions = Transaction.objects.filter(product__seller=self.request.user, status='pending')
        return Response({'transactions': transactions})


# API endpoint for a seller to approve a transaction
class ApproveTransactionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, transaction_id, format=None):
        transaction = get_object_or_404(Transaction, id=transaction_id)
        # Ensure that only the seller can approve the transaction
        if transaction.product.seller != request.user:
            return Response({"detail": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)
        
        transaction.status = 'accepted'
        transaction.save()
        return HttpResponseRedirect(redirect_to="/seller/notifications/")



# API endpoint for a seller to deny a transaction
class DenyTransactionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, transaction_id, format=None):
        transaction = get_object_or_404(Transaction, id=transaction_id)
        if transaction.product.seller != request.user:
            return Response({"detail": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)
        
        transaction.status = 'rejected'
        transaction.save()
        return HttpResponseRedirect(redirect_to="/seller/notifications/")
