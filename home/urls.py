from django.conf.urls import url
from home.views import HomePageView, AboutPageView
urlpatterns = [
    url(r'^$', HomePageView.as_view(), name="home"),
    url(r'^about/$', AboutPageView.as_view(), name="about"),
    #url(r'contact/^$', HomePageView.as_view(), name="contact"),
]
