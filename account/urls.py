from django.urls import path
from django.urls.conf import include

from .models import *
from . import views
from .views import LoginView , UserView , LogoutView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('faculty',views.Faculty_Detail)
router.register('user-profile',views.user_profile)
router.register('approval',views.Approval_Detail)
router.register('document',views.Document_Detail)


urlpatterns = [
    path('',include(router.urls)),
    path('login', LoginView.as_view(), name="login",),
    path('profile', UserView.as_view(), name="profile",),
    path('logout', LogoutView.as_view(), name="logout",),
    path('user_update/<str:pk>/',views.Userupdate)

]
