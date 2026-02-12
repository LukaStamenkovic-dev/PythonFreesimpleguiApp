import FreeSimpleGUI as sg
import dataFunctions
import patientIntakeForm

table_data = dataFunctions.convert_patients_to_table_data()

def press_add_patient_button(patients_window):
    was_save_successful = patientIntakeForm.display_intake_form()
    if was_save_successful:
        table_data = dataFunctions.convert_patients_to_table_data()
        patients_window["PATIENTS_TABLE"].update(values = table_data)

table_headings = [
    "First Name", "Last Name", "Date of birth", "Height", "Weight", "Is taking medication?"
    ]

patients_window_layout = [
    [sg.Text("All Patient Data"), sg.Button("Add new patient")],
    [sg.Table(headings = table_headings, values = table_data, key = "PATIENTS_TABLE")]
]
patients_window = sg.Window("Patient list", patients_window_layout)

while True:
    event, values = patients_window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Add new patient":
        press_add_patient_button(patients_window)
patients_window.close()