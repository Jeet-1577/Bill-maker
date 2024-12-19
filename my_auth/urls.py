from django.urls import path
from my_auth import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.handlelogin,name='handlelogout'),
    path('logout/',views.handlelogout,name='handlelogout'),
    path('activate/<uidb64>/<token>', views.ActivateAccountView.as_view(), name='activate'),
]
