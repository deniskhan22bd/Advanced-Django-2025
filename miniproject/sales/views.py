from django.shortcuts import render
from tradings.models import Transaction
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required

class InvoiceView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Filter transactions to only include those for the current user
        transactions = Transaction.objects.filter(buyer=request.user)
        total_price = sum(transaction.product.price for transaction in transactions)
        context = {
            "transactions": transactions,
            "total_price": total_price,
        }
        return render(request, "sales/invoice.html", context)

class InvoicePDFView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Filter transactions to only include those for the current user
        transactions = Transaction.objects.filter(buyer=request.user)
        total_price = sum(transaction.product.price for transaction in transactions)
        
        # Render the invoice HTML template with context data
        template = get_template("sales/invoice.html")
        html = template.render({
            "transactions": transactions,
            "total_price": total_price,
        })
        
        # Create an HttpResponse with PDF content type
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
        
        # Generate the PDF from the rendered HTML using xhtml2pdf (pisa)
        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse("Error generating PDF", status=500)
        
        return response
