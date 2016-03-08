from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from app.views import UserCreateView, MainView, SuggestionCreateView, AlcoholCreateView, UserDetailView, AddFollower

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^main/$', MainView.as_view(), name="main_view"),
    url(r'^login/$', auth_views.login, name="login_view"),
    url(r'^logout/$', auth_views.logout_then_login, name="logout_view"),
    url(r'^addalcohol/$', AlcoholCreateView.as_view(), name="alcohol_create_view"),
    url(r'^makesuggestion/$', SuggestionCreateView.as_view(), name="suggestion_create_view"),
    url(r'^memberdetails/(?P<pk>\d+)/$', UserDetailView.as_view(), name="user_detail_view"),
    url(r'^addfollower/(?P<pk>\d+)$', AddFollower.as_view(), name='add_follower_view')
]
