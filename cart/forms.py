from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
class CartAddProductForm(forms.Form):
    count_product = forms.TypedChoiceField(label="Кількість",
                                           choices=PRODUCT_QUANTITY_CHOICES,
                                           coerce=int)
    update_count_product = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
