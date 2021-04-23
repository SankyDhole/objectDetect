from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import objectDetect, getReport
from .models import uploadFile, object_store
import cv2
import xml.dom.minidom
import numpy as np
import os
from datetime import datetime
from djqscsv import render_to_csv_response, write_csv
from PIL import Image
# Create your views here.
if os.path.exists("media/abc.jpg"):
    os.remove("media/abc.jpg")

def index(request):
    context = {}
    object_detail = {}
    if request.method == "POST":
        form = objectDetect(request.POST, request.FILES)
        if form.is_valid():
            print (request.FILES['imgfile'])
            newxml = request.FILES['xmlfile']
            img_name = request.FILES['imgfile'].name
            print (img_name)
            file = request.FILES['imgfile'].read()
            npimg = np.fromstring(file, np.uint8)
            img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
            #print (img_name)
            if img is None:
                print ("HI")
            #cv2.imshow('img', img)
            dom = xml.dom.minidom.parse(newxml)
            root = dom.documentElement

            objects = dom.getElementsByTagName("object")
            list_objects = objects

            for object in list_objects:
                print(objects.index(object))

                bndbox = object.getElementsByTagName('bndbox')[0]
                print(bndbox)
                object_name = object.getElementsByTagName('name')[0]
                name = object_name.childNodes[0].data
                xmin = bndbox.getElementsByTagName('xmin')[0]
                ymin = bndbox.getElementsByTagName('ymin')[0]
                xmax = bndbox.getElementsByTagName('xmax')[0]
                ymax = bndbox.getElementsByTagName('ymax')[0]
                xmin_data = xmin.childNodes[0].data
                ymin_data = ymin.childNodes[0].data
                xmax_data = xmax.childNodes[0].data
                ymax_data = ymax.childNodes[0].data
                object_detail[name] = {}
                object_detail[name]['xmin_data'] = xmin_data
                object_detail[name]['ymin_data'] = ymin_data
                object_detail[name]['xmax_data'] = xmax_data
                object_detail[name]['ymax_data'] = ymax_data
                cv2.rectangle(img, (int(xmin_data), int(ymin_data)), (int(xmax_data), int(ymax_data)), (55, 255, 155),3)
                cv2.putText(img, name, (int(xmin_data), int(ymin_data) - 5), cv2.FONT_HERSHEY_COMPLEX, 0.3, (55, 255, 155), 1)
                print(object, "myobject")
            flag = 0
            flag = cv2.imwrite("media/abc.jpg", img)
            if (flag):
                print("doneab")
            print("all done ====================================")
            storedata = object_store(image_name=img_name, uploadtime = datetime.now(), object_detail = object_detail)
            storedata.save()
    else:
        form = objectDetect()
    context['form'] = form
    print (context)
    return render(request, "base.html", context)

def report(request):
    if request.method == "POST":
        start_date = request.POST.get('startdate')
        end_date = request.POST.get('enddate')
        if start_date <= end_date:
            print (start_date)
            print (end_date)
            x = object_store.objects.filter(uploadtime__range=[start_date,end_date]).values()
            print (x.all())
            with open('report.csv','wb') as csv_file:
                write_csv(x, csv_file)
        else:
            print ("Wrong input")
            return render(request, "report.html", {"msg":"Wrong Input"})
    return render(request, "report.html")