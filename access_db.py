from pymodm import connect

connect("mongodb+srv://jakejavier70:SRVfootball54@bme547.8bjgx.mongodb.net/health_db?retryWrites=true&w=majority")


def get_database_record():
    from database_info import Patient
    patient = Patient.objects.raw({"_id": 101}).first()
    print(patient.name)


def put_new_record():
    from health_db_server import Patient
    new_patient = Patient(name="David", patient_id=1)
    new_patient.save()


if __name__ == '__main__':
    get_database_record()
