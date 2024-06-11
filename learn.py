from flask import *
from sympy import *
from flask_cors import CORS

x, y = symbols('x y')

app = Flask(__name__)  
CORS(app)  # Enable CORS for all routes
@app.route('/derivation/<string:n>')  
def derivation(n):  
       
    expr = n
    expr_diff = Derivative(expr, x).doit() 
    k = str(expr_diff)
    m = {
        "number":k
    }
    return jsonify(m)

@app.route('/integrationwo/<string:m>')
def integration(m):
    exp = m
    expr1 = integrate(exp, x)
    kp = str(expr1)
    yo = {
        "number":kp
    }
    return jsonify(yo)

if __name__ == '__main__':  
    app.run(debug=True)  
