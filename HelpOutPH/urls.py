from django.conf.urls import patterns, include, url
from views import *
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    url(r'^$', home),
    url(r'^report/', report),
    url(r'^deployedtowhere/', deployedtowhere),
    url(r'^giverelief/', giverelief),
    url(r'^listofcauses/', listofcauses),
    url(r'^reportssubmitted/', reportssubmitted),
    url(r'^tweettoform/', tweettoform),
    url(r'^thanks-report/', thanksreport),





    
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    
    
)
