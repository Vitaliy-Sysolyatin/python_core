class Doctor:
    def treat(self):
        print("Врач проводит лечение")


class Surgeon(Doctor):
    def treat(self):
        print("Хирург проводит операцию")


class Dentist(Doctor):
    def treat(self):
        print("Дантист лечит зубы")


class Therapist(Doctor):
    def treat(self):
        print("Терапевт проводит лечение")

    def assign_doctor(self, patient):
        if patient.treatment_plan == 1:
            patient.doctor = Surgeon()
        elif patient.treatment_plan == 2:
            patient.doctor = Dentist()
        else:
            patient.doctor = Therapist()

        patient.doctor.treat()


class Patient:
    def __init__(self, treatment_plan):
        self.treatment_plan = treatment_plan
        self.doctor = None


patient = Patient(1)
therapist = Therapist()

therapist.assign_doctor(patient)
