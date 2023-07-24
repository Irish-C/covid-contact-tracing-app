import re

# Contact Tracing Form class
class ContactForm:
    """ Methods """
    # PERSONAL INFORMATION
    def set_personal_information(self, first_name, last_name, phone_number, email_address, address):
        # Set fullname format
        self.__fullname = '{} {}'.format(first_name.capitalize(), last_name.capitalize())
        
        # set and validate phone number
        phone_number = re.sub(r'\D', '', phone_number)
        if len(phone_number) != 11:
            raise ValueError("Phone number must have 11 digits.")
        self.__phone_number = phone_number

        # set and validate email address
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email_address):
            raise ValueError("Invalid email address.")
        self.__email_address = email_address

        # set address
        self.__address = address

    # A method that sets health information
    def set_health_information(self, symptoms, symptom_onset, tested_positive, test_date="", test_result=""):
        self.__symptoms = symptoms
        self.__symptom_onset = symptom_onset
        self.__tested_positive = tested_positive
        self.__test_date = test_date
        self.__test_result = test_result

    # A method that add close contact into lists
    def add_close_contact(self, name, contact_details):
        self.close_contacts.append({'name': name, 'contact_details': contact_details})

    # A method that add travel history into lists
    def add_travel_history(self, location, date):
        self.travel_history.append({'location': location, 'date': date})

    # A method that sets consent to TRUE
    def give_consent(self):
        self.consent = True