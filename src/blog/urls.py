from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from auth_app import views as auth_views

urlpatterns = [
    path("", views.home_view, name="home"),
    path('admin/', admin.site.urls),
    path("signup/", auth_views.signup, name="signup"),
    path("login/", auth_views.login, name="login"),
    path("settings/", auth_views.settings, name="settings"),
]

# if settings.DEBUG:
#     from django.conf.urls.static import static
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.TE_URL,
#                           document_root=settings.STATIC_ROOT)