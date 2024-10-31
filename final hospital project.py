class Person:
    def __init__(self, name: str, age: int):
        # Initialize a person's name and age
        self.name = name  
        self.age = age    

    def view_info(self) -> str:
        # Return a string representation of the person's basic information
        return f'Name: {self.name}, Age: {self.age}'


class Staff(Person):
    def __init__(self, name: str, age: int, position: str):
        # Initialize staff with name, age, and position
        super().__init__(name, age)
        self.position = position  

    def view_info(self) -> str:
        # Return a string representation of the staff's information, including position
        return f'{super().view_info()}, Position: {self.position}'


class Patient(Person):
    def __init__(self, name: str, age: int, medical_record: str):
        # Initialize patient with name, age, and medical record
        super().__init__(name, age)
        self.medical_record = medical_record  

    def view_record(self) -> str:
        # Return the patient's medical record as a string
        return f'Medical Record: {self.medical_record}'


class Hospital:
    def __init__(self, name: str, location: str):
        # Initialize hospital with name and location
        self.name = name  
        self.location = location  
        self.departments = []  # List to store departments in the hospital

    def add_department(self, department: 'Department') -> None:
        # Add a department to the hospital's departments list
        self.departments.append(department)

    def __str__(self) -> str:
        # Return a string representation of the hospital's name and location
        return f'Hospital Name: {self.name}, Location: {self.location}'


class Department:
    def __init__(self, name: str):
        # Initialize department with a name
        self.name = name  
        self.patients = []  # List to store patients in the department
        self.staff = []  # List to store staff in the department

    def add_patient(self, patient: Patient) -> None:
        # Add a patient to the department's patients list
        self.patients.append(patient)

    def add_staff(self, staff_member: Staff) -> None:
        # Add a staff member to the department's staff list
        self.staff.append(staff_member)

    def __str__(self) -> str:
        # Return a string representation of the department's name
        return f'Department Name: {self.name}'


# Main function to demonstrate the functionality of the classes
def main():
    # Get hospital information from the user
    hospital_name = input("Enter hospital name: ")
    hospital_location = input("Enter hospital location: ")
    hospital = Hospital(hospital_name, hospital_location)

    # Get department information and create department
    dept_name = input("Enter department name: ")
    department = Department(dept_name)
    hospital.add_department(department)

    # Get patient information and add to department
    patient_name = input("Enter patient name: ")
    patient_age = int(input("Enter patient age: "))
    medical_record = input("Enter patient medical record: ")
    patient = Patient(patient_name, patient_age, medical_record)
    department.add_patient(patient)

    # Get staff information and add to department
    staff_name = input("Enter staff member name: ")
    staff_age = int(input("Enter staff member age: "))
    position = input("Enter staff member position: ")
    staff = Staff(staff_name, staff_age, position)
    department.add_staff(staff)

    # Display hospital information
    print("\n--- Hospital Information ---")
    print(hospital)

    # Display department information
    print("\n--- Department Information ---")
    print(department)

    # Display patient information
    print("\n--- Patient Information ---")
    print(patient.view_info())
    print(patient.view_record())

    # Display staff information
    print("\n--- Staff Information ---")
    print(staff.view_info())


# Run the main function only if this script is run directly
if __name__ == "__main__":
    main()
