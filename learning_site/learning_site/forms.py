from django import forms


def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty!')

class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Verify email')
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label='Leave empty',
        validators=[must_be_empty]
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        verify = cleaned_data['verify_email']
        if email != verify:
            raise forms.ValidationError('Email must match')
