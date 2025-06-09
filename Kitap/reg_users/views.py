from django.contrib.auth.models import User
from rest_framework import viewsets

from Kitap.reg_users.models import Profile, Selected, Readlater, Reading, History, Purchases
from Kitap.reg_users.serializers import ProfileSerializers, UserSerializers, SelectedSerializer, ReadlaterSerializer, \
    ReadingSerializer, HistorySerializer, PurchasesSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class SelectedViewSet(viewsets.ModelViewSet):
    queryset = Selected.objects.all()
    serializer_class = SelectedSerializer

    def add_to_selected(user, book):
        if book.is_available:
            selected, created = Selected.objects.get_or_create(user=user, book=book)
            if created:
                return "Книга добавлена в избранное."
            else:
                return "Книга уже в избранном."
        else:
            return "Книга недоступна и не может быть добавлена."

    def remove_from_selected(user, book):
        try:
            selected = Selected.objects.get(user=user, book=book)
            selected.delete()
            return "Книга удалена из избранного."
        except Selected.DoesNotExist:
            return "Этой книги нет в избранном."

class ReadlaterViewSet(viewsets.ModelViewSet):
    queryset = Readlater.objects.all()
    serializer_class = ReadlaterSerializer

    def add_readlater(user, book):
        to_read, created = Readlater.objects.get_or_create(user=user, book=book)
        if created:
            return "Книга добавлена в 'Читать позже'."
        else:
            return "Эта книга уже есть в 'Читать позже'."

    def remove_readlater(user, book):
        try:
            to_read = Readlater.objects.get(user=user, book=book)
            to_read.delete()
            return "Книга удалена из 'Читать позже'."
        except Readlater.DoesNotExist:
            return "Этой книги нет в 'Читать позже'."

class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer



class PurchasesViewSet(viewsets.ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer