from django.contrib import admin
from django.urls import path
from TODO import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path('add/', views.add, name="add"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('clear/', views.clear, name="clear"),

    path('login/', views.login_user, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout_view, name="logout"),
]
