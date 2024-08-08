from django.urls import path
from .views import CatDetails, CatList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", CatList.as_view()),
    path("<int:id>", CatDetails.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
