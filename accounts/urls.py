from django.urls import path
from django.urls.resolvers import URLPattern
from accounts import views

urlpatterns=[
    path('login/',views.login_view),
    path('logout/',views.logout_view),
    
]
