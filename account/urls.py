from django.urls import path
from .import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register',views.register,name='register'),
    path('profile',views.profile,name='profile'),
    path('login',auth_view.LoginView.as_view(template_name = 'login.html'),name="user-login"),
    path('logout',auth_view.LogoutView.as_view(template_name = 'logout.html'),name="user-logout")
]

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)