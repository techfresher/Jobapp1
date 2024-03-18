from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader

from app.models import Jobpost

# Create your views here. 
job_title = [
    "first job",
    "second job",
    "third job",
    "fourth job",
    "six job"
]

job_description = [
    "frist job description ",
    "second job description",
    "third job description", 
    "fourth job description",
    "six job description"

]

# def hello(request):
#     return HttpResponse("<h1>Hello world</h1>")  T

class TempClass:
    x = 5


def hello (request):
    list = ["alpha", "Beta"]
    temp = TempClass()
    is_authenticated = True 
    context = {"name":"Joshua", "age": 10, "first_list":list, "temp_object":temp, "is_authenticated": is_authenticated}
    #return HttpResponse(template.render(context, request))
    return render (request, "app/hello.html", context)

def job_list(request):    
    # #<ul><li> job 1</li> <li>job 2</li> <li>job 3</li></ul>
    # list_of_jobs = "<ul>"
    # for j in job_title: 
    #     job_id = job_title.index(j)
    #     url_detail = reverse('job_detail', args=(job_id,))
    #     list_of_jobs += f"<li><a href='{url_detail}'>{j}</a></li>"
    # list_of_jobs += "</ul>"
    # return HttpResponse(list_of_jobs)
    jobs = Jobpost.objects.all()
    context = {"jobs": jobs }
    return render (request, "app/index.html", context)
    
def job_detail(request, id):
    try:
        print(type(id))
        if id == 2: 
            return redirect(reverse('jobs_home'))
        #return_html = f"<h1>{job_title[id]}  </h1> <h3>{job_description[id]}</h3>" 
        #return HttpResponse (return_html)
        job = Jobpost.objects.get(id=id)
        context = {"job": job}
        return render(request, "app/job_details.html", context)
    except:
        return HttpResponseNotFound('Not Found')
    