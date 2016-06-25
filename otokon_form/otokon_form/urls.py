from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from form_api import views


admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'form', views.FormViewSet)
router.register(r'mail', views.EmailMessageViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('form.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
