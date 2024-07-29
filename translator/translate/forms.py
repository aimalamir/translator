from django import forms

class TranslationForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Text to Translate')
    source_language = forms.CharField(max_length=10, label='Source Language')
    target_language = forms.CharField(max_length=10, label='Target Language')
