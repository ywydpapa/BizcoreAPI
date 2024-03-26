from flask import Flask,jsonify,request,render_template,redirect,url_for
import comm.dbconn
import comm.dbconncu
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/')
def denyaccess():  # put application's code here
    return "Not allowed to access"

@app.route('/usercheck')
def usercheck():
    username = request.form.get('username')
    password = request.form.get('password')
    result = comm.dbconn.logincheck(username, password)
    result = jsonify(result)
    return render_template("apitemp.html", result=result)

@app.route('/listsopp')
def listsopp():
    result = comm.dbconn.listsopp()
    return render_template("apitemp.html", result=result)

@app.route('/detailsopp/<soppno>')
def detailsopp(soppno):
    result = comm.dbconn.detailsopp(soppno)
    return render_template("apitemp.html", result=result)

@app.route('/listcont')
def listcont():
    result = comm.dbconn.listcont()
    return render_template("apitemp.html", result=result)

@app.route('/detailcont/<contno>')
def detailcont(contno):
    result = comm.dbconn.detailcont(contno)
    return render_template("apitemp.html", result=result)

@app.route('/listcust')
def listcust():
    result = comm.dbconn.listcust()
    return render_template("apitemp.html", result=result)

@app.route('/detailcust/<custno>')
def detailcust(custno):
    result = comm.dbconn.detailcust(custno)
    return render_template("apitemp.html", result=result)

@app.route('/listsales')
def listsales():
    result = comm.dbconn.listsales()
    return render_template("apitemp.html", result=result)

@app.route('/listsched')
def listsched():
    result = comm.dbconn.listsched()
    return render_template("apitemp.html", result=result)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
