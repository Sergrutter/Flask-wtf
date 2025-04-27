from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

list = [
    'инженер-строитель', 'пилот', 'строитель', 'экзобиолог', 'врач',
    'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите',
    'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог',
    'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов'
]


@app.route('/')
@app.route('/index/<title>')
def index(title="Миссия на Марс"):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('prof.html', prof=prof)


@app.route('/list_prof/<prm>')
def spis_prof(prm):
    return render_template('prof_list.html', list=list, prm=prm)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
