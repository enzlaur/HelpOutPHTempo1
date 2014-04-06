from django.template import Context, Template
from django.shortcuts import render
from django.http import HttpResponse
from google.appengine.ext import db
from models import RescueReport, HeatMapPins, ReliefOrg

def home(request):
    if 'fnames' in request.GET:
        r = RescueReport(names = request.GET['fnames'],
                         location = request.GET['flocation'],
                         situation = request.GET['fsituation'],
                         contactinfo = request.GET['fcontact']) 
        r.put()
        return thanksreport(request)
    else:
        return render(request, 'index.html')

def report(request):
    if 'fnames' in request.GET:
        r = RescueReport(names = request.GET['fnames'],
                         location = request.GET['flocation'],
                         situation = request.GET['fsituation'],
                         contactinfo = request.GET['fcontact']) 
        r.put()
        return thanksreport(request)
    else:
        return render(request, 'index.html')

def thanksreport(request):
    return render(request, 'thanks-report.html')

def deployedtowhere(request):
    if 'lat' in request.GET:
        hmp = HeatMapPins(lat = request.GET['lat'],
                          long = request.GET['long'])
        hmp.put()
    return render(request, 'deployedtowhere.html')

def giverelief(request):
    return render(request, 'giverelief.html')

def listofcauses(request):
    causes = ReliefOrg.all()
    return render(request, 'listofcauses.html', {'causes':causes})

def reportssubmitted(request):
    rrs = RescueReport.all()
    return render(request, 'reportssubmitted.html', {'rrs':rrs})

def tweettoform(request):
    if 'fnames' in request.GET:
        r = RescueReport(names = request.GET['fnames'],
                         location = request.GET['flocation'],
                         situation = request.GET['fsituation'],
                         contactinfo = request.GET['fcontact']) 
        r.put()
        return render(request, 'tweettoform.html')
    else:
        return render(request, 'tweettoform.html')
  


