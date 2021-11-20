from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import *
from .form import Applyform
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    con = {'jobs' : page_obj}
    return render(request , 'job/job_list.html' , con )

def job_detail(request , id):
    job_detail = get_object_or_404(Job , pk = id)
    if request.method == 'POST':
        form = Applyform(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            
    else:
        form = Applyform()
    
    context = {'job':job_detail , 'form1' : form}
    return render(request,'job/job_detail.html',context)