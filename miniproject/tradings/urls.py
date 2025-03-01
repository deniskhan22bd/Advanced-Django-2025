from django.urls import path
from .views import (
    BuyProductView, BuyerBucketView, SellerNotificationsView,
    ApproveTransactionView, DenyTransactionView
)

urlpatterns = [
    path('buy/<int:product_id>/', BuyProductView.as_view(), name='buy_product'),
    path('bucket/', BuyerBucketView.as_view(), name='buyer_bucket'),
    path('seller/notifications/', SellerNotificationsView.as_view(), name='seller_notifications'),
    path('seller/approve/<int:transaction_id>/', ApproveTransactionView.as_view(), name='approve_transaction'),
    path('seller/deny/<int:transaction_id>/', DenyTransactionView.as_view(), name='deny_transaction'),
]
