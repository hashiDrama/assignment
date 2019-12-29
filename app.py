from flask import Flask
import isTwoSidedPrime
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/isTwoSidedPrime/<inputNumber>')
def checkTwoSidedPrime(inputNumber):
    return str(isTwoSidedPrime.checkTwoSidedPrime(inputNumber))
if __name__ == "__main__":
    app.run(debug=True)