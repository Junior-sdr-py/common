from flask import Flask, render_template, send_file
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())


@app.route('/nav')
def get_nav_page():
    return render_template("nav.html")


@app.route('/alarm_clock')
def get_alarm_page():
    for i in get_data():
        if i['title'] == 'Alarm clock':
            data = i
    return render_template("alarm_clock.html", data=data)


@app.route('/headphones')
def get_headphones_page():
    for i in get_data():
        if i['title'] == 'Headphones':
            data = i
    return render_template("headphones.html", data=data)

@app.route('/ipod')
def get_ipod_page():
    for i in get_data():
        if i['title'] == 'iPod':
            data = i
    return render_template("ipod.html", data=data)

@app.route('/calculator')
def get_calculator_page():
    for i in get_data():
        if i['title'] == 'Calculator':
            data = i
    return render_template("calculator.html", data=data)

@app.route('/сoffeemaker')
def get_coffe_page():
    for i in get_data():
        if i['title'] == 'Coffeemaker':
            data = i
    return render_template("сoffeemaker.html", data=data)

@app.route('/battery_charger')
def get_battery_page():
    for i in get_data():
        if i['title'] == 'Battery charger':
            data = i
    return render_template("battery_charger.html", data=data)
@app.route('/author')
def get_author():
    return render_template("author.html",data=[])


if __name__ == "__main__":
    app.run(debug=True)
