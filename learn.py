from flask import *  
from sympy import *

x, y = symbols('x y')

app = Flask(__name__)  
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

@app.route('/integrationw/<string:e>/<string:ll>/<string:ul>')
def integrationw(e,ll,ul):
    exp = e
    expr1 = integrate(e, (x,ll,ul)).doit()
    kp = str(expr1)
    yo = {
        "number":kp
    }
    return jsonify(yo)





  
  
if __name__ == '__main__':  
    app.run(debug = True)  