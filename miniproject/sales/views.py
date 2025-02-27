from django.shortcuts import render
from tradings.models import Transaction
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

class InvoiceView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # Retrieve transactions (filter as needed)
        transactions = Transaction.objects.all()
        # Calculate total price (assuming each transaction is for one product)
        total_price = sum(transaction.product.price for transaction in transactions)
        context = {
            "transactions": transactions,
            "total_price": total_price,
        }
        return render(request, "sales/invoice.html", context)
    
def invoice_pdf(request):
    template = get_template("sales/invoice.html")
    html = template.render({
        "transactions": Transaction.objects.all(),
        "total_price": sum(t.product.price for t in Transaction.objects.all())
    })
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response


