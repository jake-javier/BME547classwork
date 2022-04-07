import logging
from flask import Flask, request, jsonify
from pymodm import MongoModel, fields, connect
from pymodm import errors as pymodm_errors

app = Flask(__name__)

# db = []


class Patient(MongoModel):
    name = fields.CharField()
    patient_id = fields.IntegerField(primary_key=True)
    blood_type = fields.CharField()
    tests = fields.DictField()


def init_server():

    logging.basicConfig(filename='health_db_server.log', level=logging.DEBUG, filemode='w')
    print('Connecting to database...')
    connect("mongodb+srv://jakejavier70:SRVfootball54@bme547.8bjgx.mongodb.net/health_db?retryWrites=true&w=majority")
    print("connection attempt finished")
    add_patient_to_db("Ann Ables", 101, "A+")
    add_patient_to_db("Bob Boyles", 202, "B-")


@app.route("/add_patient", methods=["POST"])
def add_patient():
    # get the data from the request
    in_data = request.get_json()
    # call other func to do request
    answer, status_code = add_patient_driver(in_data)
    # provide response
    return jsonify(answer), status_code


def add_patient_driver(in_data):

    expected_keys = ['name', 'id', 'blood_type']
    expected_types = [str, int, str]
    answer, status_code = validate_add_patient_input(in_data, expected_keys, expected_types)

    if status_code != 200:
        return answer, status_code
    add_patient_to_db(in_data["name"], in_data["id"], in_data["blood_type"])
    # print(db)
    return True, 200


def validate_add_patient_input(in_data, expected_keys, expected_types):
    if type(in_data) is not dict:
        return "The input was not a dictionary", 400
    for key, expected_type in zip(expected_keys, expected_types):
        if key not in in_data:
            error_message = "Key {} is missing".format(key)
            return error_message, 400
        if type(in_data[key]) is not expected_type:
            error_message = "Value of key {} is not of type {}".format(key, expected_type)
            return error_message, 400
        return True, 200


def add_patient_to_db(name, id, blood_type):
    # new_patient = {"name": name, "id": id, "blood_type": blood_type, "tests": {}}
    # db.append(new_patient)
    new_patient = Patient(name=name, patient_id=id, blood_type=blood_type)
    new_patient.save()
    return True


def get_test_from_database(patient_id):
    try:
        patient = Patient.objects.raw({"id": patient_id}).first()
    except pymodm_errors.DoesNotExist:
        return "Patient_id {} was not found".format(patient_id), 400
    return patient.tests, 200


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_results(patient_id):
    answer, status_code = validate_patient_id(patient_id)
    if status_code != 200:
        return answer, status_code
    for patient in Patient.objects.raw({}):
        if patient.patient_id == int(patient_id):
            return patient.tests, 200
    return "Patient id {} is not in database".format(patient_id), 400


def validate_patient_id(patient_id):
    try:
        patient_id_int = int(patient_id)
    except ValueError:
        return "Patient_id was not an integer", 400
    return patient_id_int, 200


if __name__ == '__main__':
    init_server()
    app.run()
