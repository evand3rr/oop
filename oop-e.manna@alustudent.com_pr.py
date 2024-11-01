#!/usr/bin/bash
class Patient:
    def __init__(self, patient_id, name, age, gender, admission_date, condition):
        self.id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.admission_date = admission_date
        self.condition = condition

    def get_details(self):
        return (f"Patient ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Admission Date: {self.admission_date}\n"
                f"Condition: {self.condition}")

def count_patients(patient_list):
    return len(patient_list)

def list_patient_names(patient_list):
    return [patient.name for patient in patient_list]

def print_patient_by_id(patient_list):
    patient_id = int(input("Enter patient ID: "))
    for patient in patient_list:
        if patient.id == patient_id:
            print(patient.get_details())
            return
    print("Patient not found.")

# Creating multiple patient objects
patient1 = Patient(1, "Davina Reese", 24, "Female", "2024-03-27", "Pneumonia")
patient2 = Patient(2, "Ravi Singh", 26, "Male", "2024-05-10", "Sprained ankle")
patient3 = Patient(3, "Kim Soo Hyuk", 30, "Male", "2024-04-06", "Malaria")

# Storing them in a list
patients = [patient1, patient2, patient3]

# Count the number of patients
print(f"Total number of patients: {count_patients(patients)}")

# List all patient names
print("Patient Names:", list_patient_names(patients))

# Optional: Print patient details by ID
print_patient_by_id(patients)    