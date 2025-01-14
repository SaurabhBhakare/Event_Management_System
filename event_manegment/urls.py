from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from events import user_login
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('events.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh'),


    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', user_login.REGISTER, name='signup'),
    path('dologin/', user_login.DOLOGIN, name='dologin'),
    path('guest_login/', user_login.GUEST_LOGIN, name='guest_login'),
    path('dologout/', user_login.DOLOGOUT, name='dologout'),

    path('', views.home, name='home'),
    path('event_list/', views.event_list, name='event_list'),
    path('category_list/', views.category_list, name='category_list'),
    path('create_category/', views.create_category, name='create_category'),
    path('add/', views.add_event, name='add_event'),
    path('<int:pk>/update/', views.update_event, name='update_event'),
    path('<int:pk>/delete/', views.delete_event, name='delete_event'),
    path('<int:pk>/delete_category/', views.delete_category, name='delete_category'),
    path('<int:pk>/', views.event_detail, name='event_detail'),

    path('guest_event_list/', views.guest_event_list, name='guest_event_list'),
    path('<int:pk>/guest_event_details/', views.guest_event_details, name='guest_event_details'),
    path('login_required/', user_login.LOGIN_REQUIRED, name='login_required'),
]
