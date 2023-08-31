from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('itens/', views.item_list),
    path('post-item/', views.post_item),
    path('sing-up/', views.sing_up),
    path('is-user-available/', views.is_user_available),
]
