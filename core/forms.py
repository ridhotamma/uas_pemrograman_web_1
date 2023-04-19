from django import forms
from .models import Product, Sales, Type, Size
from .utils import generate_code


class SalesForm(forms.ModelForm):
    product_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"placeholder": "Sepatu Nike Air Jordan", "class": "form-control"}
        ),
    )
    product_type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    product_size = forms.ModelChoiceField(
        queryset=Size.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    product_price = forms.FloatField(
        widget=forms.NumberInput(
            attrs={"placeholder": "BO00000123", "class": "form-control"}
        ),
    )
    product_stock_qty = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"placeholder": "10000000", "class": "form-control"}
        ),
    )

    class Meta:
        model = Sales
        fields = [
            "product_name",
            "product_type",
            "product_size",
            "product_price",
            "product_stock_qty",
        ]

    def save(self, commit=True):
        # Get the form data
        product_name = self.cleaned_data["product_name"]
        product_type = self.cleaned_data["product_type"]
        product_size = self.cleaned_data["product_size"]
        product_price = self.cleaned_data["product_price"]
        product_stock_qty = self.cleaned_data["product_stock_qty"]

        product = Product.objects.create(
            code=generate_code(),
            name=product_name,
            type=product_type,
            size=product_size,
            price=product_price,
            stock_quantity=product_stock_qty,
        )
        sale = Sales.objects.create(product=product, product_quantity=product_stock_qty)

        return sale if commit else None
