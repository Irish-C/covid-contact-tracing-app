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
        self.close_contacts = []
        self.travel_history = []
        # Consent
        self.consent = False