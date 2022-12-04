from django.urls import path
from App_login import views


app_name = "App_login"

urlpatterns = [
    path('signup/', views.SignUp, name='sign_up'),
    path('login/', views.login_page, name = 'login'),
    path('edit/', views.edit_profile, name='edit'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.Profile, name = 'user_profile'),
    path('user/<username>', views.user, name='user'),
    path('follow/<username>',views.follow, name='follow'),
    path('unfollow/<username>',views.unfollow, name ='unfollow'),
]