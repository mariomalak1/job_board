from django.urls import path , include
from.views import *
#my urls

app_name = 'job'

urlpatterns = [
    path('' , job_list),
    path('<int:id>' , job_detail , name = 'job_detail')
]
