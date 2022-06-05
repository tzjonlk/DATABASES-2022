import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="mydatabase"
)

@app.route("/")

def home():

  return render_template("home.html")


@app.route("/showprograms")

def program():
  h = ["Program Name", "Program Address"]
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM program")
  prog = mycursor.fetchall()
  return render_template("programs.html",values= prog, header=h)
    
@app.route("/page1/<startdate>/<enddate>/<corporate>/<nostartdate>/<noenddate>/<nocorporate>", methods=["GET","POST"])

def page1(startdate,enddate,corporate,nostartdate,noenddate,nocorporate):
  if request.method == "POST" and "proj_name" in request.form:
    tuxaio=request.form.get("proj_name")
    return redirect(url_for("index", tuxaio=tuxaio))


  elif request.method== "POST":
    startdate = request.form["start-date"]
    enddate = request.form["end-date"]
    corporate = request.form["corporate"]
    nocorporate= 0
    nostartdate= 0
    noenddate = 0
    if (len(corporate)==0):
      nocorporate = 1
      corporate = -1      
    if (len(startdate)==0):
      nostartdate = 1
      startdate = -1
    if (len(enddate)==0):
      noenddate = 1
      enddate = -1
    return redirect(url_for("page1", startdate=startdate, enddate=enddate, corporate=corporate,nostartdate=nostartdate, noenddate=noenddate, nocorporate=nocorporate))
  else:
    mycursor = mydb.cursor()
    header = ["Project Title", "Grant Amount", "Starting Date", "Ending Date", "Project Abstract", "Corporate First Name","Corporate Last name" ,"Organisation Name", "Field Name", "Program Name", "Researchers"]
    mycursor.execute("SELECT cfirst_name FROM corporate_member")
    corporate_fnames = mycursor.fetchall()
    mycursor.execute("SELECT  clast_name FROM corporate_member")
    corporate_lnames = mycursor.fetchall()
    corporate_names=[]
    st1=[]
    st2=[]
    for i in range(len(corporate_fnames)):
       s1= str(corporate_fnames[i])
       s1=s1[2:(len(s1)-3)]
       st1.append(s1)
       s2= str(corporate_lnames[i])
       s2=s2[2:(len(s2)-3)]
       st2.append(s2)
       corporate_names.append(s1+" "+s2)
  
    if(((nostartdate)and(noenddate))and(nocorporate)):
      proj= "SELECT DISTINCT(project_title), grant_amount, starting_date, ending_date, project_abstract,corporate_member.cfirst_name,corporate_member.clast_name, org_name, field_name, program_name FROM project natural join corporate_member"
      mycursor.execute(proj)
      values = mycursor.fetchall()
    
    if((int(nostartdate)==0)and(int(noenddate)==0)and(int(nocorporate)!=0)):
      proj= "SELECT DISTINCT(project_title), grant_amount, starting_date, ending_date, project_abstract, corporate_member.cfirst_name,corporate_member.clast_name, org_name, field_name, program_name FROM project natural join corporate_member WHERE (starting_date >= %s AND ending_date <= %s);"
      mycursor.execute(proj, (startdate, enddate))
      values = mycursor.fetchall()

    if((int(nostartdate)==0)and(int(noenddate)==1)and(int(nocorporate)==1)):
      proj= "SELECT DISTINCT(project_title), grant_amount, starting_date, ending_date, project_abstract, corporate_member.cfirst_name,corporate_member.clast_name, org_name, field_name, program_name FROM  project  natural join corporate_member WHERE (starting_date >= %s%s);"
      mycursor.execute(proj, (startdate,""))
      values = mycursor.fetchall()

    if((int(nostartdate)==1)and(int(noenddate)==0)and(int(nocorporate)==1)):
      proj= "SELECT DISTINCT(project_title), grant_amount, starting_date, ending_date, project_abstract, corporate_member.cfirst_name,corporate_member.clast_name,org_name, field_name, program_name FROM project natural join corporate_member WHERE (ending_date <= %s%s);"
      mycursor.execute(proj, (enddate,""))
      values = mycursor.fetchall()
      
    if((int(nostartdate)==1)and(int(noenddate)==1)and(int(nocorporate)==0)):
      for i in range(len(st1)):
        s3= st1[i]
        s4=st2[i]
        s5=st1[i]+" "+st2[i]
        if (s5 == corporate):
          proj= "SELECT DISTINCT(project_title), grant_amount, starting_date, ending_date, project_abstract, corporate_member.cfirst_name,corporate_member.clast_name, org_name, field_name, program_name FROM project NATURAL JOIN corporate_member WHERE ((corporate_member.cfirst_name = %s) AND (corporate_member.clast_name = %s));"
          mycursor.execute(proj, (s3,s4))
          values = mycursor.fetchall()
          break;
    if((int(nostartdate)==0)and(int(noenddate)==0)and(int(nocorporate)==0)):
      for i in range(len(st1)):
        s3= st1[i]
        s4=st2[i]
        s5=st1[i]+" "+st2[i]
        if (s5 == corporate):
          proj= "SELECT DISTINCT(project_title), grant_amount, starting_date, ending_date, project_abstract,corporate_member.cfirst_name,corporate_member.clast_name, org_name, field_name, program_name FROM project NATURAL JOIN corporate_member WHERE (starting_date >= %s AND ending_date <= %s AND (corporate_member.cfirst_name = %s) AND (corporate_member.clast_name = %s));"
          mycursor.execute(proj, (startdate,enddate,s3,s4))
          values = mycursor.fetchall()
          break;
    if((int(nostartdate)==0)and(int(noenddate)==1)and(int(nocorporate)==0)):
      for i in range(len(st1)):
        s3= st1[i]
        s4=st2[i]
        s5=st1[i]+" "+st2[i]
        if (s5 == corporate):
          proj= "SELECT DISTINCT(project_title), grant_amount, starting_date, ending_date, project_abstract, corporate_member.cfirst_name,corporate_member.clast_name, org_name, field_name, program_name FROM project NATURAL JOIN corporate_member WHERE (starting_date >= %s AND (corporate_member.cfirst_name = %s) AND (corporate_member.clast_name = %s));"
          mycursor.execute(proj, (startdate,s3,s4))
          values = mycursor.fetchall()
          break;
    if((int(nostartdate)==1)and(int(noenddate)==0)and(int(nocorporate)==0)):
      for i in range(len(st1)):
        s3= st1[i]
        s4=st2[i]
        s5=st1[i]+" "+st2[i]
        if (s5 == corporate):
          proj= "SELECT DISTINCT(project_title), grant_amount, starting_date, ending_date, project_abstract, corporate_member.cfirst_name,corporate_member.clast_name, org_name, field_name, program_name FROM project NATURAL JOIN corporate_member WHERE (ending_date <= %s AND (corporate_member.cfirst_name = %s) AND (corporate_member.clast_name = %s));"
          mycursor.execute(proj, (enddate,s3,s4))
          values = mycursor.fetchall()
          break;        
    return render_template("page1.html",values=values, header = header, corporate_names = corporate_names)


@app.route("/showresearcher/<tuxaio>",methods=["GET","POST"])
def index(tuxaio):
  header=["Researcher First Name","Researcher Last Name"]
  '''s1=''
  s2=''
  for i in range(7):
    s1=s1+tuxaio[i]
  for i in range(7,len(tuxaio)):
    s2=s2+tuxaio[i]
  s=s1+"    "+s2'''
  #tuxaio
  s1=''
  for letters in tuxaio:
    s1=s1+letters
  mycursor=mydb.cursor()
  res="SELECT DISTINCT (researcher.rfirst_name),researcher.rlast_name FROM project natural join researcher  WHERE project_title=%s;"
  mycursor.execute(res,[s1])
  researchers=mycursor.fetchall()
  return render_template("showresearcher.html",researchers=researchers,project=s1,header=header)








  
 #return render_template("check.html", startdate=startdate, enddate=enddate, corporate=nocorporate, values=values)

@app.route("/choosefield/",methods=["GET","POST"])
def choose():
  header=["Project Title","Researcher First Name","Researcher Last name"]
  mycursor=mydb.cursor()
  query="select field_name from scientific_field;"
  mycursor.execute(query)
  fields=mycursor.fetchall()
  s=[]
  results=[]
  for field in fields:
    for fiels in field:
      s.append(fiels)
  if request.method=="POST":
    field=request.form["field"]
    query2="SELECT project_title,researcher.rfirst_name ,researcher.rlast_name FROM project natural join researcher WHERE(YEAR(CURRENT_TIMESTAMP)-YEAR(project.starting_date)<=1) and field_name=%s and (project.ending_date>CURDATE());"
    mycursor.execute(query2,[field])
    results.append(mycursor.fetchall())
  return render_template("choosefield.html",header=header,fields=s,results=results)



@app.route("/viewresearchers",methods=["GET","POST"])
def viewr():
  if request.method=="POST":
    id=request.form.get("proj_name")
    return redirect(url_for("viewp",id=id))

  header=["Researcher First Name","Researcher Last name","Researcher Id","Show Projects"]
  mycursor=mydb.cursor()
  query="SELECT rfirst_name,rlast_name,researcher_id from researcher;"
  mycursor.execute(query)
  researchers=mycursor.fetchall()
  return render_template("viewresearchers.html",header=header,researchers=researchers)



@app.route("/viewp/<id>",methods=["GET","POST"])
def viewp(id):
  header=["Project Title"]
  id=int(id)
  mycursor=mydb.cursor()
  query="SELECT project_title from project  where researcher_id=%s;"
  mycursor.execute(query,[id])
  projects=mycursor.fetchall()
  return render_template("viewp.html",header=header,id=id,projects=projects)


@app.route("/viewor",methods=["GET","POST"])
def viewor():
  if request.method=="POST":
    org_name=request.form.get("org_name")
    return redirect(url_for("viewors",org_name=org_name))


  header=["Organization Name","Show Projects"]
  mycursor=mydb.cursor()
  query="SELECT DISTINCT org_name from organizations;"
  mycursor.execute(query)
  organizations=mycursor.fetchall()
  return render_template("viewor.html",header=header,organizations=organizations)



@app.route("/viewpor/<org_name>",methods=["GET","POST"])
def viewors(org_name):
  header=["Project Title"]
  mycursor=mydb.cursor()
  query="SELECT  DISTINCT project_title from project  where org_name=%s;"
  mycursor.execute(query,[org_name])
  projects=mycursor.fetchall()
  return render_template("viewpor.html",header=header,org_name=org_name,projects=projects)

@app.route("/youngs")
def youngs():
  header=["Researcher First name","Researcher Last Name","Researcher Date of Birth"]
  mycursor=mydb.cursor()
  query="SELECT researcher.rfirst_name,researcher.rlast_name,researcher.date_of_birth FROM project natural join researcher WHERE(year(CURRENT_TIMESTAMP)-year(date_of_birth)<40 and ending_date>CURDATE());"
  mycursor.execute(query)
  youngs=mycursor.fetchall()
  return render_template("youngs.html",header=header,youngs=youngs)



