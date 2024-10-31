from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhoneNumberViewSet, UploadExcelView

router = DefaultRouter()
router.register(r'phone-numbers', PhoneNumberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload-phone-numbers/', UploadExcelView.as_view(), name='upload-phone-numbers'),
]
