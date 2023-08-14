


class Doctor:
    def __init__(self, doctor_id, doctor_name, doctor_specilist, doctor_timing, doctor_qualification, doctor_roomNb):
        self.id = doctor_id
        self.name = doctor_name
        self.specilist = doctor_specilist
        self.timing = doctor_timing
        self.qualification = doctor_qualification
        self.roomNb = doctor_roomNb

# Implement one getter function for each Doctor property. The getter function should return the value of the property.
    def get_doctor_id(self):
        return self.id
    
    def get_doctor_name(self):
        return self.name
    
    def get_doctor_specialist(self):
        return self.specilist
    
    def get_doctor_timing(self):
        return self.timing
    
    def get_doctor_qualification(self):
        return self.qualification
    
    def get_doctor_roomNb(self):
        return self.roomNb

# Implement one setter function for each Doctor property. The setter function should set the property to a new value. 
    def set_doctor_id(self, new_id):
        self.id = new_id
        
    def set_doctor_name(self, new_name):
        self.name = new_name

    def set_doctor_specilist(self, new_specilist):
        self.specilist = new_specilist

    def set_doctor_timing(self, new_timing):
        self.timing = new_timing

    def set_doctor_qualification(self, new_qualification):
        self.qualification = new_qualification

    def set_doctor_roomNb(self, new_roomNb):
        self.roomNb = new_roomNb

# It returns the string representation of a doctor object. 
    def __str__(self):
        return f"{self.id}_{self.name}_{self.specilist}_{self.timing}_{self.qualification}_{self.roomNb}"
    
    
#######################################################################################################

class DoctorManager:
    def __init__(self):
        self.doctor_list = []
        self.read_doctor_file()
        
    def read_doctor_file(self):
        doctor_file = open('doctors.txt', 'r')
        lines = doctor_file.readlines()

        for line in lines:
            doctor_data = line.strip().split('_')
            if len(doctor_data) == 6:
                doctor = Doctor(*doctor_data)
                self.doctor_list.append(doctor)

    def format_dr_info(self, doctor):
        return f"{doctor.get_doctor_id()}_{doctor.get_doctor_name()}_{doctor.get_doctor_specialist()}_{doctor.get_doctor_timing()}_{doctor.get_doctor_qualification()}_{doctor.get_doctor_roomNb()}"

    def enter_dr_info(self):
        doctor_id = input("Enter the doctor’s ID: ")
        doctor_name = input("Enter the doctor’s name: ")
        doctor_specialist = input("Enter the doctor’s specility: ")
        doctor_timing = input("Enter the doctor’s timing (e.g., 7am-10pm): ")
        doctor_qualification = input("Enter the doctor’s qualification: ")
        doctor_roomNb = input("Enter the doctor’s room number: ")

        new_doctor = Doctor(doctor_id, doctor_name, doctor_specialist, doctor_timing, doctor_qualification, doctor_roomNb)
        self.doctor_list.append(new_doctor)
        print(f'Doctor whose ID is {doctor_id} has been added')
        return new_doctor
    

    def search_doctor_by_id(self, target_id):
        for doctor in self.doctor_list:
            if doctor.get_doctor_id() == target_id:
                return doctor
        return None
    
    def search_doctor_by_name(self, target_name):
        for doctor in self.doctor_list:
            if doctor.get_doctor_name() == target_name:
                return doctor
        return None
    
    def edit_doctor_info(self):
        doctor_id = input("Enter the doctor ID you want to edit: ")
        found_doctor = self.search_doctor_by_id(doctor_id)
        
        if found_doctor:
            new_name = input("Enter new Name: ")
            new_specialist = input("Enter new Specialist: ")
            new_timing = input("Enter new Timing: ")
            new_qualification = input("Enter new Qualification: ")
            new_roomNb = input("Enter new Room Number: ")

            found_doctor.set_doctor_name(new_name)
            found_doctor.set_doctor_specialist(new_specialist)
            found_doctor.set_doctor_timing(new_timing)
            found_doctor.set_doctor_qualification(new_qualification)
            found_doctor.set_doctor_roomNb(new_roomNb)

            self.update_doctors_file()
            print("Doctor information updated successfully.")
        else:
            print("Cannot find the doctor with the entered ID.")


    def write_list_of_doctor_to_file(self):
        with open('doctors.txt', 'w') as doctor_file:
            for doctor in self.doctor_list:
                doctor_file.write(str(doctor) + '\n')   

    def display_doctor_info(self, doctor):
        print("Id   Name                   Speciality      Timing          Qualification   Room Number")
        print(f"{doctor.get_doctor_id():<4} {doctor.get_doctor_name():<22} {doctor.get_doctor_specialist():<15} {doctor.get_doctor_timing():<15} {doctor.get_doctor_qualification():<15} {doctor.get_doctor_roomNb()}")

    def display_doctors_list(self):
        print(f"{'Id':<4} {'Name':<22} {'Speciality':<15} {'Timing':<15} {'Qualification':<15} {'Room Number'}")
        for doctor in self.doctor_list:
            print(f"{doctor.get_doctor_id():<4} {doctor.get_doctor_name():<22} {doctor.get_doctor_specialist():<15} {doctor.get_doctor_timing():<15} {doctor.get_doctor_qualification():<15} {doctor.get_doctor_roomNb()}")

    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        self.doctor_list.append(new_doctor)

        with open('doctors.txt', 'a') as doctor_file:
            formatted_info = self.format_dr_info(new_doctor)
            doctor_file.write('\n' + formatted_info)

        print("New doctor added successfully.")

class Management:
    def __init__(self):
        self.doctor_manager = DoctorManager()

    def doctors_menu(self):
        while True:
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
                search_id = input("Enter the doctor ID: ")
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
            print("\nPatients Menu:")
            print("1 - Display Patients list")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient info")
            print("5 - Back to the Main Menu")
            choice = input(">>> ")

            if choice == '1':
                pass  # Implement Display Patients list
            elif choice == '2':
                pass  # Implement Search for patient by ID
            elif choice == '3':
                pass  # Implement Add patient
            elif choice == '4':
                pass  # Implement Edit patient info
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def display_menu(self):
        while True:
            print("\nSelect from the following options, or select 3 to stop:")
            print("1 - Doctors")
            print("2 - Patients")
            print("3 - Exit Program")
            choice = input(">>> ")

            if choice == '1':
                self.doctors_menu()
            elif choice == '2':
                self.patients_menu()
            elif choice == '3':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

management = Management()
management.display_menu()
