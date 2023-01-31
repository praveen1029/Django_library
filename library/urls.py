from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name='home'),
    path('book/',views.book_page,name='book'),
    path('book/<int:book_num>/details/',views.book_detail_page,name='book_detail'),
]