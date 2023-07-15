# Contact Tracing Form class
class ContactForm:
    # Constructor
    def __init__(self):
        # Personal information
        self.__first_name = ""
        self.__last_name = ""
        self.__phone_number = ""
        self.__email_address = ""
        self.__address = ""
        # Health information
        self.__symptoms = ""
        self.__symptom_onset = ""
        self.__tested_positive = False
        self.__test_date = ""
        self.__test_result = ""
        # Contact information
        self.__close_contacts = []    # List of close contacts in the last 14-days
        self.__travel_history = []    # List of places visited
        # Consent
        self.__consent = False


        """ Methods """
        # A method that sets personal information of the respondent
        def set_personal_information(self, first_name, last_name, phone_number, email_address, address):
            self.__first_name = first_name
            self.__last_name = last_name
            self.__phone_number = phone_number
            self.__email_address = email_address
            self.__address = address

        # A method that sets health information of the respondent
        def set_health_information(self, symptoms, symptom_onset, tested_positive, test_date="", test_result=""):
            self.__symptoms = symptoms
            self.__symptom_onset = symptom_onset
            self.__tested_positive = tested_positive
            self.__test_date = test_date
            self.__test_result = test_result

        def add_close_contact(self, name, contact_details):
            self.close_contacts.append({'name': name, 'contact_details': contact_details})

        def add_travel_history(self, location, date):
            self.travel_history.append({'location': location, 'date': date})

        def give_consent(self):
            self.consent = True