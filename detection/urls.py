from django.conf.urls import url
from detection.api import views as api_views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url, include

urlpatterns = [
    url(
        regex=r'^detection/(?P<uuid>.+)/$',
        view=api_views.DectectionAPIView.as_view(),
        name='detection'
    ),
    url(
        regex=r'^detection/$',
        view=api_views.DectectionAPIView.as_view(),
        name='detection'
    ),
]
