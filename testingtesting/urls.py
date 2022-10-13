from django.urls import include, path
from rest_framework import routers
from testingtesting.newapp import views

router = routers.DefaultRouter()
router.register(r'people', views.PersonViewSet)
router.register(r'random', views.RandomPersonViewSet, basename='RandomMale')
router.register(r'address', views.AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))]

