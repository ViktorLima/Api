from flask import Flask, jsonify, request

app = Flask(__name__)

employee = [

    {
        'id': 1,
        'Name': 'Heloisa',
        'Occupation': 'Develop Jr',
        'Stack': 'Python'
    },
    {
        'id': 2,
        'Name': 'Victor',
        'Occupation': 'Develop Senior',
        'Stack': 'Python'
    },
    {
        'id': 3,
        'Name': 'Yanne',
        'Occupation': 'Develop Senior',
        'Stack': 'Python'
    },
]


# HOMEPAGE


@app.route('/employee/homepage')
def home_page_employee():
    return 'The API is on the air!'


# Method GET


@app.route('/employee', methods=['GET'])
def consult_employee():
    return jsonify(employee)


# Method GET/id


@app.route('/employee/<int:id>', methods=['GET'])
def consult_employee_id(id):
    for employees in employee:
        if employees.get('id') == id:
            return jsonify(employees)


# Method GET/id


@app.route('/employee/<int:id>', methods=['PUT'])
def edit_employee_by_id(id):
    edit_employee = request.get_json()
    for indice, employees in enumerate(employee):
        if employees.get('id') == id:
            employee[indice].update(edit_employee)
            return jsonify(employee[indice])


# Method POST


@app.route('/employee', methods=['POST'])
def create_employee():
    new_employee = request.get_json()
    employee.append(new_employee)
    return jsonify(employee)


# Method DELETE


@app.route('/employee/<int:id>', methods=['DELETE'])
def delete_employee(id):
    for indice, employees in enumerate(employee):
        if employees.get('id') == id:
            del employee[indice]
    return jsonify(employee)


app.run(port=5000, host='localhost', debug=True)
