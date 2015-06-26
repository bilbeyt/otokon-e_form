from django.conf.urls import url
from form.views import FormCreateView, custom_login, custom_logout, auth_view
from . import views
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy


urlpatterns = [
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy("create")),
        name="base"),
    url(r'^create/$',
        FormCreateView.as_view(),
        name="create"),
    url(r'login/$',
        views.custom_login ,
        name = 'login'),
    url(r'logout/$',
        views.custom_logout,
        name="realout"),
    url(r'auth/$',
        views.auth_view,
        name="auth"),

    ]
