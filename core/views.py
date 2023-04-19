from django.shortcuts import render, redirect
from .models import Sales
from .forms import SalesForm


# Create your views here.
def index(request):
    sales = Sales.objects.all()
    return render(request, "index.html", {"sales": sales})


def add_sale(request):
    if request.method == "POST":
        form = SalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sales:index")
    else:
        form = SalesForm()
    return render(request, "add_sale.html", {"form": form})


def edit_sale(request, pk):
    sale = Sales.objects.get(pk=pk)
    form_data = {
        "product_name": sale.product.name,
        "product_type": sale.product.type,
        "product_size": sale.product.size,
        "product_price": sale.product.price,
        "product_stock_qty": sale.product.stock_quantity,
    }
    if request.method == "POST":
        form = SalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sales:index")
    else:
        form = SalesForm(data=form_data)
    return render(request, "edit_sale.html", {"form": form})


def delete_sale(request, pk):
    sale = Sales.objects.get(pk=pk)
    sale.delete()
    return redirect("sales:index")
