from django.urls import path , include
from.views import *
urlpatterns = [
    path('' , job_list),
    path('<int:id>' , job_detail)
]
