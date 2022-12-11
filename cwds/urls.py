from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.contrib.auth import views as auth_views
from django.conf.urls import (
handler400, handler403, handler404, handler500
)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='registration/login.html',
        extra_context={
        	'title':'Admin',
        	'next': '/admin-dashboard',
        }), name='login'),
    url(r'^agency-login/$', auth_views.LoginView.as_view(template_name='registration/staff_login.html',
        extra_context={
        	'title':'Agency Join',
        	'next': '/agency-dashboard',
        	'join_us':'/create-agency'
        }), name='agency_login'),
    url(r'^plant-login/$', auth_views.LoginView.as_view(template_name='registration/staff_login.html',
        extra_context={
        	'title':'Plant Join',
        	'next': '/plant-dashboard',
        	'join_us':'/create-plant'
        }), name='plant_login'),
    url(r'^user-login/$', auth_views.LoginView.as_view(template_name='registration/staff_login.html',
        extra_context={
        	'title':'User Join',
        	'next': '/user-dashboard',
        	'join_us':'/create-user'
        }), name='user_login'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('myuser.urls',namespace='myuser')),
    url(r'^', include('general.urls',namespace='general'))
]

handler400 = "cwds.views.handler400"
handler403 = "cwds.views.handler403"
handler404 = "cwds.views.handler404"
handler500 = "cwds.views.handler500"