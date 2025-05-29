from django.urls import path

from .views import omonim_view,omonimlar_search,omonim_create
urlpatterns = [
    path('search/', omonimlar_search, name='omonimlar-search'),
    path('create/', omonim_create, name='omonimlar-create'),
    path('tafsilot/', omonim_view, name='omonimlar'),

]