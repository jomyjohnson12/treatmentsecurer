from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from treatmentsecurer import connect, ccdate


def patientchangepassword1(request):
    return render(request,"patientchangepassword.html")

def patientchangepassword2(request):
    con = connect()
    cursor = con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        pid=row[0]

    s1 = request.POST["t1"]
    s2 = request.POST["t2"]
    s = "select * from patient where pid ='" + pid + "' and   password='" + s1 + "'"
    cursor.execute(s)
    if cursor.rowcount == 0:
        msg = "Invalid User ID or Pasword"
        return render(request, "patientchangepassword.html", {'msg': msg})
    else:
        s="update patient set password='"+ s2 +"'  where pid='"+ pid +  "'"

        cursor.execute(s)
        con.commit()
        msg="Successfully Changed..."
        return render(request, "patientchangepassword.html",{'msg': msg})


def opbook1(request):
    con = connect()
    cursor = con.cursor()
    s = "select distinct(spl) from staff where spl is not null"
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])
    return render(request,"opbook1.html",{'l':l})

def opbook2(request):
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

    return render(request,"opbook2.html",{'s1':s1,'l':l,'records':records})

def opbook3(request):
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
    return render(request, "opbook3.html", {'records':records,'s1':s1,'name': name, 'hname': hname,'place':place,'pin':pin,'ph':ph,'gender':gender,'specialization':specialization, 'hospid':hospid,'location':location,'place':place,'pin':pin,'phone':phone,'district':district,'email':email,'htype':htype})

def opbook4(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["t1"]
    s2=request.POST["d1"]
    pid=""
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        pid=row[0]
    datetime_str = s2

    d2 = datetime.strptime(datetime_str, '%Y-%m-%d')

    dd = d2.strftime("%A")



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
        if row[0] == dd:
            ff = "ok"
    if ff == "No":
        msg="No Consultation for the selected date"
        return render(request, "opbook44.html",
                      {'msg':msg,'records': records, 's1': s1,'s2': s2, 'name': name, 'hname': hname, 'place': place, 'pin': pin, 'ph': ph,
                       'gender': gender, 'specialization': specialization, 'hospid': hospid, 'location': location,
                       'place': place, 'pin': pin, 'phone': phone, 'district': district, 'email': email,
                       'htype': htype})
    s = "select * from opbooking where bdate='" + str(d2) + "' and drid='" + s1 + "' and bno not in (select bno from opcancel)"
    cursor.execute(s)
    records1 = cursor.fetchall()
    n = 0
    for row in records1:
        n = n + 1
    s = "select * from dropdays where staffid='" + s1 + "' and opday='" + dd + "'"
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
        return render(request, "opbook44.html",
                      {'msg':msg,'records': records, 's1': s1,'s2': s2, 'name': name, 'hname': hname, 'place': place, 'pin': pin, 'ph': ph,
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
        return render(request, "opbook44.html",
                      {'msg': msg, 'records': records, 's1': s1,'s2': s2, 'name': name, 'hname': hname, 'place': place,
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

    return render(request, "opbook4.html", {'tno':tno,'records':records,'s1':s1,'s2': s2,'name': name, 'hname': hname,'place':place,'pin':pin,'ph':ph,'gender':gender,'specialization':specialization, 'hospid':hospid,'location':location,'place':place,'pin':pin,'phone':phone,'district':district,'email':email,'htype':htype})


def opbook5(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["t1"]
    s2=request.POST["d1"]
    pid=""
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        pid=row[0]
    datetime_str = s2

    d2 = datetime.strptime(datetime_str, '%Y-%m-%d')

    dd = d2.strftime("%A")



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
        return render(request, "opbook44.html",
                      {'msg': msg, 'records': records, 's1': s1, 's2': s2, 'name': name, 'hname': hname, 'place': place,
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
    s="insert into opbooking(bno,drid,bdate,tno,pid,cdate,hospid) values("+ str(bno) + ",'" + s1 + "','"+ s2 + "',"+ str(tno) +",'"+ pid + "','"+ cdate + "','" + hospid + "')"

    cursor.execute(s)
    con.commit()
    return render(request, "opbook5.html", {'bno':bno,'tno':tno,'records':records,'s1':s1,'s2': s2,'name': name, 'hname': hname,'place':place,'pin':pin,'ph':ph,'gender':gender,'specialization':specialization, 'hospid':hospid,'location':location,'place':place,'pin':pin,'phone':phone,'district':district,'email':email,'htype':htype})

def opcancel1(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    pid=""
    for row in records:
        pid=row[0]
    bdate=ccdate()
    s="select bno,drid,bdate,tno from opbooking where pid='"+ pid +"' and bdate>'"+ bdate +"' and bno not in(select bno from opcancel)"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"opcancel1.html",{'records':records})

def opcancel2(request):
    con=connect()
    cursor=con.cursor()
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


    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    pid=""
    for row in records:
        pid=row[0]
    bdate=ccdate()
    s="select bno,drid,bdate,tno from opbooking where pid='"+ pid +"' and bdate>'"+ bdate +"' and bno not in(select bno from opcancel)"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"opcancel2.html",{'records':records,'s1':s1,'drid':drid,'bdate1':bdate1,'tno':tno,'cdate':cdate,'staffid':staffid,'sname':sname,'qualification':qualification,'specialization':specialization})

def opcancel3(request):
    con=connect()
    cursor=con.cursor()
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


    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    pid=""
    for row in records:
        pid=row[0]
    bdate=ccdate()
    s="insert into opcancel (bno,cdate) values("+ s1 + ",'" + bdate + "')"
    cursor.execute(s)
    con.commit()

    s="select bno,drid,bdate,tno from opbooking where pid='"+ pid +"' and bdate>'"+ bdate +"' and bno not in(select bno from opcancel)"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"opcancel3.html",{'records':records,'s1':s1,'drid':drid,'bdate1':bdate1,'tno':tno,'cdate':cdate,'staffid':staffid,'sname':sname,'qualification':qualification,'specialization':specialization})

def patientprofile(request):
    con = connect()
    cursor = con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    pid=""
    for row in records:
        pid=row[0]
    s="select * from patient where pid='"+ pid +"'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname=row[2]
        place=row[3]
        pin=row[4]
        ph=row[5]
        district=row[6]
        gender=row[7]
        age=row[8]
        adharno=row[9]
        regdate=row[10]
        staffid=row[12]
        hospid=row[13]
    return render(request,"patientprofile.html",{'pid':pid,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'staffid':staffid,'hospid':hospid})


def patientcomingbooking(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        pid=row[0]
    bdate=ccdate()
    s="select a.bno,a.drid,a.bdate,a.tno,a.hospid,b.name,b.gender,b.spl,c.location,c.place,c.pin,c.phone,c.district,c.htype from opbooking a,staff b,hospital c where a.drid=b.staffid and a.hospid=c.hospid and a.bno  not in (select bno from opcancel) and a.bdate>='"+ bdate + "' and a.pid='" + pid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"patientcomingbooking.html",{'records':records})


def patientprevbooking(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        pid=row[0]
    bdate=ccdate()
    s="select a.bno,a.drid,a.bdate,a.tno,a.hospid,b.name,b.gender,b.spl,c.location,c.place,c.pin,c.phone,c.district,c.htype from opbooking a,staff b,hospital c where a.drid=b.staffid and a.hospid=c.hospid and a.bno  not in (select bno from opcancel) and a.bdate<'"+ bdate + "' and a.pid='" + pid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"patientprevbooking.html",{'records':records})


def patientcomingcbooking(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        pid=row[0]
    bdate=ccdate()
    s="select a.bno,a.drid,a.bdate,a.tno,a.hospid,b.name,b.gender,b.spl,c.location,c.place,c.pin,c.phone,c.district,c.htype from opbooking a,staff b,hospital c where a.drid=b.staffid and a.hospid=c.hospid and a.bno   in (select bno from opcancel) and a.bdate>='"+ bdate + "' and a.pid='" + pid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"patientcomingcbooking.html",{'records':records})

def patientpreviouscbooking(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        pid=row[0]
    bdate=ccdate()
    s="select a.bno,a.drid,a.bdate,a.tno,a.hospid,b.name,b.gender,b.spl,c.location,c.place,c.pin,c.phone,c.district,c.htype from opbooking a,staff b,hospital c where a.drid=b.staffid and a.hospid=c.hospid and a.bno   in (select bno from opcancel) and a.bdate<'"+ bdate + "' and a.pid='" + pid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"patientpreviouscbooking.html",{'records':records})


def mycasefile(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        pid=row[0]

    s = "select eno,problem,prescription,drcomment,drid,bno,edate from casesheet where pid='" + pid + "'"
    cursor.execute(s)
    records1 = cursor.fetchall()
    return render(request, "mycasefile.html",{'records1': records1})

def mylabtestresult2(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        s0=row[0]

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
    return render(request,"mylabtestresult2.html",{'records2':records2,'records1':records1,'records':records,'s0':s0,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})

def mylabtestresult3(request):
    con=connect()
    cursor=con.cursor()

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

    return render(request,"mylabtestresult3.html",{'s1':s1,'rfile':rfile,'staffid1':staffid1,'rdate':rdate,'l':l,'records1':records1,'records':records,'s0':s0,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})


def mymedsalelist2(request):
    con=connect()
    cursor=con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        s0=row[0]

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

    s = "select sno,sdate,staffid,hospid  from medsalemaster where pid='" + s0 + "'"
    cursor.execute(s)
    records1=cursor.fetchall()

    return render(request,"mymedsalelist2.html",{'records1':records1,'records':records,'s0':s0,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})

def mymedsalelist3(request):
    con=connect()
    cursor=con.cursor()
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
    s = "select sno,sdate,staffid,hospid  from medsalemaster where pid='" + s0 + "'"
    cursor.execute(s)
    records1=cursor.fetchall()
    s = "select medname,qty  from medsalechild where sno='" + s1 + "'"
    cursor.execute(s)
    records11 = cursor.fetchall()
    return render(request,"mymedsalelist3.html",{'records11':records11,'s1':s1,'records1':records1,'records':records,'s0':s0,'name':name,'hname':hname,'place':place,'pin':pin,'ph':ph,'district':district,'gender':gender,'age':age,'adharno':adharno,'regdate':regdate,'hospid':hospid,'location1':location1,'place1':place1,'pin1':pin1,'phone1':phone1,'district1':district1,'email1':email1,'htype1':htype1})

def patientsignout(request):
    return render(request,"patientsignout.html")

def complaint1(request):
    return render(request,"complaint1.html")

def complaint2(request):
    con=connect()
    cursor=con.cursor()
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
        pid=row[0]

    s="insert into complaint(cmpno,pid,complaint,cdate) values("+ str(cmpno) + ",'" + pid + "','" + s1 + "','"+ cdate + "')"
    cursor.execute(s)
    con.commit()

    return render(request,"complaint2.html",{'cmpno':cmpno,'s1':s1})


def viewreply1(request):
    con = connect()
    cursor = con.cursor()
    s="select * from session"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        pid=row[0]
    s="select cmpno,cdate from complaint where pid='"+ pid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"viewreply1.html",{'records':records})


def viewreply2(request):
    con = connect()
    cursor = con.cursor()
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
        pid=row[0]
    s="select cmpno,cdate from complaint where pid='"+ pid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"viewreply2.html",{'s1':s1,'records':records,'complaint':complaint,'cdate':cdate,'reply':reply,'rdate':rdate})












