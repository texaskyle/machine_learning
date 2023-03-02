from flask import Flask, request, jsonify, render_template

app = Flask(__name__)  # creating a flask app


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/math', methods=['POST'])
def maths_operations():
    if request.method == 'POST':
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if operation == 'add':
            r = num1 + num2
            result = 'The addition of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)

        elif operation == 'substract':
            r = num1 - num2
            result = 'The substract of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)

        elif operation == 'multiply':
            r = num1 * num2
            result = 'The multiplication of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        elif operation == 'division':
            r = num1 / num2
            result = 'The division of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)

        return render_template('results.html', result=result)


@app.route('/via_postman', methods=['POST'])  # for calling the API from Postman/SOUPUI
def math_operation_via_postman():
    if request.method == 'POST':
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if operation == 'add':
            r = num1 + num2
            result = 'the sum of' + str(num1) + 'and' + str(num2) + 'is' + str(r)
        elif operation == 'substract':
            r = num1 - num2
            result = 'the subtraction of' + str(num1) + 'and' + str(num2) + 'is' + str(r)
        elif operation == 'multiply':
            r = num1 * num2
            result = 'the multiplication of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        elif operation == 'divide':
            r = num1 / num2
            result = 'the division of' + str(num1) + 'and' + str(num2) + 'is' + str(r)

        return jsonify(result)


if __name__ == '__main__':
    print('The app is working fine!')
    app.run()


