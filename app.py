from flask import Flask, render_template, request, redirect, url_for, jsonify,session
#from flask_session import Session
#from tinydb import TinyDB, Query
#import re
import requests
import random
#import redis
import os
#import requests

#pip install flask --user

app = Flask(__name__)


@app.route("/")

def index():
    return render_template("index.html")

@app.route("/onas")

def onas():
    return render_template("onas.html")

@app.route("/trgovina")

def trgovina():
    return render_template("trgovina.html")

@app.route("/blog")

def blog():
    return render_template("blog.html")

@app.route("/kontakt")

def kontakt():
    return render_template("kontakt.html")

@app.route("/admin")

def admin():
    return render_template("admin.html")

@app.route("/narocila")
def narocila():
    return render_template("narocila.html")

"""
# ---------- Prijava v admin ----------

userDict = {}
passwordDict = {}

userDict["admin"] = 1
passwordDict["admin"] = 1

@app.route("/loginTry", methods=["POST"])
def login():
    ime = request.form.get("ime") 
    geslo = request.form.get("geslo")  

    if ime in userDict and geslo in passwordDict:
        if userDict[ime] == passwordDict[geslo]:
            session['admin_mode'] = True
            return jsonify({"redirect_to": session['last_log_link']})  
        else:
            return jsonify({"error": "Vnešeno ime ali geslo je napačno"}), 400
    else:
        return jsonify({"error": "Vnešeno ime ali geslo je napačno"}), 400

 

# ---------- Dodajanje e-mail racuna v databazo TinyDB (za novice) ----------

@app.route("/poskusDodajanjaMail", methods=["POST"])
def poskusDodajanjaMail():
    mail = request.form.get("mail")
    print("heh")
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    mailTest = re.match(pattern, mail) is not None
    if (mailTest):
        User = Query()
        if len(narocnikiDB.search(User.mail == mail))==0:
            narocnikiDB.insert({"mail":mail})
        return jsonify(success=True)
    else:
        return jsonify(success=False)
"""

"""
# ---------- INSTAGRAM API  ---------- 
igtoken = ""
iguporabnik = ""
igapi = ""

def instagramapi():
    objave = {
        "fields": "id,caption,media_type,media_url,permalink",
        "access_token": igtoken,
        "limit": 6
    }

    odgovor = requests.get(igapi, params=objave)
    return odgovor.json().get("data", [])

@app.route("/blog")

def blog():
    poslji = instagramapi
    admin_mode = session.get('admin_mode', False)
    return render_template("blog.html", post=poslji,admin_mode=admin_mode)

@app.route("/api/poslji")

def apiposlji():
    poslji = instagramapi
    return jsonify(poslji)
"""
app.run(debug = True, port=5000)


