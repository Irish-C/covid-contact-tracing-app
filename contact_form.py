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
        def set_personal_information(self):
            pass

        def set_health_information(self):
            pass

        def set_contact_information(self):
            pass

        def add_close_contact(self):
            pass

        def add_travel_history(self):
            pass

        def give_consent(self):
            pass