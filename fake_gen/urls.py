from django.urls import path
from fake_gen.views import item_gen, user_gen

urlpatterns = [
    path('api/generator/user-gen/', user_gen),
    path('api/generator/item-gen/', item_gen),
]