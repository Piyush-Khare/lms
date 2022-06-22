from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', login_view, name="login_view"),
    path('signup/', signup_view, name="signup_view"),
    path('logout/', logout_view, name="logout_view"),
    path('allbook/', allbook, name="allbook"),
    path('add_book/', add_book, name="add_book"),
    path('view_book/' , view_book , name="view_book"),
    path('delete/<id>' , delete , name="delete"),
    path('update/<id>/' , update , name="update"),

]