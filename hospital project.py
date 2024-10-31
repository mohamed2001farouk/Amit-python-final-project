class Person:
    """Base class for all people in the hospital."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def view_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Patient(Person):
    """Class for patients in the hospital."""
    
    def __init__(self, name, age, medical_record):
        super().__init__(name, age)
        self.medical_record = medical_record
    
    def view_record(self):
        return f"Medical Record: {self.medical_record}"


class Staff(Person):
    """Class for staff members in the hospital."""
    
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position
    
    def view_info(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}"


class Department:
    """Class representing a department in the hospital."""
    
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.staff = []
    
    def add_patient(self, patient):
        if isinstance(patient, Patient):
            self.patients.append(patient)
    
    def add_staff(self, staff_member):
        if isinstance(staff_member, Staff):
            self.staff.append(staff_member)
    
    def view_patients(self):
        return [patient.view_info() for patient in self.patients]
    
    def view_staff(self):
        return [staff.view_info() for staff in self.staff]


class Hospital:
    """Class representing a hospital."""
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []
    
    def add_department(self, department):
        if isinstance(department, Department):
            self.departments.append(department)
    
    def view_departments(self):
        return [dept.name for dept in self.departments]
    

if __name__ == "__main__":
    # Create hospital
    hospital = Hospital("City Hospital", "123 Main St")

    # Create departments
    cardiology = Department("Cardiology")
    neurology = Department("Neurology")

    # Add departments to hospital
    hospital.add_department(cardiology)
    hospital.add_department(neurology)

    # Create patients and staff
    patient1 = Patient("Alice", 30, "Record A123")
    patient2 = Patient("Bob", 45, "Record B456")
    staff1 = Staff("Dr. Smith", 50, "Cardiologist")
    staff2 = Staff("Nurse Nancy", 35, "Neurology Nurse")

    # Add patients and staff to departments
    cardiology.add_patient(patient1)
    cardiology.add_staff(staff1)
    neurology.add_patient(patient2)
    neurology.add_staff(staff2)

    # View hospital details
    print(f"Hospital: {hospital.name}, Location: {hospital.location}")
    print("Departments:", hospital.view_departments())
    
    # View department details
    print("\nCardiology Patients:", cardiology.view_patients())
    print("Cardiology Staff:", cardiology.view_staff())
    print("\nNeurology Patients:", neurology.view_patients())
    print("Neurology Staff:", neurology.view_staff())
