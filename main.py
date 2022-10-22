from flask import Flask,render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("about.html")



@app.route('/Laptops')
def Laptops():
    return render_template("laptops.html")




@app.route('/Tvs')
def Tvs():
    return render_template("tvs.html")


@app.route('/Electronics')
def Electronics():
    return render_template("Electronics.html")



@app.route('/cloths')
def cloths():
    return render_template("cloths.html")


if __name__ == '__main__':
    app.run(debug=True)