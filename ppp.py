from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import session

import pyttsx3 as p
global a
global b
app=Flask(__name__)

@app.route("/home",methods=["POST","GET"])
def home():
    if request.method=="POST":
       entered=request.form['ngm']
       if entered=='user':
           return redirect(url_for("login"))
       elif entered=='admin':
           return redirect(url_for("admin_login"))

    else:
        return render_template("index.html")
@app.route("/home/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
       user1=request.form['np']
       global a
       a=[user1]
       import mysql.connector 
       mydb=mysql.connector.connect(host="localhost",password="mysql123456",database="car_rent",port="3306",user="root",auth_plugin='mysql_native_password')
       c=mydb.cursor()
       kpo="insert into images(eid) values(%s)"
       klp=(a)
       c.execute(kpo,klp)
       mydb.commit()
       se="select usersid from email_user where usersid =%s"
       sr=([user1])
       c.execute(se,sr)
       my=c.fetchall()
       ooo=[]
       for ro in my:
            ooo.append(ro)
       try: 
        if (user1) in ooo[0][0]:
            dg="update images set id =1 where eid=%s"
            v=([user1])
            c.execute(dg,v)
            mydb.commit()
            d="update email_user set no=1 where usersid = %s"
            va=([user1])
            c.execute(d,va)
            mydb.commit()
            return redirect(url_for("image"))
       except:
        sd="insert into images(eid,id) values(%s,2)"
        fr=(a)
        c.execute(sd,fr)
        mydb.commit()
        sql="insert into extra(name,num) values(%s,1)"
        s1=(a)
        c.execute(sql,s1)
        mydb.commit()
        import smtplib
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        user='hcoder209@gmail.com'
        #password='chaitanya_123456'
        password='ynwhleskfmqczufn'
        #to_addr='gowthammanikanta422@gamil.com'
        #to_addr='pavanakhil189@gmail.com'
        to_addr='124004212@sastra.ac.in'
        server.login(user,password)
        import math
        import random
        digits='0123456789'
        otl=''
        for i in range(4):
            otl+=digits[math.floor(random.random()*10)]
        global msg
        msg=otl
        print('work')
        server.sendmail('hcoder209@gmail.com',a,msg)
        server.quit()
        print("mail sent")
        return redirect(url_for("otpq"))
    else:
        return render_template("email_login.html")
@app.route("/home/login/otp",methods=["POST","GET"])
def otpq():
    if request.method=="POST":
        ot=request.form["otpnm"]
        if ot==msg:
           import mysql.connector 
           mydb=mysql.connector.connect(host="localhost",password="mysql123456",database="car_rent",port="3306",user="root",auth_plugin='mysql_native_password')
           c=mydb.cursor()
           mn="select name from extra where num=1"
           c.execute(mn)
           m=c.fetchall()
           pal=[]
           for r in m:
               pal.append(r)
           sw="insert into email_user(usersid,no) values(%s,2)"
           sqq=(r)
           c.execute(sw,sqq)
           mydb.commit()
           sp="update extra set num = 0 where name =%s"
           cd=([pal[0][0]])
           c.execute(sp,cd)
           mydb.commit()
           return redirect(url_for("image"))
    else:
        return render_template("user_otp.html")
@app.route("/home/login/otp/image",methods=["POST","GET"])
def image():
    if request.method=="POST":
        t=request.form['nam']
        f=str(t)
        from PIL import Image
        import hashlib
        #C:\\Users\\munab\\OneDrive\\Pictures\\
        md=hashlib.md5(Image.open('{}'.format(f)).tobytes())
        #sql="insert into imageid(username,password,imgid,identify) values(%s,%s,%s,%s)"
        #s1=(uio,b,md.hexdigest(),'original')
        import mysql.connector 
        mydb=mysql.connector.connect(host="localhost",password="mysql123456",database="car_rent",port="3306",user="root",auth_plugin='mysql_native_password')
        c=mydb.cursor()
        c.execute("select usersid from email_user where no =1")
        pp=c.fetchall()
        l=[]
        for nn in pp:
            l.append(nn)
        c.execute("select no from email_user where no =1")
        pol=c.fetchall()
        lol=[]
        for iii in pol:
            lol.append(iii)
        try:
         if ('1') == lol[0][0]:
          c.execute("select usersid from email_user")
          my=c.fetchall()
          for ro in my:
               if (l[0][0]) in ro:
                 tan ="select imgid from imageid"
                 c.execute(tan)
                 nnp=c.fetchall()
                 k=[]
                 for too in nnp:
                     k.append(too)
                 if (k[0][0]) == md.hexdigest():
                    s1=(l[0][0],md.hexdigest(),'original')
                    sql="insert into imageid(username,imgid,identify) values(%s,%s,%s)"
                    c.execute(sql,s1)
                    mydb.commit()
                 else:
                     def converttobinary(filename):
                       with open(filename,'rb')as file:
                          binarydata=file.read()
                       return binarydata
                     def convertbinarytofile(binarydata,filename):
                       with open(filename,'wb') as file:
                              file.write(binarydata)
                     #####we will store the image
                     covertpc=converttobinary(f)
                     
                     with open(f,'rb')as file:
                          binarydata=file.read()
                     klt="update images set fake_photo =%s where id=1"
                     fpo=([binarydata])
                     c.execute(klt,fpo)
                     mydb.commit()
                     #binn=converttobinary('C:\\Users\\munab\\OneDrive\\Pictures\\cry.jpeg')
                     
                     s1=(l[0][0],md.hexdigest(),'fake')
                     sql="insert into imageid(username,imgid,identify) values(%s,%s,%s)"
                     c.execute(sql,s1)
                     mydb.commit()
                     
                 d="update email_user set no =0 where usersid = %s"
                 b=([l[0][0]])
                 c.execute(d,b)
                 mydb.commit()
                 c.execute(sql,s1)
                 jj=len(l)
                 kk=len(k)
                 lb="update images set id =0 where eid = %s"
                 vp=([l[0][0]])
                 c.execute(lb,vp)
                 mydb.commit()
                 return f"<h1>successfully updated</h1>"
        except:
          c.execute("select usersid from email_user where no=2")
          pp=c.fetchall()
          popy=[]
          for i in pp:
             popy.append(i)
          c.execute("select usersid from email_user")
          myl=c.fetchall()
          for ro in myl:
            if (popy[0][0]) in ro:
                 sql="insert into imageid(username,imgid,identify) values(%s,%s,%s)"
                 s1=(popy[0][0],md.hexdigest(),'original')
                 c.execute(sql,s1)
                 mydb.commit()
                 def converttobinary(filename):
                    with open(filename,'rb')as file:
                          binarydata=file.read()
                    return binarydata
                 def convertbinarytofile(binarydata,filename):
                     with open(filename,'wb') as file:
                              file.write(binarydata)
                 #####we will store the image
                 
                 insertquery="insert into images(photo,eid) value(%s,%s)"
                 #binn=converttobinary('C:\\Users\\munab\\OneDrive\\Pictures\\cry.jpeg')
                 covertpic=converttobinary(f)
                 with open(filename,'rb')as file:
                          binarydata=file.read()
                 kq="update images set photo =%s where id=2"
                 om=([binarydata])
                 c.execute(kq,om)
                 mydb.commit()
                 v="update email_user set no =0 where usersid = %s"
                 vt=([popy[0][0]])
                 c.execute(v,vt)
                 mydb.commit()
                 vm="update images set id =0 where eid = %s"
                 vo=([popy[0][0]])
                 c.execute(vm,vo)
                 mydb.commit()
                 return f"<h1>successfully updated</h1>"
        
    else:
        return render_template("image_page.html")
@app.route("/home/admin_login",methods=["POST","GET"])
def admin_login():
    if request.method=="POST":
       us1=request.form['npl']
       ps1=request.form['np']
       if us1 == 'chaitanya' and ps1 == 'chaitanya_123':
           return redirect(url_for('view'))
       else:
           return f'<h1>incorrect user name or password</h1>'
    else:
        return render_template('admin.html')
@app.route("/home/admin_login/view",methods=["POST","GET"])
def view():
    return render_template('view_page.html')
if __name__=="__main__":
    app.run(debug=True,port=5000, host='0.0.0.0')
