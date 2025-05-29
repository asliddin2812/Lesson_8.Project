from django.urls import path

from .views import omonim_view,omonimlar_search,omonim_create,omonimlar_list,omonim_tafsiloti_list
urlpatterns = [
    path('',omonimlar_list,name='omonimlar_list'),
    path('tafsilot/',omonim_tafsiloti_list,name='omonimlar_tafsiloti_list'),
    path('search/', omonimlar_search, name='omonimlar-search'),
    path('create/', omonim_create, name='omonimlar-create'),
    path('tafsilot_create/', omonim_view, name='omonimlar'),

]