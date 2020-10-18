"""stackcbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include #important
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view,register_page,login_page
from .router import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home_view'),
    path('profiles/',include('profiles.urls',namespace='profiles')), #namespace must match with app name in appurls.py
    path('posts/',include('posts.urls',namespace='posts')), #namespace must match with app name in appurls.py
    path('api/', include(router.urls)), #this will return all the apis url
    path('register/',register_page,name='register_page'),
    path('login/',login_page,name='login_page')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
