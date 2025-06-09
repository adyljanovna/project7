from modeltranslation.translator import register, TranslationOptions
from .models import Book


@register(Book)
class BookTranslate(TranslationOptions):
    fields = ('title', 'content')
