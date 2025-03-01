from django.urls import path
from .views import InvoiceView, InvoicePDFView

urlpatterns = [
    path('invoice/', InvoiceView.as_view(), name='invoice'),
    path('invoice/download/', InvoicePDFView.as_view(), name='invoice_download')
]
