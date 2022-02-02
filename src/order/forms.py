from django import forms


class CheckoutForm(forms.Form):
    address = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Main address ...', 'rows': 3}))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City ...'}))
    zip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    use_default = forms.BooleanField(required=False)
    set_default = forms.BooleanField(required=False)


