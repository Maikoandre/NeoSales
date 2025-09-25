from django import forms
from .models import Customer, Product, Order

class CustomerForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
        required=False,
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"}),
        required=False,
    )

    class Meta:
        model = Customer
        fields = [
            "name",
            "email",
            "phone_number",
            "home_number",
            "neighborhood",
            "city",
            "state",
            "password",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone"}),
            "home_number": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Number"}),
            "neighborhood": forms.TextInput(attrs={"class": "form-control", "placeholder": "Neighborhood"}),
            "city": forms.TextInput(attrs={"class": "form-control", "placeholder": "City"}),
            "state": forms.TextInput(attrs={"class": "form-control", "placeholder": "State"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password or confirm_password:
            if password != confirm_password:
                self.add_error("confirm_password", "Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        customer = super().save(commit=False)

        password = self.cleaned_data.get("password")
        if password:
            customer.set_password(password)

        if commit:
            customer.save()
        return customer


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "price", "stock_quantity", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Product Name"}),
            "category": forms.TextInput(attrs={"class": "form-control", "placeholder": "Category"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Price"}),
            "stock_quantity": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Stock Quantity"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Description", "rows": 3}),
        }

    def save(self, commit=True):
        product = super().save(commit=False)
        if commit:
            product.save()
        return product
    
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['amount', 'customer_id', 'product_id', 'status', 'notes']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
            'customer_id': forms.Select(attrs={'class': 'form-control'}),
            'product_id': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Notes', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_id'].queryset = Customer.objects.all()
        self.fields['product_id'].queryset = Product.objects.all()

    def save(self, commit=True):
        order = super().save(commit=False)
        if commit:
            order.save()
        return order