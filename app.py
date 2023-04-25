from flask import Flask,render_template,request
from main import solve
app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/calculate",methods=["POST"])
def calculate():
    feed_conc = request.form["feed_conc"]
    feed_flowrate = request.form["feed_flowrate"]
    feed_temperature = request.form["feed_temperature"]
    pressure = request.form["pressure"]
    distillate = request.form["distillate"]
    no_trays = request.form["no_trays"]
    feed_location = request.form["feed_location"]
    reflux = request.form["reflux"]
    Type = request.form["type"]

    val1,val2 = solve(feed_conc,feed_temperature,pressure,feed_flowrate,feed_location,distillate,no_trays,Type,reflux)
    return render_template("output.html",Vj_new=val1,Tj_new=val2)

app.run('0.0.0.0',8001,debug=True)