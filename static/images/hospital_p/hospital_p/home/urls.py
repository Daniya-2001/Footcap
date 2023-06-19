
from django.urls import path
from.import views
urlpatterns = [
    path('',views.index,name="index"),
    path('department',views.department,name="department"),
    path('department/<str:slug>',views.doctors,name="doctors"),
    path('book',views.booking,name="book"),
    path('login',views.loginn,name="login"),
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    path('about',views.about,name="about")
]
