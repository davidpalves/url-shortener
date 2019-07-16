from django.contrib import admin
from django.urls import path, include
from shorten import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('shorten.urls'))
]
