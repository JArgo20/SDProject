from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display="", pageTitle='Loan Calculator')

@app.route('/loan', methods=['GET', 'POST'])
def loan():
    if request.method == 'POST':
        form = request.form
        A = float(form['numOne'])
        numPmt = float(form['numTwo'])
        numYears = float(form['numThree'])
        intRate = float(form['numFour'])
        n = numPmt * numYears
        i = (intRate / 100) / numPmt
        D = ((( 1 + i )**n ) - 1 ) / ( i * ( 1 + i)**n )
        calc = A / D
        calc = (round(calc, 2))
        return render_template('index.html', display=calc, pageTitle='Loan Calculator')
   
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)