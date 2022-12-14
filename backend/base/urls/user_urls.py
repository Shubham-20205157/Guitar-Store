from django.urls import path

from base.views import userViews as views

urlpatterns = [
    path('',views.getUsers, name='users'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/',views.registerUser,name = 'register-user'),
    path('profile/',views.getUserProfile, name='user-profile'),
    path('profile/update/',views.updateUserProfile, name='user-profile-update'),


]
