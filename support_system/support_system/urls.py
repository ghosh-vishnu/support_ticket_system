from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('tickets.urls')),
#     path('api/token/', obtain_auth_token),
# ]
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tickets.urls')),
    path('api/token/', obtain_auth_token),   
    path('api-auth/', include('rest_framework.urls')), 
]
