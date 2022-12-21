from flask import Flask, redirect, render_template, request, url_for
from block import *

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        name = request.form['lender']
        amount = request.form['amount']
        borrower = request.form['borrower']
        write_block(name=name, amount=amount, to_whom=borrower)
        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/checking', methods=["GET"])
def check():
    res = check_integrity()
    return render_template('index.html', results=res)


if __name__ == '__main__':
    app.run(debug=True)