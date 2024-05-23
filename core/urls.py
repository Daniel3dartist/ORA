from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from fake_gen import urls

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('items/', views.items, name='items'),
    path('sing-up/', views.sing_up, name='sing_up'),
    path('users/', views.users, name='users'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('fake-gen/', include(urls))
]
