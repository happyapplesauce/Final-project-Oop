
#######################################################################################################
# Doctor #

# Constructor to initialize Doctor properties.
class Doctor:
    def __init__(self, doctor_id, doctor_name, doctor_specialist, doctor_timing, doctor_qualification, doctor_roomNb):
        self.id = doctor_id
        self.name = doctor_name
        self.specialist = doctor_specialist
        self.timing = doctor_timing
        self.qualification = doctor_qualification
        self.roomNb = doctor_roomNb

# Implement one getter function for each Doctor property. The getter function should return the value of the property.
# Getter functions for Doctor properties.
# These functions return the respective property values.
    def get_doctor_id(self):
        return self.id
    def get_doctor_name(self):
        return self.name
    def get_doctor_specialist(self):
        return self.specialist
    def get_doctor_timing(self):
        return self.timing
    def get_doctor_qualification(self):
        return self.qualification
    def get_doctor_roomNb(self):
        return self.roomNb

# Implement one setter function for each Doctor property. The setter function should set the property to a new value.
# Setter functions for Doctor properties.
# These functions set new values for the respective properties.
    def set_doctor_id(self, new_id):
        self.id = new_id
    def set_doctor_name(self, new_name):
        self.name = new_name
    def set_doctor_specialist(self, new_specialist):
        self.specialist = new_specialist
    def set_doctor_timing(self, new_timing):
        self.timing = new_timing
    def set_doctor_qualification(self, new_qualification):
        self.qualification = new_qualification
    def set_doctor_roomNb(self, new_roomNb):
        self.roomNb = new_roomNb

# It returns the string representation of a doctor object. 
    def __str__(self):
        return f"{self.id}_{self.name}_{self.specialist}_{self.timing}_{self.qualification}_{self.roomNb}"
    

class DoctorManager:
    def __init__(self):
    # Initialize an empty list of doctors and read data from a file.
        self.doctor_list = []
        self.read_doctor_file()
    
    # Function to read doctor data from doctors.txt.
    def read_doctor_file(self):
        doctor_file = open('doctors.txt', 'r')
        lines = doctor_file.readlines() # Read lines from the file, split data, and create Doctor objects.

        for line in lines:
            doctor_data = line.strip().split('_')
            if len(doctor_data) == 6:
                doctor = Doctor(*doctor_data)
                self.doctor_list.append(doctor) # Append Doctor objects to the doctor_list.
        doctor_file.close() # Close the file when done.

    # This formatted string is used when writing the doctor's information to a file.
    def format_dr_info(self, doctor):
        return f"{doctor.get_doctor_id()}_{doctor.get_doctor_name()}_{doctor.get_doctor_specialist()}_{doctor.get_doctor_timing()}_{doctor.get_doctor_qualification()}_{doctor.get_doctor_roomNb()}"

    # prompts the user to input various properties of a doctor
    # It then creates a new Doctor instance using the provided data and returns the newly created doctor object. 
    # This function is used when adding a new doctor to the list.
    def enter_dr_info(self):
        doctor_id = input("\nEnter the doctor’s ID: ")
        doctor_name = input("Enter the doctor’s name: ")
        doctor_specialist = input("Enter the doctor’s speciality: ")
        doctor_timing = input("Enter the doctor’s timing (e.g., 7am-10pm): ")
        doctor_qualification = input("Enter the doctor’s qualification: ")
        doctor_roomNb = input("Enter the doctor’s room number: ")

        new_doctor = Doctor(doctor_id, doctor_name, doctor_specialist, doctor_timing, doctor_qualification, doctor_roomNb)
        print(f'\nDoctor whose ID is {doctor_id} has been added')
        return new_doctor
    
    #  searches the list of doctors for a doctor with a specific ID (target_id). 
    #  It iterates through the doctor_list and compares the target_id with the ID of each doctor in the list.
    def search_doctor_by_id(self, target_id):
        for doctor in self.doctor_list:
            if doctor.get_doctor_id() == target_id:
                return doctor
        return None
    
    # This function works similarly to search_doctor_by_id, but instead of searching by ID it search the name 
    def search_doctor_by_name(self, target_name):
        for doctor in self.doctor_list:
            if doctor.get_doctor_name() == target_name:
                return doctor
        return None
    

    def edit_doctor_info(self):
        doctor_id = input("Please enter the id of the doctor that you want to edit their information: ")
        # Prompt the user to input the ID of the doctor to be edited.
        found_doctor = self.search_doctor_by_id(doctor_id)
        # Search for the doctor using the entered ID.
        
        # If the doctor is found, prompt the user to enter new information.
        if found_doctor:
            new_name = input("Enter new Name: ")
            new_specialist = input("Enter new Specialist: ")
            new_timing = input("Enter new Timing: ")
            new_qualification = input("Enter new Qualification: ")
            new_roomNb = input("Enter new Room Number: ")

        # Update the doctor's properties with the new information.
            found_doctor.set_doctor_name(new_name)
            found_doctor.set_doctor_specialist(new_specialist)
            found_doctor.set_doctor_timing(new_timing)
            found_doctor.set_doctor_qualification(new_qualification)
            found_doctor.set_doctor_roomNb(new_roomNb)

        # Write the updated list of doctors to the file.
            self.write_list_of_doctor_to_file()
            print(f"\nDoctor whose ID is {doctor_id} has been edited")
        else:
            print("Cannot find the doctor with the entered ID.")

    # Write each doctor's information as a string to a file.
    def write_list_of_doctor_to_file(self):
        with open('doctors.txt', 'w') as doctor_file:
            for doctor in self.doctor_list:
                doctor_file.write(str(doctor) + '\n')   

    # Display the doctor's information in a formatted way.
    def display_doctor_info(self, doctor):
        print("\nId   Name                   Speciality      Timing          Qualification   Room Number")
    # The <a number part is a format specifier that means "left-align the text and use a minimum width of requested characters.
        print(f"\n{doctor.get_doctor_id():<4} {doctor.get_doctor_name():<22} {doctor.get_doctor_specialist():<15} {doctor.get_doctor_timing():<15} {doctor.get_doctor_qualification():<15} {doctor.get_doctor_roomNb()}")

    # Display the doctor's list in a formatted way.
    def display_doctors_list(self):
        for doctor in self.doctor_list:
            print(f"{doctor.get_doctor_id():<4} {doctor.get_doctor_name():<22} {doctor.get_doctor_specialist():<15} {doctor.get_doctor_timing():<15} {doctor.get_doctor_qualification():<15} {doctor.get_doctor_roomNb()}\n")

    # Append the new doctor to the doctor list.
    # Write the updated list of doctors to the file.
    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        self.doctor_list.append(new_doctor)

        with open('doctors.txt', 'a') as doctor_file:
            formatted_info = self.format_dr_info(new_doctor)
            doctor_file.write('\n' + formatted_info)



#######################################################################################################
# Patient #

# Constructor to initialize patient properties.
class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

# Implement one getter function for each Doctor property. The getter function should return the value of the property.
# Getter functions for Doctor properties.
# These functions return the respective property values.
    def get_pid(self):
        return self.pid
    def get_name(self):
        return self.name    
    def get_disease(self):
        return self.disease
    def get_gender(self):
        return self.gender
    def get_age(self):
        return self.age

# Implement one setter function for each patient property. The setter function should set the property to a new value.
# Setter functions for patient properties.
# These functions set new values for the respective properties.
    def set_pid(self, new_pid):
        self.pid = new_pid
    def set_name(self, new_name):
        self.name = new_name
    def set_disease(self, new_disease):
        self.disease = new_disease
    def set_gender(self, new_gender):
        self.gender = new_gender
    def set_age(self, new_age):
        self.age = new_age

# It returns the string representation of a patient object. 
    def __str__(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"

class PatientManager:
    def __init__(self):
    # Initialize an empty list of patients and read data from a file.
        self.patient_list = []
        self.read_patients_file()

    # Function to read doctor data from patients.txt.
    def format_patient_info_for_file(self, patient):
        return f"{patient.get_pid()}_{patient.get_name()}_{patient.get_disease()}_{patient.get_gender()}_{patient.get_age()}"


    # prompts the user to input various properties of a patient
    def enter_patient_info(self):
        patient_id = input("\nEnter patient ID: ")
        patient_name = input("Enter patient name: ")
        patient_disease = input("Enter patient disease: ")
        patient_gender = input("Enter patient gender: ")
        patient_age = input("Enter patient age: ")
    # It then creates a new Patient instance using the provided data and returns the newly created patient object.
        new_patient = Patient(patient_id, patient_name, patient_disease, patient_gender, patient_age)
    # This function is used when adding a new patient to the list.
        self.patient_list.append(new_patient)
        print(f'\nPatient whose ID is {patient_id} has been added.')
        return new_patient

    def read_patients_file(self):
        patient_file = open('patients.txt', 'r')
        lines = patient_file.readlines()

    # Read lines from the file, split data, and create Patient objects.
        for line in lines:
            patient_data = line.strip().split('_')
            if len(patient_data) == 5:
                patient = Patient(*patient_data)
                self.patient_list.append(patient)

    #  searches the list of patients for a patient with a specific ID (target_id). 
    #  It iterates through the patient_list and compares the target_id with the ID of each patient in the list.
    def search_patient_by_id(self, target_id):
        for patient in self.patient_list:
            if patient.get_pid() == target_id:
                return patient
        return None

    # Display the patient's information in a formatted way.
    def display_patient_info(self, patient):
        print("\nId   Name                   Disease         Gender          Age")
        print(f"\n{patient.get_pid():<4} {patient.get_name():<22} {patient.get_disease():<15} {patient.get_gender():<15} {patient.get_age()}")


    def edit_patient_info_by_id(self):
        patient_id = input("\nPlease enter the id of the Patient that you want to edit their information: ")
        # Prompt the user to input the ID of the patient to be edited.
        patient = self.search_patient_by_id(patient_id)
        # Search for the patient using the entered ID.
        
        # If the patient is found, prompt the user to enter new information.
        if patient:
            new_name = input("Enter new Name: ")
            new_disease = input("Enter new Disease: ")
            new_gender = input("Enter new Gender: ")
            new_age = input("Enter new Age: ")

        # Update the patient's properties with the new information.
            patient.set_name(new_name)
            patient.set_disease(new_disease)
            patient.set_gender(new_gender)
            patient.set_age(new_age)

        # Write the updated list of patients to the file.
            self.write_list_of_patients_to_file()
            print(f'Patient whose ID is {patient_id} has been edited.')
        else:
            print("Cannot find the patient with the entered ID.")

    # Display the patient's list in a formatted way.
    def display_patients_list(self):
        for patient in self.patient_list: 
            print(f"{patient.get_pid():<4} {patient.get_name():<22} {patient.get_disease():<15} {patient.get_gender():<15} {patient.get_age()}\n")

    # Write each pateient's information as a string to a file.
    def write_list_of_patients_to_file(self):
        with open('patients.txt', 'w') as patient_file:
            for patient in self.patient_list:
                formatted_info = self.format_patient_info_for_file(patient)
                patient_file.write(formatted_info + '\n')

    # Append the new patient to the patient list.
    # Write the updated list of patients to the file.
    def add_patient_to_file(self):
        self.enter_patient_info()
        self.write_list_of_patients_to_file()


###################################################################################



class Management:
    def __init__(self):
        # Create an instance of DoctorManager to manage doctors.
        self.doctor_manager = DoctorManager()
        # Create an instance of PatientManager to manage patients.
        self.patient_manager = PatientManager()

    def doctors_menu(self):
        while True:
        # Display a menu for managing doctors and perform actions based on user input.
            print("\nDoctors Menu:")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add doctor")
            print("5 - Edit doctor info")
            print("6 - Back to the Main Menu")
            choice = input(">>> ")
        
            if choice == '1':
                self.doctor_manager.display_doctors_list()
            elif choice == '2':
                search_id = input("\nEnter the doctor ID: ")
                found_doctor = self.doctor_manager.search_doctor_by_id(search_id)
                if found_doctor:
                    self.doctor_manager.display_doctor_info(found_doctor)
                else:
                    print("Can't find the doctor with the same ID on the system")
            elif choice == '3':
                search_name = input("Enter the doctor name: ")
                found_doctor = self.doctor_manager.search_doctor_by_name(search_name)
                if found_doctor:
                    self.doctor_manager.display_doctor_info(found_doctor)
                else:
                    print("Can't find the doctor with the same name on the system")
            elif choice == '4':
                self.doctor_manager.add_dr_to_file()
            elif choice == '5':
                self.doctor_manager.edit_doctor_info()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def patients_menu(self):
        while True:
        # Display a menu for managing patients and perform actions based on user input.
            print("\nPatients Menu:")
            print("1 - Display Patients list")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient info")
            print("5 - Back to the Main Menu")
            choice = input(">>> ")

            if choice == '1':
                self.patient_manager.display_patients_list()  
            elif choice == '2':
                search_id = input("\nEnter the patient ID: ")
                found_patient = self.patient_manager.search_patient_by_id(search_id)
                if found_patient:
                    self.patient_manager.display_patient_info(found_patient)
                else:
                    print("Can't find the Patient with the same id on the system")
            elif choice == '3':
                self.patient_manager.add_patient_to_file()  
            elif choice == '4':
                self.patient_manager.edit_patient_info_by_id()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please select a valid option.")


    def display_menu(self):
        while True:
        # Display the main menu of the hospital management system and handle user choices.
            print("\nWelcome to Alberta Hospital (AH) Managment system \nSelect from the following options, or select 3 to stop:")
            print("1 - Doctors")
            print("2 - Patients")
            print("3 - Exit Program")
            choice = input(">>> ")

            if choice == '1':
            # Call the doctors_menu function to manage doctors.
                self.doctors_menu()
            elif choice == '2':
            # Call the patients_menu function to manage patients.
                self.patients_menu()
            elif choice == '3':
            # Exit the loop and end the program.
                print("Thanks for using the program. Bye!")
                break
            else:
            # Display an error message for invalid input.
                print("Invalid choice. Please select a valid option.")

#######################################################################################################




management = Management()
management.display_menu()