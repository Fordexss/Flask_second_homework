from flask import Flask, render_template

app = Flask('Oderman', template_folder="templates", static_folder="static")

menu_items = [
    {"name": "Маргарита", "description": "Томатний соус, моцарела, базилік", "price": 100},
    {"name": "Пепероні", "description": "Томатний соус, пепероні, моцарела", "price": 120},
    {"name": "Гавайська", "description": "Томатний соус, курка, ананас, моцарела", "price": 130},
    {"name": "Чотири сири", "description": "Томатний соус, гауда, пармезан, дор-блю, моцарела", "price": 150},
    {"name": "Вегетаріанська", "description": "Томатний соус, гриби, перець, помідор, моцарела", "price": 110},
]


@app.route('/')
@app.route('/index')
def index():
    pizza_name = "Oderman"
    return render_template("index.html", pizza_name=pizza_name)


@app.route('/menu')
def menu():
    return render_template("menu.html", menu_items=menu_items)


@app.route('/aboutUs')
def about_us():
    return render_template('about_us.html', title='Про нас', header='Інформація про нас')


if __name__ == "__main__":
    app.run(debug=True)
