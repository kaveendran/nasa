from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("index.html")

@app.route('/welcome',methods=["POST"])

def welcome():
    get_name = request.form.get("input")
    return render_template("next.html",name=get_name)



if __name__ == "__main__":
    app.run(debug=True)
