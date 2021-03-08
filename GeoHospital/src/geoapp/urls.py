from .serializers import HospitalSerializer
from .views import HospitalView, SearchHospital, HospitalDetails
from .views import  HospitalList

from django.urls import path, re_path

urlpatterns = [
    path('hospital', HospitalView.as_view(), name='hospital'),
    path('hospital/<int:pk>', HospitalDetails.as_view(), name='hospital_details'),
    path('search_hospital', SearchHospital.as_view(), name='search_hospital'),
    # path('hospitallist', HospitalList.as_view(), name='hospital_list'),
    # re_path('^hospitallist/(?P<name>.+)/$', HospitalList.as_view()),
]