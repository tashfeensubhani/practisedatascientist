from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def calculator():
    result = ""
    num1 = num2 = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
        except:
            result = "Invalid Operator"
    return render_template("calculator.html", result=result, num1=num1,num2=num2, operation=operation)
if __name__ == "__main__":
    app.run(debug=True)
