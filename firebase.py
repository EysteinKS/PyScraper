import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
from util import print_time

def get_time_now():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

class FirebaseConnection():
    def __init__(self, admin_key):
        print_time("Creating database connection")
        cred = credentials.Certificate(admin_key)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def set_data(self, col, doc, data):
        print_time(f"Saving document {col}/{doc}")
        doc_ref = self.db.collection(col).document(doc)
        doc_ref.set({"data": data, "timestamp": get_time_now()})
        print_time(f"Data saved")
    