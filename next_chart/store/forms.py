from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"})
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

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        customer = super().save(commit=False)
        customer.set_password(self.cleaned_data["password"])
        if commit:
            customer.save()
        return customer

class ProductForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Product Name"})
    )
    category = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Category"})
    )
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Price"})
    )
    stock_quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Stock Quantity"})
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Description", "rows": 3})
    )

    def save(self):
        from .models import Product  # Importing here to avoid circular imports
        data = self.cleaned_data
        product = Product(
            name=data['name'],
            category=data['category'],
            price=data['price'],
            stock_quantity=data['stock_quantity'],
            description=data.get('description', '')
        )
        product.save()
        return product