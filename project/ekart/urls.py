from django.urls import path
from ekart import views

urlpatterns=[
    path('',views.Home.as_view(),name="home"),
    path('signup',views.SignUpView.as_view(),name="signup"),
    path('signin',views.SignInView.as_view(),name="signin"),
    path('signout',views.SignOutView.as_view(),name="signout"),
    path('detail/<int:id>',views.ProductDetailView.as_view(),name="detail"),
    
    
]