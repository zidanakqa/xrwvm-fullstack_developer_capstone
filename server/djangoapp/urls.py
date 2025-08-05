from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView  # Add this import
from . import views

app_name = 'djangoapp'
urlpatterns = [
  # path for dealerships
  # path for login
  path(route='login', view=views.login_user, name='login'),
  path(route='get_cars', view=views.get_cars, name ='getcars'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)