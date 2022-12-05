from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_lifestyle', views.about_lifestyle, name='about_lifestyle'),
    path('about_bodypoint', views.about_bodypoint, name='about_bodypoint'),
    path('lifestyle', views.lifestyle, name='lifestyle'),
    path('bodypoint', views.bodypoint, name='bodypoint'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('upload/',views.upload, name="upload"),
    path('tmp_result',views.tmp_result, name="tmp_result"),
    path('upload_create/', views.upload_create, name="upload_create"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)