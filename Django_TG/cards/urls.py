from django.urls import path
from . import views

app_name = 'cards'

urlpatterns = [
    path('expansions/<str:expansion_name>/', views.cards_by_expansion, name='cards_by_expansion'),
    path('expansion/ajax/', views.cards_by_expansion_ajax, name='cards_by_expansion_ajax'),
    path('update_owned_status/', views.update_card_ownership, name='update_owned_status'),
]