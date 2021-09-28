from django.urls import path
from core.views import AplicativosView

urlpatterns = [
    path('aplicativos/', AplicativosView.as_view(), name='aplicativos'),
]