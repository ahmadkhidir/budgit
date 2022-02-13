from django import template
from googletrans import Translator

register = template.Library()


@register.simple_tag(takes_context=True)
def translate(context, text):
    lang = context.get("lang")
    if lang == 'en':
        return text
    translator = Translator(raise_exception=True)
    try:
        translation = translator.translate(text, dest=lang)
        return translation.text
    except Exception:
        return text
