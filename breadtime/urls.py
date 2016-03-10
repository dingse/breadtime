"""breadtime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from bread import views

urlpatterns = [
#	url(r'^$', views.bread_list, name='bread_list'),
    url(r'^admin/', admin.site.urls),
    url(r'^bread/(\d+)$', views.single_bread, name='view_single_bread'),
    url(r'^$', views.bread_boot, name='view_bread_boot'),
    url(r'^html/', views.bread_html, name='view_bread_html'),
    url(r'^accounts/login', auth_views.login, name='login', 
            kwargs={
                'template_name':'bread/login.html'}
                ),
    url(r'^accounts/logout', auth_views.logout, name='logout', 
            kwargs={
                'template_name':'bread/logout.html'}
                ),
    url(r'^bread/upload/$', views.new_bread, name='view_new_bread'),
    url(r'^bread/upload_object/$', views.new_bread_object, name='view_new_bread_object'),
#    url(
#    	r'^accounts/login/',
#    	name = 'login',
#    	kwargs = {
#    		'template_name': 'login.html'
#    	}
#    ),
#    url(
#    	r'^accounts/logout/',
#    	'django.contrib.auth.views.logout',
#    	name = 'logout'
#    ),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(
	settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
	)








