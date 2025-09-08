# app.py
from flask import Flask, render_template, request, jsonify
import calculator  # uses your file above

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate_route():
    data = request.get_json() or {}
    op = data.get("operation")
    nums = data.get("numbers", [])

    try:
        if op == "add":
            res = calculator.add(nums[0], nums[1])
        elif op == "subtract":
            res = calculator.subtract(nums[0], nums[1])
        elif op == "multiply":
            res = calculator.multiply(nums[0], nums[1])
        elif op == "divide":
            res = calculator.divide(nums[0], nums[1])
        elif op == "modulus":
            res = calculator.modulus(nums[0], nums[1])
        elif op == "power":
            res = calculator.power(nums[0], nums[1])
        elif op == "squarert":
            res = calculator.squarert(nums[0])
        elif op == "fact":
            res = calculator.fact(nums[0])
        elif op == "logarithm":
            res = calculator.logarithm(nums[0])
        elif op == "evenodd":
            res = calculator.even_or_odd(nums[0])
        elif op == "prime":
            res = calculator.is_prime(nums[0])
        elif op == "reverse":
            res = calculator.rev_num(nums[0])
        elif op == "countdigits":
            res = calculator.Count_Digits(nums[0])
        elif op == "simple_interest":
            res = calculator.simple_interest(nums[0], nums[1], nums[2])
        elif op == "compound_interest":
            res = calculator.compound_interest(nums[0], nums[1], nums[2])
        else:
            return jsonify(error="Invalid operation"), 400

        return jsonify(result=res)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(debug=True)
