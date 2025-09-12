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
