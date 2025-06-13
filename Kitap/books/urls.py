from os.path import basename

from rest_framework.routers import DefaultRouter


from .views import BookViewSet,ReviewViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'reviews', ReviewViewSet, basename = 'review')

urlpatterns = router.urls