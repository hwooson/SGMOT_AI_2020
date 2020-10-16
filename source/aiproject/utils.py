from django.conf import settings
from google.cloud import translate_v2 as translate


def google_translate(text, source_lang, target_lang):
    translated_text = ''
    translate_client = translate.Client(credentials=settings.GOOGLE_CREDENTIAL)
    # 소스 언어 및 타겟 언어 설정
    source_lang = source_lang
    target_lang = target_lang
    result = translate_client.translate(
        text, source_language=source_lang, target_language=target_lang)
    if isinstance(result, dict):
        translated_text = result['translatedText']
    return translated_text
