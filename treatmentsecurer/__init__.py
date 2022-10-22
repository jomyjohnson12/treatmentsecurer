def connect():
    import pymysql
    con = pymysql.connect(host="localhost", user="root", passwd="", database="treatment")
    return(con)

def ccdate():
    import datetime
    now = datetime.datetime.now()
    d = now.day
    m = now.month
    y = now.year
    regdate = str(y) + "-" + str(m) + "-" + str(d)
    return(regdate)