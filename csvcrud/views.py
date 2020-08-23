from django.shortcuts import render
from django.http import HttpResponse
import csv
from csv import writer
import os
import mimetypes

def home(request):
    return render(request, 'csvcrud/home.html')

def addpg(request):
    return render(request, 'csvcrud/add.html')

def displaypg(request):
    return render(request, 'csvcrud/display.html')

def displayallpg(request):
    
    infodict = {}
    flist = []
    with open('students.csv', newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            flist.append(row)
    context = {'stuinfo': flist }
    return render(request, 'csvcrud/displayall.html', context)

def add(request):
    
    if request.method == "GET":
        
        sid = request.GET['sid']
        sname = request.GET['sname']
        gender = request.GET['gender']
        dob = request.GET['dob']
        city = request.GET['city']
        state = request.GET['state']
        email = request.GET['email']
        quali = request.GET['quali']
        stream = request.GET['stream']

        alist = [sid, sname, gender, dob, city, state, email, quali, stream ]
        
        # Open file in append mode
        with open('students.csv', 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(alist)
        print("Added Successfully!!!")

        print(sid)
        
        infodict = {}
        flist = []
        
        infodict['sid']=sid
        infodict['name']=sname
        infodict['gender']=gender
        infodict['dob']=dob
        infodict['city']=city
        infodict['state']=state
        infodict['email']=email
        infodict['quali']=quali
        infodict['stream']=stream

        flist.append(infodict)
        context = {'stuinfo': flist }
        return render(request, 'csvcrud/printt.html', context)

def display(request):

    if request.method == "GET":
        sid = request.GET['sid']
        infodict = {}
        flist = []
        with open('students.csv', newline='') as csvfile:
            data = csv.DictReader(csvfile)
            for row in data:
                if row['sid'] == sid: 
                    infodict['sid']=row['sid']
                    infodict['name']=row['name']
                    infodict['gender']=row['gender']
                    infodict['dob']=row['dob']
                    infodict['city']=row['city']
                    infodict['state']=row['state']
                    infodict['email']=row['email']
                    infodict['quali']=row['quali']
                    infodict['stream']=row['stream']
        flist.append(infodict)
        context = {'stuinfo': flist }
        return render(request, 'csvcrud/printt.html', context)


def exportcsv(request):
    pass

def download_file(request):
    # fill these variables with real values
    fl_path = "students.csv"
    filename = "students_data.csv"

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response