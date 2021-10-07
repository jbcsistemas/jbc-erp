from django.urls import path
from core.views import AplicativosView

app_name = 'core'
urlpatterns = [
    path('aplicativos/', AplicativosView.as_view(), name='aplicativos'),
]