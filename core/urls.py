from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/accounts/', include('django.contrib.auth.urls')),
    path('api/items/', views.items, name='items'),
    path('api/sing-up/', views.sing_up, name='sing_up'),
    path('api/users/', views.users, name='users'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
