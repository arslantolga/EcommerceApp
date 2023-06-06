from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "ecommerce_app"


urlpatterns = [
    path("", views.mainpage, name="mainpage"),
    path("login/", views.loginpage, name="loginpage"),
    path("signup/", views.signuppage, name="signuppage"),
    path("store/", views.storepage, name="storepage"),
    path("addproduct/", views.addproductpage, name="addproductpage"),
    path("sort/", views.sortpage, name="sortpage"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)