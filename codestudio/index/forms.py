from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ваше имя',
            'class': 'text-box',
            'id': 'name',
            'name': 'name'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Электронная почта',
            'class': 'text-box',
            'id': 'email',
            'name': 'email'
        })
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Сообщение',
            'class': 'text-box',
            'id': 'message',
            'name': 'message'
        })
    )
