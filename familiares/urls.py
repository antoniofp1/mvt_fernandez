from django.urls import path
from familiares.views import probar_template


urlpatterns = [
    path('', probar_template),
]