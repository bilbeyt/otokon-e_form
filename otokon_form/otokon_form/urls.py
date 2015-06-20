from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('form.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
