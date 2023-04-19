import http
import imp
from unicodedata import category
from .models import student
from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(response):
    if response.method == "POST":
        # print(response.POST)
        # print(response.POST.get("name"))
        # print(response.POST.get("x_percent"))
        name = response.POST.get("name")
        x_percent = int(response.POST.get("x_percent"))
        xii_percent = int(response.POST.get("xii_percent"))
        xii_stream = response.POST.get("xii_stream")
        degree_percent = int(response.POST.get("degree_percent"))
        degree_cat  = response.POST.get("degree_cat")
        gender = response.POST.get("gender")
        category = response.POST.get("category")
        workex = int(response.POST.get("workex"))
        st = student(name=name,X_percent=x_percent,XII_percent=xii_percent,XII_stream=xii_stream,degree_percent=degree_percent,degree_cat=degree_cat,gender=gender,category=category,work_ex=workex)
        eligible,reasons = st.is_eligible_iima()
        msg = ""
        if eligible:
            msg = "Eligible"
        else:
            msg = "Not Eligible"

        return render(response,"result.html",{'msg': msg, 'reasons':reasons})
    
    
    return render(response,"first.html")

def index(response):
    if response.method == "POST":
        # print(response.POST)

        name = response.POST.get("Name")
        # Last_name = response.POST.get("Name_Last")
        email = response.POST.get("Email")
        phn = response.POST.get("PhoneNumber")
        x_percent = int(response.POST.get("x_percent"))
        xii_percent = int(response.POST.get("xii_percent"))
        xii_stream = response.POST.get("xii_stream")
        degree_percent = int(response.POST.get("degree_percent"))
        degree_cat  = response.POST.get("degree_cat")
        gender = response.POST.get("Gender")
        category = response.POST.get("category")
        workex = int(response.POST.get("workex"))
        # print(name,email,phn,x_percent,xii_percent,degree_percent,degree_cat,gender,category,workex)
        st = student(name=name,X_percent=x_percent,XII_percent=xii_percent,XII_stream=xii_stream,degree_percent=degree_percent,degree_cat=degree_cat,gender=gender,category=category,work_ex=workex)
        # res = st.IIMA()
        res = st.calculate()
        # print(res)
        return render(response,"table.html",{'res':res})
    return render(response,"new_index.html")

def table(response):
    return render(response,"table.html")