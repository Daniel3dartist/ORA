from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/accounts/', include('django.contrib.auth.urls')),
    path('api/itens/', views.item_list),
    path('api/post-item/', views.post_item),
    path('api/sing-up/', views.sing_up),
    path('api/is-user-available/', views.is_user_available),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
