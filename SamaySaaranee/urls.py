from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "SAMAY-SAARANEE Admin"
admin.site.site_title = "SAMAY-SAARANEE Admim"
admin.site.index_title = "Welcome to SAMAY-SAARANEE"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
