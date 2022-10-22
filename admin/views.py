from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from treatmentsecurer import connect, ccdate


def adminchangepassword1(request):
    return render(request,"adminchangepassword.html")

def adminchangepassword2(request):
    con = connect()
    cursor = con.cursor()
    s1 = request.POST["t1"]
    s2 = request.POST["t2"]
    s = "select * from login where  password='" + s1 + "'"
    cursor.execute(s)
    if cursor.rowcount == 0:
        msg = "Invalid Old Password"
        return render(request, "adminchangepassword.html", {'msg': msg})
    else:
        s="update login set password='"+ s2 +"'"
        cursor.execute(s)
        con.commit()
        msg="Successfully Changed..."
        return render(request, "adminchangepassword.html",{'msg': msg})



def hospreg1(request):
    return render(request,"hospreg1.html")
def hospreg2(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    s3 = request.POST["t3"]
    s4 = request.POST["t4"]
    s5 = request.POST["t5"]
    s6 = request.POST["t6"]
    s7 = request.POST["t7"]
    s8 = request.POST["t8"]
    regdate=ccdate()
    hospid="H12345"
    s="select * from hospital order by hospid desc"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        hospid=row[0]
        break
    x=hospid[1:]
    y=int(x)
    y=y+1
    hospid="H"+ str(y)
    s="insert into hospital values('" +  hospid + "','" + s1 + "','" + s2 + "','" + s3 + "','" + s4 + "','" + s5 + "','" + s6 + "','" + s7 + "','" + regdate + "','" + s8  + "')"
    cursor.execute(s)
    con.commit()
    return render(request,"hospreg2.html",{'hospid':hospid,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8})



def staffreg1(request):
    con = connect()
    cursor = con.cursor()
    s = "select hospid from hospital"
    cursor.execute(s)
    records = cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])

    s="select hospid,location,place,district,htype from hospital"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"staffreg1.html",{'records':records,'l':l})


def staffreg2(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    s3 = request.POST["t3"]
    s4 = request.POST["t4"]
    s5 = request.POST["t5"]
    s6 = request.POST["t6"]
    s7 = request.POST["t7"]
    s8 = request.POST["t8"]
    s9 = request.POST["t9"]
    s10 = request.POST["t10"]
    staffid="S10000"
    s="select * from staff order by staffid desc"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
        break
    x=staffid[1:]
    y=int(x)
    y=y+1
    staffid="S"+ str(y)
    regdate=ccdate()
    s="insert into staff(staffid,name,hname,place,pin,ph,gender,qualification,experience,password) values('"+ staffid + "','" + s1 + "','" + s2 + "','" + s3 + "','" + s4 + "','" + s5 + "','" + s6 + "','" + s7 + "','" + s8  + "','" + staffid + "')"
    cursor.execute(s)
    con.commit()
    wno=1
    s="insert into staffhospital values('"+ staffid + "','" + str(wno) + "','" + s10  + "','" + s9 + "','" + regdate +  "')"
    cursor.execute(s)
    con.commit()
    s = "select hospid from hospital"
    cursor.execute(s)
    records = cursor.fetchall()
    l = []
    for row in records:
        l.append(row[0])

    s = "select hospid,location,place,district,htype from hospital"
    cursor.execute(s)
    records = cursor.fetchall()
    return render(request, "staffreg2.html", {'records': records, 'l': l,'staffid':staffid,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'s9':s9,'s10':s10})


def doctorreg1(request):
    con = connect()
    cursor = con.cursor()
    s = "select hospid from hospital"
    cursor.execute(s)
    records = cursor.fetchall()
    l = []
    for row in records:
        l.append(row[0])

    s = "select hospid,location,place,district,htype from hospital"
    cursor.execute(s)
    records = cursor.fetchall()
    return render(request, "doctorreg1.html", {'records': records, 'l': l})

def doctorreg2(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    s3 = request.POST["t3"]
    s4 = request.POST["t4"]
    s5 = request.POST["t5"]
    s6 = request.POST["t6"]
    s7 = request.POST["t7"]
    s8 = request.POST["t8"]
    s9 = request.POST["t9"]
    s10 = request.POST["t10"]
    s11=request.POST["t11"]

    staffid="S10000"
    s="select * from staff order by staffid desc"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[0]
        break
    x=staffid[1:]
    y=int(x)
    y=y+1
    staffid="S"+ str(y)
    regdate=ccdate()
    s="insert into staff(staffid,name,hname,place,pin,ph,gender,spl,qualification,experience,password) values('"+ staffid + "','" + s1 + "','" + s2 + "','" + s3 + "','" + s4 + "','" + s5 + "','" + s6 + "','" + s8 + "','" + s7  + "','" + s9 + "','" + staffid + "')"
    cursor.execute(s)
    con.commit()
    wno=1
    s="insert into staffhospital values('"+ staffid + "','" + str(wno) + "','" + s11  + "','" + s10 + "','" + regdate +  "')"
    cursor.execute(s)
    con.commit()
    s = "select hospid from hospital"
    cursor.execute(s)
    records = cursor.fetchall()
    l = []
    for row in records:
        l.append(row[0])

    s = "select hospid,location,place,district,htype from hospital"
    cursor.execute(s)
    records = cursor.fetchall()
    return render(request, "doctorreg2.html", {'records': records, 'l': l,'staffid':staffid,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8,'s9':s9,'s10':s10})




def medreg1(request):
    return render(request,"medreg1.html")
def medreg2(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    s3 = request.POST["t3"]
    s4 = request.POST["t4"]
    s5 = request.POST["t5"]
    s="select * from pharmacymed where medname='" + s1 +"'"
    cursor.execute(s)
    if cursor.rowcount>0:
        msg ="This medicine already Registered"
    else:
        s="insert into pharmacymed values('"+ s1 + "','" + s2 + "','" + s3 + "','" + s4 + "','" + s5 +   "')"
        cursor.execute(s)
        con.commit()
        msg="Medicine Registered...."
    return render(request,"medreg2.html",{'msg':msg,'s1':s1,'s2':s2,'s3':s3 ,'s4':s4,'s5':s5})

def labreg1(request):
    return render(request,"labreg1.html")

def labreg2(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    s3 = request.POST["t3"]
    s4 = request.POST["t4"]
    s5 = request.POST["t5"]
    s6 = request.POST["t6"]
    s7 = request.POST["t7"]
    s="select  * from labmaster where tname='"+ s1 +  "'"
    cursor.execute(s)
    if cursor.rowcount>0:
        msg="This test name already exist"
    else:
        s="insert into labmaster values('"+ s1 + "','"+ s2 + "','"+  s3 + "','"+ s4 + "','"+ s5 + "','"+ s6 + "','"+ s7 +  "')"
        cursor.execute(s)
        con.commit()
        msg="Succesfully Stored"
    return render(request,"labreg2.html",{'msg':msg,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7})


def stafflist1(request):
    con = connect()
    cursor = con.cursor()
    l = []
    s = "select distinct(designation) from staffhospital"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        l.append(row[0])
    return render(request, "stafflist1.html", {'l': l})


def stafflist2(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["c1"]
    s="select b.staffid,b.name,b.hname,b.place,b.pin,b.ph,b.gender,b.qualification,b.experience,a.hospid from staffhospital a,staff b where a.designation='" + s1 +  "' and a.staffid = b.staffid"
    cursor.execute(s)
    records1=cursor.fetchall()
    l = []
    s = "select distinct(designation) from staffhospital"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        l.append(row[0])
    return render(request, "stafflist2.html", {'l': l,'s1':s1,'records1':records1})


def medstocklist1(request):
    con = connect()
    cursor = con.cursor()
    l = []
    s = "select hospid from hospital"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        l.append(row[0])
    return render(request, "medstocklist1.html", {'l': l})



def medstocklist2(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["c1"]
    s="select medname,cstock from medstock  where hospid='"+s1 + "'"
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

    return render(request, "medstocklist2.html", {'l': l,'s1':s1,'records1':records1,'location':location,'place':place,'pin':pin,'phone':phone,'district':district,'email':email,'htype':htype,'nbed':nbed})



def meddamagelist1(request):
    con = connect()
    cursor = con.cursor()
    l = []
    s = "select hospid from hospital"
    cursor.execute(s)
    records = cursor.fetchall()
    for row in records:
        l.append(row[0])
    return render(request, "meddamagelist1.html", {'l': l})



def meddamagelist2(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["c1"]
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

    return render(request, "meddamagelist2.html", {'l': l,'s1':s1,'records1':records1,'location':location,'place':place,'pin':pin,'phone':phone,'district':district,'email':email,'htype':htype,'nbed':nbed})

def allot1(request):
    con=connect()
    cursor=con.cursor()
    s="select hospid from hospital"
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])
    return render(request,"allot1.html",{'l':l})

def allot2(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["c1"]
    s="select * from hospital where hospid='"+ s1 +  "'"
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

    s = "select hospid from hospital"
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])

    s = "select tname from labmaster"
    cursor.execute(s)
    records = cursor.fetchall()
    m = []
    for row in records:
        m.append(row[0])
    n=[]
    s="select tname from hosplab where hospid='"+ s1 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        n.append(row[0])

    return render(request,"allot2.html",{'n':n,'m':m,'l':l,'s1':s1,'location':location,'place':place,'pin':pin,'phone':phone,'district':district,'email':email,'htype':htype})

def allot3(request):
    con=connect()
    cursor=con.cursor()
    s1=request.POST["c1"]
    s2=request.POST["c2"]
    s="select * from hosplab where tname='" + s2 + "' and hospid='" + s1  +"'"
    cursor.execute(s)
    if cursor.rowcount>0:
        msg="This Test already alloted"
    else:
        s="insert into hosplab values('"+ s2 + "','" + s1 +  "')"
        cursor.execute(s)
        con.commit()
        msg="Successfully Alloted"



    s="select * from hospital where hospid='"+ s1 +  "'"
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

    s = "select hospid from hospital"
    cursor.execute(s)
    records=cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])

    s = "select tname from labmaster"
    cursor.execute(s)
    records = cursor.fetchall()
    m = []
    for row in records:
        m.append(row[0])
    n=[]
    s="select tname from hosplab where hospid='"+ s1 + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        n.append(row[0])

    return render(request,"allot3.html",{'msg':msg,'n':n,'m':m,'l':l,'s1':s1,'location':location,'place':place,'pin':pin,'phone':phone,'district':district,'email':email,'htype':htype})


def adminsignout(request):
    return render(request,"adminsignout.html")

def complaintreply1(request):
    con = connect()
    cursor = con.cursor()
    s="select cmpno,pid,cdate from complaint where pid is not null and reply is null"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"complaintreply1.html",{'records':records})

def complaintreply2(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["t1"]
    s="select * from complaint where cmpno="+ s1
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        pid=row[1]
        complaint=row[3]
        cdate=row[4]
    s="select * from patient where pid='"+pid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname=row[2]
        place=row[3]
        pin=row[4]
        phone=row[5]

    s="select cmpno,pid,cdate from complaint where pid is not null and reply is null"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"complaintreply2.html",{'s1':s1,'records':records,'pid':pid,'complaint':complaint,'cdate':cdate,'name':name,'hname':hname,'place':place,'pin':pin,'phone':phone})


def complaintreply3(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    rdate=ccdate()
    s="update complaint set reply='" + s2 + "',rdate='" + rdate + "' where cmpno="+ s1
    cursor.execute(s)
    con.commit()

    s="select * from complaint where cmpno="+ s1
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        pid=row[1]
        complaint=row[3]
        cdate=row[4]
    s="select * from patient where pid='"+pid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname=row[2]
        place=row[3]
        pin=row[4]
        phone=row[5]

    s="select cmpno,pid,cdate from complaint where pid is not null and reply is null "
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"complaintreply3.html",{'s1':s1,'s2':s2,'records':records,'pid':pid,'complaint':complaint,'cdate':cdate,'name':name,'hname':hname,'place':place,'pin':pin,'phone':phone})


def complaintreply11(request):
    con = connect()
    cursor = con.cursor()
    s="select cmpno,staffid,cdate from complaint where staffid is not null and reply is null"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"complaintreply11.html",{'records':records})

def complaintreply22(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["t1"]
    s="select * from complaint where cmpno="+ s1
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[2]
        complaint=row[3]
        cdate=row[4]
    s="select * from staff where staffid='"+staffid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname=row[2]
        place=row[3]
        pin=row[4]
        phone=row[5]

    s="select cmpno,staffid,cdate from complaint where staffid is not null and reply is null"
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"complaintreply22.html",{'s1':s1,'records':records,'staffid':staffid,'complaint':complaint,'cdate':cdate,'name':name,'hname':hname,'place':place,'pin':pin,'phone':phone})


def complaintreply33(request):
    con = connect()
    cursor = con.cursor()
    s1=request.POST["t1"]
    s2 = request.POST["t2"]
    rdate=ccdate()
    s="update complaint set reply='" + s2 + "',rdate='" + rdate + "' where cmpno="+ s1
    cursor.execute(s)
    con.commit()

    s="select * from complaint where cmpno="+ s1
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        staffid=row[2]
        complaint=row[3]
        cdate=row[4]
    s="select * from patient where staffid='"+staffid + "'"
    cursor.execute(s)
    records=cursor.fetchall()
    for row in records:
        name=row[1]
        hname=row[2]
        place=row[3]
        pin=row[4]
        phone=row[5]

    s="select cmpno,staffid,cdate from complaint where staffid is not null and reply is null "
    cursor.execute(s)
    records=cursor.fetchall()
    return render(request,"complaintreply33.html",{'s1':s1,'s2':s2,'records':records,'staffid':staffid,'complaint':complaint,'cdate':cdate,'name':name,'hname':hname,'place':place,'pin':pin,'phone':phone})
