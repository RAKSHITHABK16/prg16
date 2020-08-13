from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('img/',views.img_upld,name="img"),
    path('img_display/',views.img_display,name="img_display"),
]