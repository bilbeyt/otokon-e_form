from django.conf.urls import url
from form.views import FormCreateView


urlpatterns = [
    url(r'',
        FormCreateView.as_view(),
        name="create"),
    ]
