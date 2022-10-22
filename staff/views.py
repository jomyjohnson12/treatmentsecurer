import os
from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.
from treatmentsecurer import connect, ccdate


def patientreg1(request):
    con = connect()
    cursor = con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"


    return render(request,"patientreg1.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd})

def patientreg2(request):
    con=connect()
    cursor=con.cursor()
    #---
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"



    #----
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    s3 = request.POST["t3"]
    s4 = request.POST["t4"]
    s5 = request.POST["t5"]
    s6 = request.POST["t6"]
    s7 = request.POST["t7"]
    s8 = request.POST["t8"]
    s9 = request.POST["t9"]
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
        hospid=row[1]
    regdate=ccdate()
    pid = "P10000"
    s = "select * from patient order by pid desc"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        pid = row[0]
        break
    x = pid[1:]
    y = int(x)
    y = y + 1

    pid = "P" + str(y)
    regdate = ccdate()
    xx=""
    s="select * from patient where ph='"+ s5 +"'"
    cursor.execute(s)
    if cursor.rowcount>0:
        msg="This patient with same phone number already registered"
    else:
        s = "insert into patient values('" + pid + "','" + s1 + "','" + s2 + "','" + s3 + "','" + str(s4) + "','" + str(s5) + "','" + s6 + "','" + s7 + "','" + str(s8) + "','" + str(s9) + "','" + regdate + "','" + str(s5) + "','"  + staffid  + "','" + hospid +  "')"
        cursor.execute(s)
        con.commit()
        xx="yes"
        msg="Patient rgistered...The patient ID is "+ pid +" and password is the phone number"
    return render(request,"patientreg2.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'xx':xx,'msg':msg,'pid':pid,'s1':s1 ,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'s9':s9})

def showpass(request):
    con=connect()
    cursor=con.cursor()
    s="select * from patient order by pid desc "
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        pid=row[0]
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
        adharno = row[9]
        regdate=row[10]
        staffid = row[12]
        hospid=row[13]


    s="select * from hospital where hospid='"+ hospid  +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location1=row[1]
        place1 = row[2]
        pin1 = row[3]
        phone1= row[4]
        district1 = row[5]
        email1 = row[6]
        htype1=row[7]

    return render(request,"showpass.html",{'pid':pid,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'staffid':staffid,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})

def staffchangepassword1(request):
    con = connect()
    cursor = con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa=""
    bb=""
    cc=""
    dd=""
    if desig=="Pharmacist":
        aa="yes"
    elif desig=="Dr":
        bb="yes"
    elif desig=="Office Staff":
        cc="yes"
    elif desig=="Lab Staff":
        dd="yes"



    return render(request,"staffchangepassword.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd})

def staffchangepassword2(request):
    con = connect()
    cursor = con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]


    s1 = request.POST["t1"]
    s2 = request.POST["t2"]
    s = "select * from staff where staffid ='" + staffid + "' and   password='" + s1 + "'"
    cursor.execute(s)
    if cursor.rowcount == 0:
        msg = "Invalid User ID or Pasword"
        return render(request, "staffchangepassword.html", {'msg': msg})
    else:
        s="update staff set password='"+ s2 +"'  where staffid='"+ staffid +  "'"

        cursor.execute(s)
        con.commit()
        msg="Successfully Changed..."
        return render(request, "staffchangepassword.html",{'msg': msg})

def medstockentry1(request):
    con=connect()
    cursor=con.cursor()
    #----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #-----
    l=[]
    s="select medname from pharmacymed"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        l.append(row[0])
    return render(request,"medstockentry1.html",{'l':l,'aa':aa,'bb':bb,'cc':cc,'dd':dd })


def medstockentry2(request):
    con=connect()
    cursor=con.cursor()
    #---
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #----
    s1=request.POST["c1"]
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[1]

    s="select * from pharmacymed where medname='"+ s1 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        medtype=row[1]
        company=row[2]
        content=row[3]
        medunit=row[4]
    s = "select * from medstock where medname='" + s1 + "' and hospid='"+ hospid + "'"

    cursor.execute(s)
    records=cursor.fetchall()
    cstock=0
    for row in records:
        cstock=row[2]


    l=[]
    s="select medname from pharmacymed"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        l.append(row[0])
    return render(request,"medstockentry2.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'cstock':cstock,'s1':s1,'l':l,'medtype':medtype,'company':company,'content':content,'medunit':medunit,'cstock':cstock})


def medstockentry3(request):
    con=connect()
    cursor=con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa=""
    bb=""
    cc=""
    dd=""
    if desig=="Pharmacist":
        aa="yes"
    elif desig=="Dr":
        bb="yes"
    elif desig=="Office Staff":
        cc="yes"
    elif desig=="Lab Staff":
        dd="yes"

    #----
    s1=request.POST["c1"]
    s2=request.POST["t1"]

    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
        hospid=row[1]
    eno=0
    s="select * from medstockentry order by eno desc"
    cursor.execute(s)
    records =cursor.fetchall()
    for row in records:
        eno=row[0]
        break
    eno=eno+1
    edate=ccdate()
    s="insert into medstockentry values("+ str(eno) + ",'" + s1 + "','" + hospid + "'," + s2 + ",'"+ staffid + "','" + edate + "')"
    cursor.execute(s)
    con.commit()
    s="select * from medstock where medname='"+s1 + "' and hospid='"+ hospid + "'"
    cursor.execute(s)
    if cursor.rowcount==0:
        s="insert into medstock values('"+ s1 + "','" + hospid + "',"+ s2 + ")"
        cursor.execute(s)
        con.commit()
    else:
        s="update medstock set cstock=cstock+ " + s2 + " where medname='" + s1 +"' and hospid='"+ hospid +"'"
        cursor.execute(s)
        con.commit()


    s="select * from pharmacymed where medname='"+ s1 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        medtype=row[1]
        company=row[2]
        content=row[3]
        medunit=row[4]
    s = "select * from medstock where medname='" + s1 + "' and hospid='"+ hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    cstock=0
    for row in records:
        cstock=row[2]


    l=[]
    s="select medname from pharmacymed"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        l.append(row[0])
    return render(request,"medstockentry3.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'cstock':cstock,'s1':s1,'s2':s2,'l':l,'medtype':medtype,'company':company,'content':content,'medunit':medunit,'cstock':cstock})

def meddamage1(request):
    con = connect()
    cursor = con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #-----
    l = []
    s = "select medname from pharmacymed"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        l.append(row[0])
    return render(request, "meddamage1.html", {'l': l,'aa':aa,'bb':bb,'cc':cc,'dd':dd})


def meddamage2(request):
    con = connect()
    cursor = con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #----
    s1 = request.POST["c1"]
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        hospid = row[1]

    s = "select * from pharmacymed where medname='" + s1 + "'"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        medtype = row[1]
        company = row[2]
        content = row[3]
        medunit = row[4]
    s = "select * from medstock where medname='" + s1 + "' and hospid='" + hospid + "'"

    cursor.execute(s)
    records = cursor.fetchall()
    cstock = 0
    for row in records:
        cstock = row[2]

    l = []
    s = "select medname from pharmacymed"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        l.append(row[0])
    return render(request, "meddamage2.html",
                  {'aa':aa,'bb':bb,'cc':cc,'dd':dd
,'cstock': cstock, 's1': s1, 'l': l, 'medtype': medtype, 'company': company, 'content': content,
                   'medunit': medunit, 'cstock': cstock})


def meddamage3(request):
    con = connect()
    cursor = con.cursor()
    #----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa=""
    bb=""
    cc=""
    dd=""
    if desig=="Pharmacist":
        aa="yes"
    elif desig=="Dr":
        bb="yes"
    elif desig=="Office Staff":
        cc="yes"
    elif desig=="Lab Staff":
        dd="yes"

    #----
    s1 = request.POST["c1"]
    s2 = request.POST["t1"]
    s3 = request.POST["t2"]
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid=row[0]
        hospid = row[1]
    dno = 0
    s = "select * from meddamage order by dno desc"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        dno = row[0]
        break
    dno = dno + 1
    edate = ccdate()
    s = "insert into meddamage values(" + str(dno) + ",'" + s1 + "','" + hospid + "'," + s2 + ",'"  + s3 + "','"  + staffid + "','" + edate + "')"
    cursor.execute(s)
    con.commit()
    s = "update medstock set cstock=cstock- " + s2 + " where medname='" + s1 + "' and hospid='" + hospid + "'"
    cursor.execute(s)
    con.commit()


    s = "select * from pharmacymed where medname='" + s1 + "'"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        medtype = row[1]
        company = row[2]
        content = row[3]
        medunit = row[4]
    s = "select * from medstock where medname='" + s1 + "' and hospid='" + hospid + "'"

    cursor.execute(s)
    records = cursor.fetchall()
    cstock = 0
    for row in records:
        cstock = row[2]

    l = []
    s = "select medname from pharmacymed"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        l.append(row[0])
    return render(request, "meddamage3.html",
                  {'aa':aa,'bb':bb,'cc':cc,'dd':dd,'cstock': cstock, 's1': s1,'s2':s2,'s3':s3, 'l': l, 'medtype': medtype, 'company': company, 'content': content,
                   'medunit': medunit, 'cstock': cstock})


def medstocklist(request):
    con = connect()
    cursor = con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #----
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        s1=row[1]


    s="select medname,cstock from medstock  where hospid='"+s1 + "'"
    cursor.execute(s)
    records1=cursor.fetchall()


    s="select * from hospital where hospid='" + s1 +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location=row[1]
        place=row[2]
        pin=row[3]
        phone=row[4]
        district=row[5]
        email=row[6]
        htype=row[7]
        nbed=row[9]

    return render(request, "medstocklist.html", {'aa':aa,'bb':bb,'cc':cc,'dd':dd,'s1':s1,'records1':records1,'location':location,'place':place,'pin':pin,'phone':phone,'district':district,'email':email,'htype':htype,'nbed':nbed})




def meddamagelist(request):
    con = connect()
    cursor = con.cursor()
    #----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #------
    s="select * from session "
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        s1=row[1]

    s="select dno,medname,dqty,reason,staffid,ddate from meddamage  where hospid='"+s1 + "'"
    cursor.execute(s)
    records1=cursor.fetchall()
    l = []
    s = "select hospid from hospital"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        l.append(row[0])


    s="select * from hospital where hospid='" + s1 +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location=row[1]
        place=row[2]
        pin=row[3]
        phone=row[4]
        district=row[5]
        email=row[6]
        htype=row[7]
        nbed=row[9]

    return render(request, "meddamagelist.html", {'aa':aa,'bb':bb,'cc':cc,'dd':dd,'l': l,'s1':s1,'records1':records1,'location':location,'place':place,'pin':pin,'phone':phone,'district':district,'email':email,'htype':htype,'nbed':nbed})

def opdaysreg1(request):
    con=connect()
    cursor=con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #-----
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
        hospid=row[1]
    s="select opday,ftime,duration,npatient from dropdays where staffid='" + staffid +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    return  render(request,"opdaysreg1.html",{'records':records,'aa':aa,'bb':bb,'cc':cc,'dd':dd})

def opdaysreg2(request):
    con=connect()
    cursor=con.cursor()
    #----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #----
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    s3 = request.POST["t3"]
    s4 = request.POST["t4"]
    s5 = request.POST["t5"]
    s6 = request.POST["t6"]
    s7 = request.POST["t7"]
    ftime=s2 + ":"+s3 +":"+s4
    duration=s5+"-"+s6

    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
        hospid=row[1]
    s="select * from dropdays where staffid='"+ staffid + "' and opday='"+ s1 + "'"
    cursor.execute(s)
    if cursor.rowcount==0:
        s="insert into dropdays values('" + staffid + "','" + s1 + "','"+ ftime + "','" + duration + "','" + s7 +   "')"
        msg="Stored"
    else:
        s="update dropdays set ftime='" + ftime + "',duration='"+ duration + "',npatient='"+ s7 +"' where staffid='"+ staffid + "' and opday='" + s1   +"'"
        msg="Updated"
    cursor.execute(s)
    con.commit()

    s="select opday,ftime,duration,npatient from dropdays where staffid='" + staffid +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    return  render(request,"opdaysreg2.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd ,'msg':msg,'records':records,'s1':s1,'ftime':ftime,'duration':duration,'s7': s7})

def opbooking1(request):
    con = connect()
    cursor = con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    return render(request,"opbooking1.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd})

def opbooking2(request):
    con=connect()
    cursor=con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    s0=request.POST["t0"]
    hospid=""
    name=""
    hname=""
    place=""
    pin=""
    ph=""
    district=""
    gender=""
    age=""
    adharno=""
    regdate=""
    hospid=""
    s="select * from patient where pid='" + s0 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
        adharno = row[9]
        regdate=row[10]
        hospid = row[13]
    location1=""
    place1=""
    pin1=""
    phone1=""
    district1=""
    email1=""
    htype1=""
    s="select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location1=row[1]
        place1 = row[2]
        pin1 = row[3]
        phone1 = row[4]
        district1 = row[5]
        email1 = row[6]
        htype1 = row[7]

    return render(request,"opbooking2.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'records':records,'s0':s0,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})

def sopbook1(request):
    con = connect()
    cursor = con.cursor()
    #----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #-----
    s0=request.POST["t0"]
    s = "select distinct(spl) from staff where spl is not null"
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])
    return render(request,"sopbook1.html",{'l':l,'s0':s0,'aa':aa,'bb':bb,'cc':cc,'dd':dd })

def sopbook2(request):
    con = connect()
    cursor = con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa=""
    bb=""
    cc=""
    dd=""
    if desig=="Pharmacist":
        aa="yes"
    elif desig=="Dr":
        bb="yes"
    elif desig=="Office Staff":
        cc="yes"
    elif desig=="Lab Staff":
        dd="yes"

    #------
    s0 = request.POST["t0"]
    s1=request.POST["c1"]
    s = "select distinct(spl) from staff where spl is not null"
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])

    s = "select staffid,name,gender,qualification from staff where spl='" + s1 + "'"
    cursor.execute(s)
    records = cursor.fetchall()

    return render(request,"sopbook2.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'s0':s0,'s1':s1,'l':l,'records':records})

def sopbook3(request):
    con = connect()
    cursor = con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #----
    s0 = request.POST["t0"]
    s1=request.POST["t1"]
    s="select * from staff where staffid='"+ s1 +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname=row[2]
        place=row[3]
        pin=row[4]
        ph=row[5]
        gender=row[6]
        specialization=row[7]
    s="select * from staffhospital where staffid='"+ s1 + "' order by wno desc"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[2]
    s = "select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        location = row[1]
        place = row[2]
        pin = row[3]
        phone = row[4]
        district = row[5]
        email = row[6]
        htype = row[7]

    s="select opday,ftime,duration,npatient from dropdays where staffid='"+ s1  +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request, "sopbook3.html", {'aa':aa,'bb':bb,'cc':cc,'dd':dd,'records':records,'s0':s0,'s1':s1,'name': name, 'hname': hname,'place':place,'pin':pin,'ph':ph,'gender':gender,'specialization':specialization, 'hospid':hospid,'location':location,'place':place,'pin':pin,'phone':phone,'district':district,'email':email,'htype':htype})

def sopbook4(request):
    con = connect()
    cursor = con.cursor()
    #----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #----
    s0 = request.POST["t0"]
    s1=request.POST["t1"]
    s2=request.POST["d1"]
    pid=s0

    datetime_str = s2
    d2 = datetime.strptime(datetime_str, '%Y-%m-%d')
    ddd = d2.strftime("%A")
    s="select * from staff where staffid='"+ s1 +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname=row[2]
        place=row[3]
        pin=row[4]
        ph=row[5]
        gender=row[6]
        specialization=row[7]
    s="select * from staffhospital where staffid='"+ s1 + "' order by wno desc"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[2]
    s = "select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        location = row[1]
        place = row[2]
        pin = row[3]
        phone = row[4]
        district = row[5]
        email = row[6]
        htype = row[7]
    s="select opday,ftime,duration,npatient from dropdays where staffid='"+ s1  +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    ff = "No"
    for row in records:
        if row[0] == ddd:
            ff = "ok"
    if ff == "No":
        msg="No Consultation for the selected date..."
        return render(request, "sopbook44.html",
                      {'aa':aa,'bb':bb,'cc':cc,'dd':dd,'msg':msg,'records': records, 's0':s0, 's1': s1,'s2': s2, 'name': name, 'hname': hname, 'place': place, 'pin': pin, 'ph': ph,
                       'gender': gender, 'specialization': specialization, 'hospid': hospid, 'location': location,
                       'place': place, 'pin': pin, 'phone': phone, 'district': district, 'email': email,
                       'htype': htype})
    s = "select * from opbooking where bdate='" + str(d2) + "' and drid='" + s1 + "' and bno not in (select bno from opcancel)"
    cursor.execute(s)
    records1 = cursor.fetchall()
    n = 0
    for row in records1:
        n = n + 1
    s = "select * from dropdays where staffid='" + s1 + "' and opday='" + ddd + "'"
    cursor.execute(s)
    records1 = cursor.fetchall()
    tot = 0
    for row in records1:
        tot = row[4]
    avail = "No"
    if int(n) < int(tot):
        avail = "yes"
    if avail == "No":
        msg = "Full only " + str(tot) + " patients are alloted for the selected day"
        return render(request, "sopbook44.html",
                      {'aa':aa,'bb':bb,'cc':cc,'dd':dd,'msg':msg,'records': records,'s0':s0, 's1': s1,'s2': s2, 'name': name, 'hname': hname, 'place': place, 'pin': pin, 'ph': ph,
                       'gender': gender, 'specialization': specialization, 'hospid': hospid, 'location': location,
                       'place': place, 'pin': pin, 'phone': phone, 'district': district, 'email': email,
                       'htype': htype})
    s = "select * from opbooking where pid='" + pid + "' and drid='" + s1 + "' and bdate='" + s2 + "' and bno not in( select bno from opcancel)"
    cursor.execute(s)
    records1 = cursor.fetchall()
    tno = 0
    bno = 0
    for row in records1:
        bno = row[0]
        tno = row[3]

    if cursor.rowcount > 0:
        msg = "You are already booked the same doctor  @ same date...The Token No is " + str(tno) + " and the booking No. " + str(bno)
        return render(request, "sopbook44.html",
                      {'aa':aa,'bb':bb,'cc':cc,'dd':dd,'msg': msg, 'records': records,'s0':s0, 's1': s1,'s2': s2, 'name': name, 'hname': hname, 'place': place,
                       'pin': pin, 'ph': ph,
                       'gender': gender, 'specialization': specialization, 'hospid': hospid, 'location': location,
                       'place': place, 'pin': pin, 'phone': phone, 'district': district, 'email': email,
                       'htype': htype})
    s = "select * from opbooking where drid='" + s1 + "' and bdate='" + s2 + "' and bno not in( select bno from opcancel)"
    cursor.execute(s)
    records1 = cursor.fetchall()
    tno = 0
    for row in records1:

        tno = row[3]

    hospid = ""
    name1 = ""
    hname1 = ""
    place1 = ""
    pin1 = ""
    ph1 = ""
    district1 = ""
    gender1 = ""
    age1 = ""
    adharno1 = ""
    regdate1 = ""
    hospid1 = ""
    s = "select * from patient where pid='" + s0 + "'"
    cursor.execute(s)
    records1 = cursor.fetchall()
    for row in records1:
        name1 = row[1]
        hname1 = row[2]
        place1 = row[3]
        pin1 = row[4]
        ph1 = row[5]
        district1 = row[6]
        gender1 = row[7]
        age1 = row[8]
        adharno1 = row[9]
        regdate1 = row[10]
        hospid1 = row[13]

    return render(request, "sopbook4.html", {'aa':aa,'bb':bb,'cc':cc,'dd':dd,'tno':tno,'records':records,'s0':s0,'s1':s1,'s2': s2,'name': name, 'hname': hname,'place':place,'pin':pin,'ph':ph,'gender':gender,'specialization':specialization, 'hospid':hospid,'location':location,'place':place,'pin':pin,'phone':phone,'district':district,'email':email,'htype':htype,'name1':name1,'hname1':hname1,'place1':place1,'pin1':pin1,'ph1':ph1,'district1':district1,'gender1':gender1,'age1':age1,'adharno1':adharno1,'regdate1':regdate1,'hospid1':hospid1})


def sopbook5(request):
    con = connect()
    cursor = con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #----
    s0 = request.POST["t0"]
    s1=request.POST["t1"]
    s2=request.POST["d1"]
    pid=s0

    datetime_str = s2

    d2 = datetime.strptime(datetime_str, '%Y-%m-%d')

    ddd = d2.strftime("%A")



    s="select * from staff where staffid='"+ s1 +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname=row[2]
        place=row[3]
        pin=row[4]
        ph=row[5]
        gender=row[6]
        specialization=row[7]
    s="select * from staffhospital where staffid='"+ s1 + "' order by wno desc"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[2]
    s = "select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        location = row[1]
        place = row[2]
        pin = row[3]
        phone = row[4]
        district = row[5]
        email = row[6]
        htype = row[7]
    s="select opday,ftime,duration,npatient from dropdays where staffid='"+ s1  +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    s = "select * from opbooking where pid='" + pid + "' and drid='" + s1 + "' and bdate='" + s2 + "' and bno not in( select bno from opcancel)"
    cursor.execute(s)
    records1 = cursor.fetchall()
    tno = 0
    bno = 0
    for row in records1:
        bno = row[0]
        tno = row[3]
    if cursor.rowcount > 0:
        msg = "You are already booked the same doctor  @ same date...The Token No is " + str(
            tno) + " and the booking No. " + str(bno)
        return render(request, "sopbook44.html",
                      {'aa':aa,'bb':bb,'cc':cc,'dd':dd,'msg': msg, 'records': records,'s0':s0, 's1': s1, 's2': s2, 'name': name, 'hname': hname, 'place': place,
                       'pin': pin, 'ph': ph,
                       'gender': gender, 'specialization': specialization, 'hospid': hospid, 'location': location,
                       'place': place, 'pin': pin, 'phone': phone, 'district': district, 'email': email,
                       'htype': htype})

    s = "select * from opbooking where  drid='" + s1 + "' and bdate='" + s2 + "' and bno not in( select bno from opcancel) order by tno desc"
    cursor.execute(s)
    records1 = cursor.fetchall()
    tno = 0

    for row in records1:
        tno = row[3]
    tno=tno+1
    bno=0
    s="select * from opbooking order by bno desc"
    cursor.execute(s)
    records1=cursor.fetchall()
    for row in records1:
        bno=row[0]
        break
    bno=bno+1
    cdate=ccdate()

    s="select * from session "
    cursor.execute(s)
    records1=cursor.fetchall()
    for row in records1:
        staffid=row[0]
    s="insert into opbooking(bno,drid,bdate,tno,pid,cdate,staffid,hospid) values("+ str(bno) + ",'" + s1 + "','"+ s2 + "',"+ str(tno) +",'"+ pid + "','"+ cdate + "','" + staffid + "','"  + hospid +  "')"

    cursor.execute(s)
    con.commit()

    hospid = ""
    name1 = ""
    hname1 = ""
    place1 = ""
    pin1 = ""
    ph1 = ""
    district1 = ""
    gender1 = ""
    age1 = ""
    adharno1 = ""
    regdate1 = ""
    hospid1 = ""
    s = "select * from patient where pid='" + s0 + "'"
    cursor.execute(s)
    records1 = cursor.fetchall()
    for row in records1:
        name1 = row[1]
        hname1 = row[2]
        place1 = row[3]
        pin1 = row[4]
        ph1 = row[5]
        district1 = row[6]
        gender1 = row[7]
        age1 = row[8]
        adharno1 = row[9]
        regdate1 = row[10]
        hospid1 = row[13]

    return render(request, "sopbook5.html", {'aa':aa,'bb':bb,'cc':cc,'dd':dd,'bno':bno,'tno':tno,'records':records,'s0':s0,'s1':s1,'s2': s2,'name': name, 'hname': hname,'place':place,'pin':pin,'ph':ph,'gender':gender,'specialization':specialization, 'hospid':hospid,'location':location,'place':place,'pin':pin,'phone':phone,'district':district,'email':email,'htype':htype,'name1':name1,'hname1':hname1,'place1':place1,'pin1':pin1,'ph1':ph1,'district1':district1,'gender1':gender1,'age1':age1,'adharno1':adharno1,'regdate1':regdate1,'hospid1':hospid1})


def opcancellation1(request):
    con = connect()
    cursor = con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    return render(request,"opcancellation1.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd})

def opcancellation2(request):
    con=connect()
    cursor=con.cursor()
    #----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #-----

    s0=request.POST["t0"]
    hospid=""
    name=""
    hname=""
    place=""
    pin=""
    ph=""
    district=""
    gender=""
    age=""
    adharno=""
    regdate=""
    hospid=""
    s="select * from patient where pid='" + s0 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
        adharno = row[9]
        regdate=row[10]
        hospid = row[13]
    location1=""
    place1=""
    pin1=""
    phone1=""
    district1=""
    email1=""
    htype1=""
    s="select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location1=row[1]
        place1 = row[2]
        pin1 = row[3]
        phone1 = row[4]
        district1 = row[5]
        email1 = row[6]
        htype1 = row[7]

    return render(request,"opcancellation2.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'records':records,'s0':s0,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})


def sopcancel1(request):
    con=connect()
    cursor=con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #-----
    s0=request.POST["t0"]
    pid=s0

    bdate=ccdate()
    s="select bno,drid,bdate,tno from opbooking where pid='"+ pid +"' and bdate>'"+ bdate +"' and bno not in(select bno from opcancel)"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"sopcancel1.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd ,'records':records,'s0':s0})

def sopcancel2(request):
    con=connect()
    cursor=con.cursor()
    #--------------
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #---------------------
    s0=request.POST["t0"]
    s1=request.POST["t1"]
    s="select * from opbooking where bno=" + s1
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        drid=row[1]
        bdate1=row[2]
        tno=row[3]
        cdate=row[5]
        staffid=row[6]
    s="select * from staff where staffid='"+ drid +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        sname=row[1]
        qualification=row[8]
        specialization=row[7]

    pid=s0
    bdate=ccdate()
    s="select bno,drid,bdate,tno from opbooking where pid='"+ pid +"' and bdate>'"+ bdate +"' and bno not in(select bno from opcancel)"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"sopcancel2.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'records':records,'s0':s0,'s1':s1,'drid':drid,'bdate1':bdate1,'tno':tno,'cdate':cdate,'staffid':staffid,'sname':sname,'qualification':qualification,'specialization':specialization})

def sopcancel3(request):
    con=connect()
    cursor=con.cursor()
    #----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #-----
    s1=request.POST["t1"]
    s0=request.POST["t0"]
    s="select * from opbooking where bno=" + s1
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        drid=row[1]
        bdate1=row[2]
        tno=row[3]
        cdate=row[5]
        staffid=row[6]
    s="select * from staff where staffid='"+ drid +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        sname=row[1]
        qualification=row[8]
        specialization=row[7]

    pid=s0
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    staffid=""
    for row in records:
        staffid=row[0]
    bdate=ccdate()
    s="insert into opcancel (bno,cdate,staffid) values("+ s1 + ",'" + bdate +"','" + staffid +  "')"
    cursor.execute(s)
    con.commit()

    s="select bno,drid,bdate,tno from opbooking where pid='"+ pid +"' and bdate>'"+ bdate +"' and bno not in(select bno from opcancel)"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"sopcancel3.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'records':records,'s0':s0,'s1':s1,'drid':drid,'bdate1':bdate1,'tno':tno,'cdate':cdate,'staffid':staffid,'sname':sname,'qualification':qualification,'specialization':specialization})

def drcomingbooking(request):
    con=connect()
    cursor=con.cursor()
    #-----------
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #----------
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
    bdate=ccdate()
    s="select a.bno,a.bdate,a.tno,a.pid,b.name,b.hname,b.place,b.ph,b.district,b.gender,b.age from opbooking a,patient b where a.pid=b.pid and a.bno  not in (select bno from opcancel) and a.bdate>='"+ bdate + "' and a.drid='" + staffid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"drcomingbooking.html",{'records':records,'aa':aa,'bb':bb,'cc':cc,'dd':dd})

def drprevbooking(request):
    con=connect()
    cursor=con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #-----
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
    bdate=ccdate()
    s="select a.bno,a.bdate,a.tno,a.pid,b.name,b.hname,b.place,b.ph,b.district,b.gender,b.age from opbooking a,patient b where a.pid=b.pid and a.bno  not in (select bno from opcancel) and a.bdate<'"+ bdate + "' and a.drid='" + staffid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"drprevbooking.html",{'records':records,'aa':aa,'bb':bb,'cc':cc,'dd':dd})


def drcomingcbooking(request):
    con=connect()
    cursor=con.cursor()
    #------
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #------
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
    bdate=ccdate()
    s="select a.bno,a.bdate,a.tno,a.pid,b.name,b.hname,b.place,b.ph,b.district,b.gender,b.age from opbooking a,patient b where a.pid=b.pid and a.bno   in (select bno from opcancel) and a.bdate>='"+ bdate + "' and a.drid='" + staffid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"drcomingcbooking.html",{'records':records,'aa':aa,'bb':bb,'cc':cc,'dd':dd})

def drprevcbooking(request):
    con=connect()
    cursor=con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #-----
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
    bdate=ccdate()
    s="select a.bno,a.bdate,a.tno,a.pid,b.name,b.hname,b.place,b.ph,b.district,b.gender,b.age from opbooking a,patient b where a.pid=b.pid and a.bno   in (select bno from opcancel) and a.bdate<'"+ bdate + "' and a.drid='" + staffid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"drprevcbooking.html",{'records':records,'aa':aa,'bb':bb,'cc':cc,'dd':dd})

def casesheetentry1(request):
    # coming and previous booked
    # if it is live work dr. should enter only that date
    con=connect()
    cursor=con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #-----
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
    bdate=ccdate()
    s="select a.bno,a.bdate,a.tno,a.pid,b.name,b.hname,b.place,b.ph,b.district,b.gender,b.age from opbooking a,patient b where a.pid=b.pid and a.bno  not in (select bno from opcancel) and a.drid='" + staffid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"casesheetentry1.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'records':records})


def casesheetentry2(request):
    con=connect()
    cursor=con.cursor()
    #--------------
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #------------
    s1=request.POST["t1"]
    s="select * from opbooking where bno="+ s1
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        bdate=row[2]
        tno=row[3]
        pid=row[4]
        cdate=row[5]
        staffid=row[6]
        hospid=row[7]

    s="select * from patient where pid='"+ pid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
    s="select eno,problem,prescription,drcomment,drid,bno,edate from casesheet where pid='"+ pid  +"'"
    cursor.execute(s)
    records1=cursor.fetchall()
    return render(request,"casesheetentry2.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'records1':records1,'s1':s1,'bdate':bdate,'tno':tno,'pid':pid,'cdate':cdate,'staffid':staffid,'hospid':hospid,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age})


def casesheetentry3(request):
    con=connect()
    cursor=con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #-----
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    s3 = request.POST["t3"]
    s4 = request.POST["t4"]

    s="select * from opbooking where bno="+ s1
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        bdate=row[2]
        tno=row[3]
        pid=row[4]
        cdate=row[5]
        staffid=row[6]
        hospid=row[7]

    s="select * from patient where pid='"+ pid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
    eno = 0
    s = "select * from casesheet where pid='" + pid +  "' order by eno desc"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        eno=row[1]
        break
    eno =eno+1
    edate=ccdate()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        drid=row[0]
    edate=ccdate()

    s="insert into casesheet values('" + pid + "',"+ str(eno) + ",'"+ s2 + "','" + s3 + "','"+ s4 +  "','" + drid + "',"+ str(s1) + ",'"+ edate + "')"
    cursor.execute(s)
    con.commit()
    msg="Entry successs...The entry No. is  " + str(eno)
    s="select eno,problem,prescription,drcomment,drid,bno,edate from casesheet where pid='"+ pid  +"'"
    cursor.execute(s)
    records1=cursor.fetchall()
    return render(request,"casesheetentry3.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'msg':msg,'records1':records1,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'bdate':bdate,'tno':tno,'pid':pid,'cdate':cdate,'staffid':staffid,'hospid':hospid,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age})

def casesheet1(request):
    con = connect()
    cursor = con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    return render(request,"casesheet1.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd})

def casesheet2(request):
    con=connect()
    cursor=con.cursor()
    #-------
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #--------
    s0=request.POST["t0"]
    hospid=""
    name=""
    hname=""
    place=""
    pin=""
    ph=""
    district=""
    gender=""
    age=""
    adharno=""
    regdate=""
    hospid=""
    s="select * from patient where pid='" + s0 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
        adharno = row[9]
        regdate=row[10]
        hospid = row[13]
    location1=""
    place1=""
    pin1=""
    phone1=""
    district1=""
    email1=""
    htype1=""
    s="select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location1=row[1]
        place1 = row[2]
        pin1 = row[3]
        phone1 = row[4]
        district1 = row[5]
        email1 = row[6]
        htype1 = row[7]
    s = "select eno,problem,prescription,drcomment,drid,bno,edate from casesheet where pid='" + s0 + "'"
    cursor.execute(s)
    records1 = cursor.fetchall()

    return render(request,"casesheet2.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'records1':records1,'records':records,'s0':s0,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})

def labtestentry1(request):
    con = connect()
    cursor = con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    return render(request,"labtestentry1.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd})

def labtestentry2(request):
    con=connect()
    cursor=con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #------
    s="delete from temp"
    cursor.execute(s)
    con.commit()
    s0=request.POST["t0"]
    hospid=""
    name=""
    hname=""
    place=""
    pin=""
    ph=""
    district=""
    gender=""
    age=""
    adharno=""
    regdate=""
    hospid=""
    s="select * from patient where pid='" + s0 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
        adharno = row[9]
        regdate=row[10]
        hospid = row[13]
    location1=""
    place1=""
    pin1=""
    phone1=""
    district1=""
    email1=""
    htype1=""
    s="select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location1=row[1]
        place1 = row[2]
        pin1 = row[3]
        phone1 = row[4]
        district1 = row[5]
        email1 = row[6]
        htype1 = row[7]
    s="select * from session "
    cursor.execute(s)
    records11=cursor.fetchall()
    for row in records11:
        hid=row[1]
    s="select tname,ttype,tcontent from labmaster where tname in (select tname from hosplab where hospid='"+ hid +"')"
    cursor.execute(s)
    records1=cursor.fetchall()
    s = "select eno,drcomment,drid,edate from casesheet where pid='" + s0 + "'"
    cursor.execute(s)
    records2 = cursor.fetchall()
    return render(request,"labtestentry2.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd ,'records2':records2,'records1':records1,'records':records,'s0':s0,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})


def labtestentry3(request):
    con=connect()
    cursor=con.cursor()
    #-------------
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #-----------
    s0=request.POST["t0"]
    s1 = request.POST["t1"]
    s="select * from temp where tname='"+ s1 +"'"
    cursor.execute(s)
    if cursor.rowcount==0:
        s="select * from temp order by itemno desc"
        cursor.execute(s)
        records=cursor.fetchall()
        itemno=0
        for row in records:
            itemno=row[0]
            break
        itemno=itemno+1
        s="insert into temp values("+ str(itemno) + ",'" + s1 + "')"
        cursor.execute(s)
        con.commit()

    hospid=""
    name=""
    hname=""
    place=""
    pin=""
    ph=""
    district=""
    gender=""
    age=""
    adharno=""
    regdate=""
    hospid=""
    s="select * from patient where pid='" + s0 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
        adharno = row[9]
        regdate=row[10]
        hospid = row[13]
    location1=""
    place1=""
    pin1=""
    phone1=""
    district1=""
    email1=""
    htype1=""
    s="select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location1=row[1]
        place1 = row[2]
        pin1 = row[3]
        phone1 = row[4]
        district1 = row[5]
        email1 = row[6]
        htype1 = row[7]
    s="select * from session "
    cursor.execute(s)
    records11=cursor.fetchall()
    for row in records11:
        hid=row[1]
    s="select tname,ttype,tcontent from labmaster where tname in (select tname from hosplab where hospid='"+ hid +"')"

    cursor.execute(s)
    records1=cursor.fetchall()
    s="select itemno,tname from temp order by itemno"
    cursor.execute(s)
    records2=cursor.fetchall()

    s = "select eno,drcomment,drid,edate from casesheet where pid='" + s0 + "'"
    cursor.execute(s)
    records22 = cursor.fetchall()
    return render(request,"labtestentry3.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'records22':records22,'records2':records2,'records1':records1,'records':records,'s0':s0,'s1':s1,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})

def labtestentry33(request):
    con=connect()
    cursor=con.cursor()
    #------------
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #--------
    s0=request.POST["t0"]
    s1 = request.POST["t1"]
    s2=request.POST["t2"]

    s="delete from temp where itemno=" + s2
    cursor.execute(s)
    con.commit()
    s="update temp set itemno=itemno-1  where itemno>" + s2
    cursor.execute(s)
    con.commit()
    hospid=""
    name=""
    hname=""
    place=""
    pin=""
    ph=""
    district=""
    gender=""
    age=""
    adharno=""
    regdate=""
    hospid=""
    s="select * from patient where pid='" + s0 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
        adharno = row[9]
        regdate=row[10]
        hospid = row[13]
    location1=""
    place1=""
    pin1=""
    phone1=""
    district1=""
    email1=""
    htype1=""
    s="select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location1=row[1]
        place1 = row[2]
        pin1 = row[3]
        phone1 = row[4]
        district1 = row[5]
        email1 = row[6]
        htype1 = row[7]
    s="select * from session "
    cursor.execute(s)
    records11=cursor.fetchall()
    for row in records11:
        hid=row[1]
    s="select tname,ttype,tcontent from labmaster where tname in (select tname from hosplab where hospid='"+ hid +"')"

    cursor.execute(s)
    records1=cursor.fetchall()
    s="select itemno,tname from temp order by itemno"
    cursor.execute(s)
    records2=cursor.fetchall()

    s = "select eno,drcomment,drid,edate from casesheet where pid='" + s0 + "'"
    cursor.execute(s)
    records22 = cursor.fetchall()

    return render(request,"labtestentry33.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'records22':records22,'records2':records2,'records1':records1,'records':records,'s0':s0,'s1':s1,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})


def labtestentry4(request):
    con=connect()
    cursor=con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa=""
    bb=""
    cc=""
    dd=""
    if desig=="Pharmacist":
        aa="yes"
    elif desig=="Dr":
        bb="yes"
    elif desig=="Office Staff":
        cc="yes"
    elif desig=="Lab Staff":
        dd="yes"

    #------
    s0=request.POST["t0"]

    hospid=""
    name=""
    hname=""
    place=""
    pin=""
    ph=""
    district=""
    gender=""
    age=""
    adharno=""
    regdate=""
    hospid=""
    s="select * from patient where pid='" + s0 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
        adharno = row[9]
        regdate=row[10]
        hospid = row[13]
    location1=""
    place1=""
    pin1=""
    phone1=""
    district1=""
    email1=""
    htype1=""
    s="select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location1=row[1]
        place1 = row[2]
        pin1 = row[3]
        phone1 = row[4]
        district1 = row[5]
        email1 = row[6]
        htype1 = row[7]
    s="select * from session "
    cursor.execute(s)
    records11=cursor.fetchall()
    for row in records11:
        hid=row[1]
    s="select tname,ttype,tcontent from labmaster where tname in (select tname from hosplab where hospid='"+ hid +"')"

    cursor.execute(s)
    records1=cursor.fetchall()
    s="select itemno,tname from temp order by itemno"
    cursor.execute(s)
    records2=cursor.fetchall()
    ltestno=0
    s="select * from labtestmaster order by ltestno desc "
    cursor.execute(s)
    records3=cursor.fetchall()
    for row in records3:
        ltestno=row[0]
        break
    ltestno=ltestno+1
    s="select * from session "
    cursor.execute(s)
    records3=cursor.fetchall()
    for row in records3:
        staffid=row[0]
        hid=row[1]
    edate=ccdate()
    s="insert into labtestmaster values("+ str(ltestno) + ",'" + s0 + "','" + hid + "','"+ staffid + "','"+ edate + "')"
    cursor.execute(s)
    con.commit()
    s="select * from temp"
    cursor.execute(s)
    records3=cursor.fetchall()
    for row in records3:
        s="insert into labtestitems values(" + str(ltestno) + ",'" + row [1] + "')"
        cursor.execute(s)
        con.commit()


    return render(request,"labtestentry4.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'ltestno':ltestno,'records2':records2,'records1':records1,'records':records,'s0':s0,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})

def labtestrentry1(request):
    con = connect()
    cursor = con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #-----
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
        hospid=row[1]
    s="select ltestno,pid,staffid,edate from labtestmaster where hospid='"+ hospid +  "' and ltestno not in (select ltestno from labtestresult)"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"labtestrentry1.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'records':records})

def labtestrentry2(request):
    con = connect()
    cursor = con.cursor()
    #------
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #------
    s1=request.POST["t1"]
    s="select * from labtestmaster where ltestno="+ s1
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        pid=row[1]
        hospid=row[2]
        staffid=row[3]
        edate=row[4]

    s="select * from patient where pid='"+ pid +  "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]

    s="select tname from labtestitems where ltestno="+ s1
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])


    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
        hospid=row[1]
    s="select ltestno,pid,staffid,edate from labtestmaster where hospid='"+ hospid +  "' and ltestno not in (select ltestno from labtestresult)"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"labtestrentry2.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'s1':s1,'l':l,'records':records,'pid':pid,'hospid':hospid,'staffid':staffid,'edate':edate,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age})



def labtestrentry3(request):
    con = connect()
    cursor = con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa=""
    bb=""
    cc=""
    dd=""
    if desig=="Pharmacist":
        aa="yes"
    elif desig=="Dr":
        bb="yes"
    elif desig=="Office Staff":
        cc="yes"
    elif desig=="Lab Staff":
        dd="yes"


    #------
    s1=request.POST["t1"]
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()

    for row in records:
        staffid=row[0]

    file = request.FILES['file']
    fs = FileSystemStorage()
    filename = fs.save("./labresult/" + file.name, file)
    filename = filename[12:]
    rdate=ccdate()
    s="insert into labtestresult values("+ s1 + ",'"+ filename +"','"+ staffid + "','"+ rdate +  "')"
    cursor.execute(s)
    con.commit()

    s="select * from labtestmaster where ltestno="+ s1
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        pid=row[1]
        hospid=row[2]
        staffid=row[3]
        edate=row[4]

    s="select * from patient where pid='"+ pid +  "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]

    s="select tname from labtestitems where ltestno="+ s1
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])


    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
        hospid=row[1]
    s="select ltestno,pid,staffid,edate from labtestmaster where hospid='"+ hospid +  "' and ltestno not in (select ltestno from labtestresult)"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"labtestrentry3.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'s1':s1,'l':l,'records':records,'pid':pid,'hospid':hospid,'staffid':staffid,'edate':edate,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age})

def labtestresult1(request):
    con = connect()
    cursor = con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    return render(request,"labtestresult1.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd})

def labtestresult2(request):
    con=connect()
    cursor=con.cursor()
    #------------
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #-----------
    s="delete from temp"
    cursor.execute(s)
    con.commit()
    s0=request.POST["t0"]
    hospid=""
    name=""
    hname=""
    place=""
    pin=""
    ph=""
    district=""
    gender=""
    age=""
    adharno=""
    regdate=""
    hospid=""
    s="select * from patient where pid='" + s0 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
        adharno = row[9]
        regdate=row[10]
        hospid = row[13]
    location1=""
    place1=""
    pin1=""
    phone1=""
    district1=""
    email1=""
    htype1=""
    s="select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location1=row[1]
        place1 = row[2]
        pin1 = row[3]
        phone1 = row[4]
        district1 = row[5]
        email1 = row[6]
        htype1 = row[7]
    s="select * from session "
    cursor.execute(s)
    records11=cursor.fetchall()
    for row in records11:
        hid=row[1]
    #s="select tname,ttype,tcontent from labmaster where tname in (select tname from hosplab where hospid='"+ hid +"')"
    s = "select ltestno,hospid,edate from labtestmaster where pid='" + s0 + "' and ltestno in(select ltestno from labtestresult)"


    cursor.execute(s)
    records1=cursor.fetchall()
    s = "select ltestno,hospid,edate from labtestmaster where pid='" + s0 + "'"
    cursor.execute(s)
    records2 = cursor.fetchall()
    return render(request,"labtestresult2.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'records2':records2,'records1':records1,'records':records,'s0':s0,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})

def labtestresult3(request):
    con=connect()
    cursor=con.cursor()
    #------
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #-------

    s0=request.POST["t0"]
    s1 = request.POST["t1"]
    hospid=""
    name=""
    hname=""
    place=""
    pin=""
    ph=""
    district=""
    gender=""
    age=""
    adharno=""
    regdate=""
    hospid=""
    s="select * from patient where pid='" + s0 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
        adharno = row[9]
        regdate=row[10]
        hospid = row[13]
    location1=""
    place1=""
    pin1=""
    phone1=""
    district1=""
    email1=""
    htype1=""
    s="select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location1=row[1]
        place1 = row[2]
        pin1 = row[3]
        phone1 = row[4]
        district1 = row[5]
        email1 = row[6]
        htype1 = row[7]
    s="select * from session "
    cursor.execute(s)
    records11=cursor.fetchall()
    for row in records11:
        hid=row[1]
    #s="select tname,ttype,tcontent from labmaster where tname in (select tname from hosplab where hospid='"+ hid +"')"
    s = "select ltestno,hospid,edate from labtestmaster where pid='" + s0 + "' and ltestno in(select ltestno from labtestresult)"


    cursor.execute(s)
    records1=cursor.fetchall()
    s="select * from labtestresult where ltestno=" + s1
    cursor.execute(s)
    records2=cursor.fetchall()
    for row in records2:
        rfile=row[1]
        staffid1=row[2]
        rdate=row[3]
    l=[]
    s="select tname from labtestitems where ltestno="+ s1
    cursor.execute(s)
    records2=cursor.fetchall()
    for row in records2:
        l.append(row[0])

    return render(request,"labtestresult3.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd ,'s1':s1,'rfile':rfile,'staffid1':staffid1,'rdate':rdate,'l':l,'records1':records1,'records':records,'s0':s0,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})


def down11(request):
    s1=request.POST["t1"]
    file_path='./labresult/'+ s1
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def medsale1(request):
    con = connect()
    cursor = con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    return render(request,"medsale1.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd})

def medsale2(request):
    con=connect()
    cursor=con.cursor()
    #------
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #------
    s="delete from temp1"
    cursor.execute(s)
    con.commit()
    s0=request.POST["t0"]
    hospid=""
    name=""
    hname=""
    place=""
    pin=""
    ph=""
    district=""
    gender=""
    age=""
    adharno=""
    regdate=""
    hospid=""
    s="select * from patient where pid='" + s0 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
        adharno = row[9]
        regdate=row[10]
        hospid = row[13]
    location1=""
    place1=""
    pin1=""
    phone1=""
    district1=""
    email1=""
    htype1=""
    s="select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location1=row[1]
        place1 = row[2]
        pin1 = row[3]
        phone1 = row[4]
        district1 = row[5]
        email1 = row[6]
        htype1 = row[7]
    s="select * from session "
    cursor.execute(s)
    records11=cursor.fetchall()
    for row in records11:
        hid=row[1]
    #s="select tname,ttype,tcontent from labmaster where tname in (select tname from hosplab where hospid='"+ hid +"')"
    s = "select medname,cstock from medstock where hospid='" + hid + "' and cstock>0"
    cursor.execute(s)
    records1=cursor.fetchall()

    return render(request,"medsale2.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'records1':records1,'records':records,'s0':s0,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})


def medsale3(request):
    con=connect()
    cursor=con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #------
    s0=request.POST["t0"]
    s1 = request.POST["t1"]
    hospid=""
    name=""
    hname=""
    place=""
    pin=""
    ph=""
    district=""
    gender=""
    age=""
    adharno=""
    regdate=""
    hospid=""
    s="select * from patient where pid='" + s0 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
        adharno = row[9]
        regdate=row[10]
        hospid = row[13]
    location1=""
    place1=""
    pin1=""
    phone1=""
    district1=""
    email1=""
    htype1=""
    s="select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location1=row[1]
        place1 = row[2]
        pin1 = row[3]
        phone1 = row[4]
        district1 = row[5]
        email1 = row[6]
        htype1 = row[7]
    s="select * from session "
    cursor.execute(s)
    records11=cursor.fetchall()
    for row in records11:
        hid=row[1]
    #s="select tname,ttype,tcontent from labmaster where tname in (select tname from hosplab where hospid='"+ hid +"')"
    s = "select medname,cstock from medstock where hospid='" + hid + "' and cstock>0"
    cursor.execute(s)
    records1=cursor.fetchall()
    s="select * from pharmacymed where medname='"+ s1  + "'"
    cursor.execute(s)
    records3=cursor.fetchall()
    for row in records3:
        medtype=row[1]
        company=row[2]
        content=row[3]
        medunit=row[4]
    s = "select * from medstock where medname='" + s1 +    "' and hospid='"+ hid +  "'"

    cursor.execute(s)
    records3 = cursor.fetchall()
    cstock=0
    for row in records3:
        cstock = row[2]

    return render(request,"medsale3.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'s1':s1,'medtype':medtype,'company':company,'content':content,'medunit':medunit,'cstock':cstock,'records1':records1,'records':records,'s0':s0,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})


def medsale4(request):
    con=connect()
    cursor=con.cursor()
    #-------
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #------
    s0=request.POST["t0"]
    s1 = request.POST["t1"]
    s2 = request.POST["t2"]
    s="select * from temp1 where medname='" + s1 + "'"
    cursor.execute(s)
    if cursor.rowcount>0:
        records=cursor.fetchall()
        for row in records:
            itemno=row[0]
        s="update temp1 set qty="+ s2 + " where itemno="+ str(itemno)
        cursor.execute(s)
    else:

        itemno=0
        s="select * from temp1 order by itemno desc"
        cursor.execute(s)
        records=cursor.fetchall()
        for row in records:
            itemno=row[0]
            break
        itemno=itemno+1
        s="insert into temp1 values("+ str(itemno) + ",'" + s1 + "'," + s2 + ")"
        cursor.execute(s)
        con.commit()
    s="select itemno,medname,qty from temp1"
    cursor.execute(s)
    records4=cursor.fetchall()
    hospid=""
    name=""
    hname=""
    place=""
    pin=""
    ph=""
    district=""
    gender=""
    age=""
    adharno=""
    regdate=""
    hospid=""
    s="select * from patient where pid='" + s0 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
        adharno = row[9]
        regdate=row[10]
        hospid = row[13]
    location1=""
    place1=""
    pin1=""
    phone1=""
    district1=""
    email1=""
    htype1=""
    s="select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location1=row[1]
        place1 = row[2]
        pin1 = row[3]
        phone1 = row[4]
        district1 = row[5]
        email1 = row[6]
        htype1 = row[7]
    s="select * from session "
    cursor.execute(s)
    records11=cursor.fetchall()
    for row in records11:
        hid=row[1]
    #s="select tname,ttype,tcontent from labmaster where tname in (select tname from hosplab where hospid='"+ hid +"')"
    s = "select medname,cstock from medstock where hospid='" + hid + "' and cstock>0"
    cursor.execute(s)
    records1=cursor.fetchall()
    s="select * from pharmacymed where medname='"+ s1  + "'"
    print(s)
    cursor.execute(s)
    records3=cursor.fetchall()
    for row in records3:
        medtype=row[1]
        company=row[2]
        content=row[3]
        medunit=row[4]
    s = "select * from medstock where medname='" + s1 +    "' and hospid='"+ hid +  "'"

    cursor.execute(s)
    records3 = cursor.fetchall()
    cstock=0
    for row in records3:
        cstock = row[2]

    return render(request,"medsale4.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'records4':records4,'s1':s1,'s2':s2,'medtype':medtype,'company':company,'content':content,'medunit':medunit,'cstock':cstock,'records1':records1,'records':records,'s0':s0,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})

def medsale44(request):
    con=connect()
    cursor=con.cursor()
    #----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #-----
    s0=request.POST["t0"]
    s1 = request.POST["t1"]
    s2 = request.POST["t2"]
    s3 = request.POST["t3"]
    s="delete from temp1 where itemno="+ s3
    cursor.execute(s)
    con.commit()
    s="update temp1 set itemno=itemno-1 where itemno>"+ s3
    cursor.execute(s)
    con.commit()
    s="select itemno,medname,qty from temp1"
    cursor.execute(s)
    records4=cursor.fetchall()

    hospid=""
    name=""
    hname=""
    place=""
    pin=""
    ph=""
    district=""
    gender=""
    age=""
    adharno=""
    regdate=""
    hospid=""
    s="select * from patient where pid='" + s0 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
        adharno = row[9]
        regdate=row[10]
        hospid = row[13]
    location1=""
    place1=""
    pin1=""
    phone1=""
    district1=""
    email1=""
    htype1=""
    s="select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location1=row[1]
        place1 = row[2]
        pin1 = row[3]
        phone1 = row[4]
        district1 = row[5]
        email1 = row[6]
        htype1 = row[7]
    s="select * from session "
    cursor.execute(s)
    records11=cursor.fetchall()
    for row in records11:
        hid=row[1]
    #s="select tname,ttype,tcontent from labmaster where tname in (select tname from hosplab where hospid='"+ hid +"')"
    s = "select medname,cstock from medstock where hospid='" + hid + "' and cstock>0"
    cursor.execute(s)
    records1=cursor.fetchall()
    s="select * from pharmacymed where medname='"+ s1  + "'"
    print(s)
    cursor.execute(s)
    records3=cursor.fetchall()
    for row in records3:
        medtype=row[1]
        company=row[2]
        content=row[3]
        medunit=row[4]
    s = "select * from medstock where medname='" + s1 +    "' and hospid='"+ hid +  "'"

    cursor.execute(s)
    records3 = cursor.fetchall()
    cstock=0
    for row in records3:
        cstock = row[2]

    return render(request,"medsale4.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'records4':records4,'s1':s1,'s2':s2,'medtype':medtype,'company':company,'content':content,'medunit':medunit,'cstock':cstock,'records1':records1,'records':records,'s0':s0,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})

def medsale5(request):
    con=connect()
    cursor=con.cursor()
    #------
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa=""
    bb=""
    cc=""
    dd=""
    if desig=="Pharmacist":
        aa="yes"
    elif desig=="Dr":
        bb="yes"
    elif desig=="Office Staff":
        cc="yes"
    elif desig=="Lab Staff":
        dd="yes"


    #------
    s0=request.POST["t0"]

    hospid=""
    name=""
    hname=""
    place=""
    pin=""
    ph=""
    district=""
    gender=""
    age=""
    adharno=""
    regdate=""
    hospid=""
    s="select * from patient where pid='" + s0 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
        adharno = row[9]
        regdate=row[10]
        hospid = row[13]
    location1=""
    place1=""
    pin1=""
    phone1=""
    district1=""
    email1=""
    htype1=""
    s="select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location1=row[1]
        place1 = row[2]
        pin1 = row[3]
        phone1 = row[4]
        district1 = row[5]
        email1 = row[6]
        htype1 = row[7]
    s="select * from session "
    cursor.execute(s)
    records11=cursor.fetchall()
    for row in records11:
        staffid=row[0]
        hid=row[1]
    s = "select itemno,medname,qty from temp1"
    cursor.execute(s)
    records4 = cursor.fetchall()
    sdate=ccdate()
    sno=0
    s="select * from medsalemaster order by sno desc"
    cursor.execute(s)
    records5=cursor.fetchall()
    for row in records5:
        sno=row[0]
        break
    sno=sno+1
    s="insert into medsalemaster values("+ str(sno) + ",'" + s0 + "','" + sdate +"','" + staffid +"','"+ hid + "')"
    cursor.execute(s)
    con.commit()
    s="select * from temp1"
    cursor.execute(s)
    records5=cursor.fetchall()
    for row in records5:
        medname=row[1]
        qty=row[2]
        s="insert into medsalechild values("+str(sno) + ",'" + medname + "'," + str(qty)+ ")"
        cursor.execute(s)
        con.commit()
        s="update medstock set cstock=cstock-"+ str(qty) + " where medname='"+ medname + "' and hospid='" + hid + "'"
        cursor.execute(s)
        con.commit()

    return render(request,"medsale5.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'sno':sno,'sdate':sdate,'records4':records4,'records':records,'s0':s0,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})


def medsalelist1(request):
    con = connect()
    cursor = con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    return render(request,"medsalelist1.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd})

def medsalelist2(request):
    con=connect()
    cursor=con.cursor()
    #-----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #-------
    s="delete from temp1"
    cursor.execute(s)
    con.commit()
    s0=request.POST["t0"]
    hospid=""
    name=""
    hname=""
    place=""
    pin=""
    ph=""
    district=""
    gender=""
    age=""
    adharno=""
    regdate=""
    hospid=""
    s="select * from patient where pid='" + s0 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
        adharno = row[9]
        regdate=row[10]
        hospid = row[13]
    location1=""
    place1=""
    pin1=""
    phone1=""
    district1=""
    email1=""
    htype1=""
    s="select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location1=row[1]
        place1 = row[2]
        pin1 = row[3]
        phone1 = row[4]
        district1 = row[5]
        email1 = row[6]
        htype1 = row[7]
    s="select * from session "
    cursor.execute(s)
    records11=cursor.fetchall()
    for row in records11:
        hid=row[1]
    s = "select sno,sdate,staffid,hospid  from medsalemaster where pid='" + s0 + "'"
    cursor.execute(s)
    records1=cursor.fetchall()

    return render(request,"medsalelist2.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'records1':records1,'records':records,'s0':s0,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})

def medsalelist3(request):
    con=connect()
    cursor=con.cursor()
    #-----------
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    #----------
    s0=request.POST["t0"]
    s1 = request.POST["t1"]
    hospid=""
    name=""
    hname=""
    place=""
    pin=""
    ph=""
    district=""
    gender=""
    age=""
    adharno=""
    regdate=""
    hospid=""
    s="select * from patient where pid='" + s0 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
        adharno = row[9]
        regdate=row[10]
        hospid = row[13]
    location1=""
    place1=""
    pin1=""
    phone1=""
    district1=""
    email1=""
    htype1=""
    s="select * from hospital where hospid='" + hospid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        location1=row[1]
        place1 = row[2]
        pin1 = row[3]
        phone1 = row[4]
        district1 = row[5]
        email1 = row[6]
        htype1 = row[7]
    s="select * from session "
    cursor.execute(s)
    records11=cursor.fetchall()
    for row in records11:
        hid=row[1]
    s = "select sno,sdate,staffid,hospid  from medsalemaster where pid='" + s0 + "'"
    cursor.execute(s)
    records1=cursor.fetchall()
    s = "select medname,qty  from medsalechild where sno='" + s1 + "'"
    cursor.execute(s)
    records11 = cursor.fetchall()

    return render(request,"medsalelist3.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd,'records11':records11,'s1':s1,'records1':records1,'records':records,'s0':s0,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})

def staffsignout(request):
    return render(request,"staffsignout.html")

def complaint11(request):
    con = connect()
    cursor = con.cursor()
    # -----
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    # -------

    return render(request, "complaint11.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd})


def complaint22(request):
    con=connect()
    cursor=con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    s1=request.POST["t1"]
    cmpno=0
    s="select * from complaint order by cmpno desc"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        cmpno=row[0]
        break
    cmpno = cmpno + 1
    cdate=ccdate()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]

    s="insert into complaint(cmpno,staffid,complaint,cdate) values("+ str(cmpno) + ",'" + staffid + "','" + s1 + "','"+ cdate + "')"
    cursor.execute(s)
    con.commit()

    return render(request,"complaint22.html",{'cmpno':cmpno,'s1':s1,'aa':aa,'bb':bb,'cc':cc,'dd':dd})



def viewreply11(request):
    con = connect()
    cursor = con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
    s="select cmpno,cdate from complaint where staffid='"+ staffid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"viewreply11.html",{'records':records,'aa':aa,'bb':bb,'cc':cc,'dd':dd})


def viewreply22(request):
    con = connect()
    cursor = con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    s1=request.POST["t1"]
    s="select * from complaint where cmpno="+ s1
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        complaint=row[3]
        cdate=row[4]
        reply=row[5]
        rdate=row[6]

    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
    s="select cmpno,cdate from complaint where staffid='"+ staffid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"viewreply22.html",{'s1':s1,'records':records,'complaint':complaint,'cdate':cdate,'reply':reply,'rdate':rdate,'aa':aa,'bb':bb,'cc':cc,'dd':dd})

def plist1(request):
    con = connect()
    cursor = con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    return render(request,"plist1.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd})

def plist2(request):
    con = connect()
    cursor = con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    s1=request.POST["t1"]
    s="select pid,name,hname,place,pin,ph,district,gender,age,adharno,regdate,staffid,hospid from patient where name like '"+ s1 +  "%'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"plist2.html",{'records':records,'s1':s1,'aa':aa,'bb':bb,'cc':cc,'dd':dd})


def plist11(request):
    con = connect()
    cursor = con.cursor()
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"

    return render(request,"plist11.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd})


def plist22(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["t1"]
    s = "select * from session"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        staffid = row[0]
        desig = row[2]
    aa = ""
    bb = ""
    cc = ""
    dd = ""
    if desig == "Pharmacist":
        aa = "yes"
    elif desig == "Dr":
        bb = "yes"
    elif desig == "Office Staff":
        cc = "yes"
    elif desig == "Lab Staff":
        dd = "yes"
    s="select * from patient where ph='" + s1 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    pid=""
    name=""
    hname=""
    place=""
    pin = ""
    ph = ""
    district = ""
    gender = ""
    age = ""
    adharno = ""

    for row in records:
        pid=row[0]
        name=row[1]
        hname = row[2]
        place = row[3]
        pin = row[4]
        ph = row[5]
        district = row[6]
        gender = row[7]
        age = row[8]
        adharno = row[9]

    return render(request,"plist22.html",{'s1':s1,'aa':aa,'bb':bb,'cc':cc,'dd':dd,'records':records,'pid':pid,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno})

