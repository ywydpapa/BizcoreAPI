from flask import Flask,jsonify,request,render_template,redirect,url_for
import comm.dbconn

app = Flask(__name__)

@app.route('/')
def denyaccess():  # put application's code here
    return "Not allowed to access"

@app.route('/usercheck')
def usercheck():
    compid = request.form.get('commpid')
    username = request.form.get('username')
    password = request.form.get('password')
    result = comm.dbconn.logincheck(compid, username, password)
    result = jsonify(result)
    return render_template("apitemp.html", result=result)

@app.route('/listsopp')
def listsopp():
    result = comm.dbconn.listsopp()
    return render_template("apitemp.html", result=result)

@app.route('/listsched')
def listsopp():
    result = comm.dbconn.listsopp()
    return render_template("apitemp.html", result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
