from django import forms


class SentenceForm(forms.Form):
    text = forms.CharField(
        max_length=255,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your sentence here",
                "class": "form-control",
            }
        ),
    )

    