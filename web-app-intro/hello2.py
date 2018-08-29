from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
def ftoc(ftemp):
   return (ftemp-32.0)*(5.0/9.0)
def MtoKm(miles):
    return (miles*1.609344)


@app.route('/ftoc/<ftempString>')
def convertFtoC(ftempString):
    ftemp = 0.0
    try:
        ftemp = float(ftempString)
        ctemp = ftoc(ftemp)
        return "In Farenheit: " + ftempString + " In Celsius " + str(ctemp) 
    except ValueError:
        return "Sorry.  Could not convert " + ftempString + " to a number"


@app.route('/MtoKm/<milesString>')
def convertMtoKm(milesString):
    miles = 0.0
    try:
        miles = float(milesString)
        km = MtoKm(miles)
        return "In miles: " + milesString + " In Kilometers " +str(km)
    except ValueError:
        return "Sorry. Could not convert " + milesString + "to a number"
    
@app.route('/')
def renderMain():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(port=5000)
