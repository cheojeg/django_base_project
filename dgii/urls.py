from django.conf.urls import url
from dgii.api import views as api_views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url, include

urlpatterns = [
    # url(r'^$', views.actions_list, name='actions_list'),
    url(
        regex=r'^dgii_query/(?P<license_plate>.+)/$',
        view=api_views.MarbeteAPIView.as_view(),
        name='dgii_query'
    ),
    url(regex=r'^get-token/', view=obtain_auth_token),
    # url(regex=r'^auth/',
    #     view=include('rest_framework.urls', namespace='rest_framework')
    # ),
]
