from django.urls import path
from .views import PersonaView

urlpatterns = [
    path('personas/', PersonaView.as_view(), name='lista_personas'),
    path('personas/<int:id>', PersonaView.as_view(), name='process_persona')
]