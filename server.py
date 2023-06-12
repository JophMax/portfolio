from flask import Flask, render_template, request, redirect
import os
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def Hello_World():
    return render_template("index.html")

@app.route("/<string:page_name>")
def funcion_ir(page_name):
    return render_template(page_name)

def funcion_dict(diction):
    with open("database.txt", "a") as file:
        file.write(f"\n {diction['email']}, {diction['subject']}, {diction['message']}")

def funcion_dict_csv(diction):
    with open("database.csv", "a", newline='') as file_csv:
        escritor_csv = csv.writer(file_csv, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        escritor_csv.writerow([diction["email"],diction["subject"],diction["message"]])

        

@app.route("/submit_form", methods=["POST", "GET"])
def form_guardar():
    if request.method == 'POST':
        try:
            nuevo_dict = request.form.to_dict()
            funcion_dict(nuevo_dict)
            funcion_dict_csv(nuevo_dict)
            return redirect("thankyou.html")
        except:
            return "Los datos no se guardaron en la base de datos"
    else:
        return "Ha ocurrido un error. Intenta de nuevo"