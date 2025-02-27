from django.urls import path
from .views import (
    buy_product, BuyerBucketView, SellerNotificationsView,
    approve_transaction, deny_transaction
)

urlpatterns = [
    path('buy/<int:product_id>/', buy_product, name='buy_product'),
    path('bucket/', BuyerBucketView.as_view(), name='buyer_bucket'),
    path('seller/notifications/', SellerNotificationsView.as_view(), name='seller_notifications'),
    path('seller/approve/<int:transaction_id>/', approve_transaction, name='approve_transaction'),
    path('seller/deny/<int:transaction_id>/', deny_transaction, name='deny_transaction'),
]
