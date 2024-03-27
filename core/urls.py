from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apps.common.views import SponsorCreateAPIView, StudentSponsorCreateAPIView,StudentListAPIView, TotalAmountStatisticAPIView,MonthlyStatisticAPIView
from .schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('sponsor-create/', SponsorCreateAPIView.as_view()),
    path('sponsor-add/', StudentSponsorCreateAPIView.as_view()),
    path('students/', StudentListAPIView.as_view()),
    path('total-amount-statistic/', TotalAmountStatisticAPIView.as_view()),
    path('monthly-statistic/', MonthlyStatisticAPIView.as_view())
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
