from flask import *
from Hypergeometric import hypergeofunc
from ErrorHandler import hypergeofunchandler

app = Flask(__name__)

@app.route('/hypergeometric_calculator', methods=["POST","GET"])
def page():

    if request.form.get("successes") or request.form.get("input") != None:
        successes = int(request.form.get("successes"))
        input = int(request.form.get("input"))
        error = hypergeofunchandler(input, 7, 100, successes)
        if error :
            return render_template(
                "hypergeo.html", successes = successes, input = input, error = error)  
        result = hypergeofunc(input, 7, 100, successes)
        return render_template(
            "hypergeo.html", result = result, input = input, successes = successes)

    return render_template("hypergeo.html")

 


@app.route('/')
def redir_to_index():

    return redirect(url_for("static", filename="index.html"))


