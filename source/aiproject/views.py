from django.shortcuts import render


def index(request):
    source_text = request.POST.get('source_text', '')
    translated_text = ''

    context = {
        'source_text': source_text,
        'translated_text': translated_text
    }
    return render(request, 'aiproject/index.html', context)
