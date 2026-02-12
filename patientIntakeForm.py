import FreeSimpleGUI as sg
import dataFunctions

def read_input_values(values):
    first_name = values["FIRST_NAME"]
    last_name = values["LAST_NAME"]
    date_of_birth = values["DATE_OF_BIRTH"]
    height = values["HEIGHT"]
    weight = values["WEIGHT"]
    is_taking_medication = values["IS_TAKING_MEDICATION"]
       
    create_patient = dataFunctions.create_patient(first_name, last_name, date_of_birth, height, weight, is_taking_medication)
    return create_patient
    


def create_layout():
    return [
    [sg.Text("First name"), sg.Input(key = "FIRST_NAME")],
    [sg.Text("Last name"), sg.Input(key = "LAST_NAME")],
    [sg.Text("Date of birth"), sg.Input(key ="DATE_OF_BIRTH"), sg.CalendarButton("Select date", format = '%Y/%m/%d')],
    [sg.Text("Height"), sg.Input(key = "HEIGHT")],
    [sg.Text("Weight"), sg.Input(key = "WEIGHT")],
    [sg.Text("Is taking medication?"), sg.Checkbox("Yes", key = "IS_TAKING_MEDICATION")],
    [sg.Cancel(), sg.Button("Save")]
]

def display_intake_form():
    patient_intake_layout = create_layout()
    patient_intake_window = sg.Window("New Patient Form", patient_intake_layout)

    was_save_successful = False

    event, values = patient_intake_window.read()
    while True:
        event, values = patient_intake_window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break  
        elif event == "Save":
            was_save_successful = read_input_values(values)
            if was_save_successful:
                print("Patient saved.")
                break
            else:
                print("Could not save patient due to invalid input(s)")

    patient_intake_window.close() 
    return was_save_successful
           
