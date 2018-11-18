from django.conf.urls import include, url

#Django Rest Framework
from rest_framework import routers

from api import controllers
from django.views.decorators.csrf import csrf_exempt

#REST API routes
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'profiles', controllers.ProfileViewSet)
router.register(r'commissions', controllers.CommissionViewSet)

urlpatterns = [
    url(r'^session', csrf_exempt(controllers.Session.as_view())),
    url(r'^register', csrf_exempt(controllers.Register.as_view())),
    url(r'^events/$', csrf_exempt(controllers.Events.as_view())),
    url(r'^events/(?P<pk>\d+)$', csrf_exempt(controllers.EventDetail.as_view())),
    #url(r'^profiles/$', csrf_exempt(controllers.Profiles.as_view())),
    #url(r'^profiles/(?P<pk>\d+)$', csrf_exempt(controllers.ProfileDetail.as_view())),
    #url(r'^commissions/$', csrf_exempt(controllers.Commissions.as_view())),
    #url(r'^commissions/(?P<pk>\d+)$', csrf_exempt(controllers.CommissionDetail.as_view())),
    url(r'^activateifttt', csrf_exempt(controllers.ActivateIFTTT.as_view())),
    url(r'^', include(router.urls)),
]
