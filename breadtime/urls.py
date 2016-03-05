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
from bread import views

urlpatterns = [
#	url(r'^$', views.bread_list, name='bread_list'),
    url(r'^admin/', admin.site.urls),
    url(r'^bread/(\d+)$', views.single_bread, name='view_single_bread'),
    url(r'^$', views.bread_boot, name='view_bread_boot'),
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








