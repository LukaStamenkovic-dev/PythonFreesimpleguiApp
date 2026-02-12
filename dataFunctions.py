from patient import Paitient
from datetime import datetime



patients = [
    Paitient("Zivko", "Zivkovic", datetime(1990, 4, 5), 187, 80.5, False),
    Paitient("Marko", "Markovic", datetime(1994, 6, 10), 193, 73.3, False),
    Paitient("Ivan", "Ivkovic", datetime(1992, 12, 29), 175, 94.0, False)
]

def convert_patients_to_table_data():
    patients_data = []
    for patient in patients:
        patients_data.append(patient.convert_values_to_strings())
    return patients_data

def create_patient(first_name, last_name, date_of_birth, height, weight, is_taking_medication):
    if len(first_name) < 2 or len(last_name) < 2 or date_of_birth == "" or height == "" or weight == "":
        return False
    try:
        date_of_birth = datetime.strptime(date_of_birth, "%Y/%m/%d")
        if date_of_birth > datetime.now():
            return False
        height = int(height)
        weight = float(weight)
        if height <= 0 or weight <= 0:
            return False
        is_taking_medication = True if is_taking_medication == "True" else False

        patient = Paitient(first_name, last_name, date_of_birth, height, weight, is_taking_medication)
        patients.append(patient)
        return True
    except:
        return False