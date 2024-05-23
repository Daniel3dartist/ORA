from django.urls import path
from fake_gen.views import item_gen, user_gen

urlpatterns = [
    path('generator/user/', user_gen, name='user_gen'),
    path('generator/item/', item_gen, name="item_gen"),
]