# Contact Tracing Form class
class ContactForm:
    # Constructor
    def __init__(self):
        # Personal information
        self.first_name = ""
        self.last_name = ""
        self.phone_number = ""
        self.email_address = ""
        self.address = ""
        # Health information
        self.symptoms = ""
        self.symptom_onset = ""
        self.tested_positive = False
        self.test_date = ""
        self.test_result = ""
        # Contact information
        self.close_contacts = []    # List of close contacts in the last 14-days
        self.travel_history = []    # List of places visited
        # Consent
        self.consent = False

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