"""treatmentsecurer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from admin.views import adminchangepassword1, hospreg1, staffreg1, doctorreg1, medreg1, labreg1, adminchangepassword2, \
    hospreg2, staffreg2, doctorreg2, medreg2, labreg2, stafflist1, stafflist2, medstocklist1, medstocklist2, \
    meddamagelist1, meddamagelist2, allot1, allot2, allot3, adminsignout, complaintreply1, complaintreply2, \
    complaintreply3, complaintreply11, complaintreply22, complaintreply33
from guest.views import home, adminlogin1, adminlogin2, stafflogin1, stafflogin2, hospitallist1, hospitallist2, medlist, \
    labtestlist, patientlogin1, patientlogin2, allotedlab1, allotedlab2, drlist, drlist1, drdays11, drdays22, drdays33, \
    about
from patient.views import patientchangepassword1, patientchangepassword2, opbook1, opbook2, opbook3, opbook4, opbook5, \
    opcancel1, opcancel2, opcancel3, patientprofile, patientcomingbooking, patientprevbooking, patientcomingcbooking, \
    patientpreviouscbooking, mycasefile, mylabtestresult2, mylabtestresult3, mymedsalelist2, mymedsalelist3, \
    patientsignout, complaint1, complaint2, viewreply1, viewreply2
from staff.views import patientreg1, staffchangepassword1, staffchangepassword2, medstockentry1, medstockentry2, \
    medstockentry3, meddamage1, meddamage2, meddamage3, medstocklist, meddamagelist, patientreg2, showpass, opdaysreg1, \
    opdaysreg2, opbooking1, opbooking2, sopbook1, sopbook2, sopbook3, sopbook4, sopbook5, opcancellation1, \
    opcancellation2, sopcancel1, sopcancel2, sopcancel3, drcomingbooking, drprevbooking, drcomingcbooking, \
    drprevcbooking, casesheetentry1, casesheetentry2, casesheetentry3, casesheet1, casesheet2, labtestentry1, \
    labtestentry2, labtestentry3, labtestentry33, labtestentry4, labtestrentry1, labtestrentry2, labtestrentry3, \
    labtestresult1, labtestresult1, labtestresult2, labtestresult3, down11, medsale1, medsale2, medsale3, medsale4, \
    medsale44, medsale5, medsalelist1, medsalelist2, medsalelist3, staffsignout, complaint11, complaint22, viewreply11, \
    viewreply22, plist1, plist2, plist11, plist22

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home),

    path('adminlogin1',adminlogin1),
    path('adminlogin2',adminlogin2),
    path('stafflogin1', stafflogin1),
    path('stafflogin2', stafflogin2),

    path('patientlogin1', patientlogin1),
    path('patientlogin2', patientlogin2),


    path('adminchangepassword1',adminchangepassword1),
    path('adminchangepassword2',adminchangepassword2),

    path('staffchangepassword1', staffchangepassword1),
    path('staffchangepassword2', staffchangepassword2),

    path('patientchangepassword1', patientchangepassword1),
    path('patientchangepassword2', patientchangepassword2),

    path('hospreg1',hospreg1),
    path('hospreg2', hospreg2),

    path('staffreg1',staffreg1),
    path('staffreg2',staffreg2),

    path('doctorreg1',doctorreg1),
    path('doctorreg2', doctorreg2),

    path('medreg1', medreg1),
    path('medreg2', medreg2),
    path('labreg1', labreg1),
    path('labreg2', labreg2),

    path('medstockentry1',medstockentry1),
    path('medstockentry2',medstockentry2),
    path('medstockentry3',medstockentry3),

    path('meddamage1',meddamage1),
    path('meddamage2',meddamage2),
    path('meddamage3',meddamage3),
    path('hospitallist1',hospitallist1),
    path('hospitallist2',hospitallist2),
    path('medlist',medlist),
    path('labtestlist',labtestlist),
    path('stafflist1',stafflist1),
    path('stafflist2',stafflist2),

    path('medstocklist1',medstocklist1),
    path('medstocklist2',medstocklist2),

    path('medstocklist',medstocklist),

    path('meddamagelist1',meddamagelist1),
    path('meddamagelist2', meddamagelist2),
    path('meddamagelist',meddamagelist),
    path('patientreg1',patientreg1),
    path('patientreg2',patientreg2),
    path('showpass',showpass),
    path('opdaysreg1',opdaysreg1),
    path('opdaysreg2',opdaysreg2),
    path('opbook1',opbook1),
    path('opbook2',opbook2),
    path('opbook3',opbook3),
    path('opbook4',opbook4),
    path('opbook5',opbook5),
    path('opcancel1',opcancel1),
    path('opcancel2',opcancel2),
    path('opcancel3',opcancel3),
    path('patientprofile',patientprofile),
    path('opbooking1',opbooking1),
    path('opbooking2',opbooking2),
    path('sopbook1',sopbook1),
    path('sopbook2', sopbook2),
    path('sopbook3', sopbook3),
    path('sopbook4', sopbook4),
    path('sopbook5', sopbook5),
    path('opcancellation1', opcancellation1),
    path('opcancellation2', opcancellation2),

    path('sopcancel1', sopcancel1),
    path('sopcancel2', sopcancel2),
    path('sopcancel3', sopcancel3),

    path('drcomingbooking', drcomingbooking),
    path('drprevbooking', drprevbooking),
    path('drcomingcbooking', drcomingcbooking),
    path('drprevcbooking', drprevcbooking),
    path('patientcomingbooking',patientcomingbooking),
    path('patientprevbooking',patientprevbooking),

    path('patientcomingcbooking',patientcomingcbooking),
    path('patientpreviouscbooking',patientpreviouscbooking),
    path('casesheetentry1',casesheetentry1),
    path('casesheetentry2',casesheetentry2),
    path('casesheetentry3',casesheetentry3),

    path('mycasefile',mycasefile),

    path('casesheet1',casesheet1),
    path('casesheet2',casesheet2),
    path('allot1',allot1),
    path('allot2',allot2),
    path('allot3',allot3),

    path('allotedlab1',allotedlab1),
    path('allotedlab2', allotedlab2),

    path('labtestentry1',labtestentry1),
    path('labtestentry2',labtestentry2),
    path('labtestentry3', labtestentry3),
    path('labtestentry33', labtestentry33),
    path('labtestentry4', labtestentry4),
    path('labtestrentry1',labtestrentry1),
    path('labtestrentry2',labtestrentry2),
    path('labtestrentry3',labtestrentry3),
    path('labtestresult1',labtestresult1),
    path('labtestresult2',labtestresult2),
    path('labtestresult3',labtestresult3),
    path('down11',down11),

    path('mylabtestresult2', mylabtestresult2),
    path('mylabtestresult3', mylabtestresult3),
    path('medsale1',medsale1),
    path('medsale2',medsale2),
    path('medsale3',medsale3),
    path('medsale4',medsale4),
    path('medsale44',medsale44),
    path('medsale5',medsale5),
    path('medsalelist1',medsalelist1),
    path('medsalelist2',medsalelist2),
    path('medsalelist3',medsalelist3),

    path('mymedsalelist2', mymedsalelist2),
    path('mymedsalelist3', mymedsalelist3),

    path('drlist', drlist),
    path('drlist1', drlist1),
    path('complaint1', complaint1),
    path('complaint2', complaint2),
    path('complaint11', complaint11),
    path('complaint22', complaint22),

    path('complaintreply1', complaintreply1),
    path('complaintreply2', complaintreply2),
    path('complaintreply3', complaintreply3),

    path('complaintreply11', complaintreply11),
    path('complaintreply22', complaintreply22),
    path('complaintreply33', complaintreply33),

    path('viewreply1', viewreply1),
    path('viewreply2', viewreply2),
    path('viewreply11', viewreply11),
    path('viewreply22', viewreply22),


    path('drdays11', drdays11),
    path('drdays22', drdays22),
    path('drdays33', drdays33),
    path('about', about),
    path('adminsignout', adminsignout),
    path('patientsignout', patientsignout),
    path('staffsignout', staffsignout),
    path('plist1',plist1),
    path('plist2',plist2),

    path('plist11',plist11),
    path('plist22',plist22),



]
