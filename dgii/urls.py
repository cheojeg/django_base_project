from django.conf.urls import url
from dgii.api import views as api_views

urlpatterns = [
    # url(r'^$', views.actions_list, name='actions_list'),
    url(
        regex=r'^dgii_query$',
        view=api_views.ActionListAPIView.as_view(),
        name='dgii_query'
    )
]
