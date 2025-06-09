# from django import forms
from django.contrib import admin
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
#
#
# from modeltranslation.admin import TranslationAdmin

from .models import Book, Genre, Author, Language

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Book)
#
#
# class BookAdminForm(forms.ModelForm):
#     description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
#     description_ky = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
#
#     class Meta:
#         model = Book
#         fields = '__all__'
#
# @admin.register(Book)
# class BookAdmin(TranslationAdmin):
#     list_display = ("title", "content")
#     list_display_links = ("title", "content")