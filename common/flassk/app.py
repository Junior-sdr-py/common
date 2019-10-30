from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('home.html')


@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/vegetables')
def vegetables_page():
    vegetable_lst = ["beans", "carrot", "beetroot", "cucumber"]
    return render_template('vegetables.html', list=vegetable_lst)


@app.route('/fruits')
def fruits_page():
    fruit_lst = ['melon', 'apple', 'strawberry', 'grape ']
    return render_template('fruits.html', list=fruit_lst)


if __name__ == "__main__":
    app.run(debug=True)
