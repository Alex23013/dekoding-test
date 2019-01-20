from django.urls import path

from .views import (
    IndexView,
    FrontendView,
    BackendView,
    DogListView,
    DogAddView,
)


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('frontend/', FrontendView.as_view(), name="frontend"),
    path('backend/', BackendView.as_view(), name="backend"),
    path('dog/list', DogListView.as_view(), name="dogList"),
    path('dog/add', DogAddView.as_view(), name="dogAdd"),
]
