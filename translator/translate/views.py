from django.shortcuts import render
from .forms import TranslationForm
from googletrans import Translator
# Create your views here.


def translate_text(request):
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            source_lang = form.cleaned_data['source_language']
            target_lang = form.cleaned_data['target_language']
            
            translator = Translator()
            translation = translator.translate(text, src=source_lang, dest=target_lang)
            
            return render(request, 'translate/results.html', {'original': text, 'translated': translation.text, 'source': source_lang, 'target': target_lang})
    else:
        form = TranslationForm()
    
    return render(request, 'translate/index.html', {'form': form})
