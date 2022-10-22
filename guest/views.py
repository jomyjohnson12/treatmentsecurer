from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from treatmentsecurer import connect


def home(request):
    return render(request,"home.html")

def adminlogin1(request):
    return render(request,"adminlogin.html")

def adminlogin2(request):
    s1 = request.POST["t1"]
    s2 = request.POST["t2"]
    con = connect()
    cursor = con.cursor()
    s = "select * from login where userid='" + s1 + "' and password='" + s2 + "'"
    cursor.execute(s)
    if cursor.rowcount == 0:
        return render(request, "adminlogin.html", {'msg': 'Invalid id and password'})
    else:
        return render(request, "adminprocess.html")


def stafflogin1(request):
    return render(request,"stafflogin.html")

def stafflogin2(request):
    s1 = request.POST["t1"]
    s2 = request.POST["t2"]
    con = connect()
    cursor = con.cursor()
    s = "select * from staff where staffid='" + s1 + "' and password='" + s2 + "'"
    cursor.execute(s)
    if cursor.rowcount == 0:
        return render(request, "stafflogin.html", {'msg': 'Invalid id and password'})
    else:
        s="select * from staffhospital where staffid='" + s1 +  "'  order by wno desc"
        cursor.execute(s)
        records=cursor.fetchall()
        for row in records:
            hospid=row[2]
            desig=row[3]
        if desig=="Pharmacist":
            desig="Pharmacist"
        elif desig=="Office Staff":
            desig="Office Staff"
        elif desig=="Lab Staff":
            desig="Lab Staff"
        else:
            desig="Dr"



        s="delete from session"
        cursor.execute(s)
        con.commit()
        s="insert into session values('"+ s1 + "','" + hospid + "','" + desig +  "')"
        cursor.execute(s)
        con.commit()
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

        return render(request, "staffprocess.html",{'aa':aa,'bb':bb,'cc':cc,'dd':dd })
def patientlogin1(request):
    return render(request,"patientlogin.html")

def patientlogin2(request):
    s1 = request.POST["t1"]
    s2 = request.POST["t2"]
    con = connect()
    cursor = con.cursor()
    s = "select * from patient where pid='" + s1 + "' and password='" + s2 + "'"
    cursor.execute(s)
    if cursor.rowcount == 0:
        return render(request, "patientlogin.html", {'msg': 'Invalid id and password'})
    else:
        records=cursor.fetchall()
        for row in records:
            hospid=row[13]

        s="delete from session"
        cursor.execute(s)
        con.commit()
        s="insert into session(userid,hospid) values('"+ s1 + "','" + hospid +  "')"
        cursor.execute(s)
        con.commit()

        return render(request, "patientprocess.html")



def hospitallist1(request):
    con = connect()
    cursor = con.cursor()
    l = []
    s = "select distinct(district) from hospital"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        l.append(row[0])
    return render(request, "hospitallist1.html", {'l': l})



def hospitallist2(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["c1"];
    s="select hospid,location,place,pin,phone,email,htype,nbed from hospital where district='"+ s1 + "'"
    cursor.execute(s)
    records1=cursor.fetchall()

    l = []
    s = "select distinct(district) from hospital where district<>'"+ s1 + "'"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        l.append(row[0])
    return render(request, "hospitallist2.html", {'l': l,'s1':s1,'records1':records1})


def medlist(request):
    con = connect()
    cursor = con.cursor()

    s="select medname,medtype,company,content,medunit from pharmacymed"
    cursor.execute(s)
    records1=cursor.fetchall()
    return render(request, "medlist.html", {'records1':records1})


def labtestlist(request):
    con = connect()
    cursor = con.cursor()

    s="select tname,ttype,tcontent,tduration,tdunit,tresultduration,trdunit  from labmaster"
    cursor.execute(s)
    records1=cursor.fetchall()
    return render(request, "labtestlist.html", {'records1':records1})

def allotedlab1(request):
    con=connect()
    cursor=con.cursor()
    s="select tname from labmaster"
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])
    return render(request,"allotedlab1.html",{'l':l})

def allotedlab2(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["c1"]
    s="select * from labmaster where tname='"+ s1 +  "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        ttype=row[1]
        tcontent=row[2]
        tduration=row[3]
        tdunit=row[4]
        tresultduration=row[5]
        trdunit=row[6]

    s="select tname from labmaster where tname<>'"+s1 +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])
    n=[]
    s="select hospid,location,place,pin,phone,district,email,htype,nbed from hospital where hospid in (select hospid from hosplab  where tname='"+ s1 +"')"

    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        n.append(row[0])

    return render(request,"allotedlab2.html",{'records':records,'l':l,'s1':s1,'ttype':ttype,'tcontent':tcontent,'tduration':tduration,'tdunit':tdunit,'tresultduration':tresultduration,'trdunit':trdunit})


def drlist(request):
    con = connect()
    cursor = con.cursor()
    s="select hospid,location,place,district from hospital"
    cursor.execute(s)
    records=cursor.fetchall()

    return render(request, "drlist.html", {'records':records})

def drlist1(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["t1"]

    s = "select hospid,location,place,district from hospital"
    cursor.execute(s)
    records = cursor.fetchall()

    s="select b.staffid,b.name,b.place,b.ph,b.gender,b.qualification,b.experience,b.spl from staffhospital a,staff b where a.hospid='" + s1 +  "' and a.staffid = b.staffid and b.spl is not null"
    cursor.execute(s)
    records1=cursor.fetchall()

    return render(request, "drlist1.html", {'s1':s1,'records':records,'records1':records1})

def drdays11(request):
    con = connect()
    cursor = con.cursor()
    s = "select distinct(spl) from staff where spl is not null"
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])
    return render(request,"drdays11.html",{'l':l})

def drdays22(request):
    con = connect()
    cursor = con.cursor()
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

    return render(request,"drdays22.html",{'s1':s1,'l':l,'records':records})

def drdays33(request):
    con = connect()
    cursor = con.cursor()
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
        gender=row[7]
        specialization=row[8]
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
    return render(request, "drdays33.html", {'records':records,'s1':s1,'name': name, 'hname': hname,'place':place,'pin':pin,'ph':ph,'gender':gender,'specialization':specialization, 'hospid':hospid,'location':location,'place':place,'pin':pin,'phone':phone,'district':district,'email':email,'htype':htype})

def about(request):
    return  render(request,"about.html")