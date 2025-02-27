from django.urls import path
from .views import InvoiceView, invoice_pdf

urlpatterns = [
    path('invoice/', InvoiceView.as_view(), name='invoice'),
    path('invoice/download/', invoice_pdf, name='invoice_download')
]
