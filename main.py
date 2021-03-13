from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/table/<pol>/<age>')
def auto_answer(pol, age):
    return render_template('auto_answer.html', pol=pol, age=int(age), a=url_for('static', filename='css/style.css'))




if __name__ == '__main__':
    print('http://127.0.0.1:8080/table/male/28')
    app.run(port=8080, host='127.0.0.1')