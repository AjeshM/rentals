# Copyright (c) 2025, Ajesh Meshram and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Rental_Ride_Booking(Document):
    def validate(self):
        if not self.rate:
            self.rate = frappe.db.get_single_value("Rentals Settings", "standard_rate")
            # frappe.get_single("Rentals Settings").standard_rate
            # frappe.db.get_singles_dict("Rentals Settings")
            # frappe.throw("Please provide the rate!!")
        total_distance = 0
        for item in self.items:
            total_distance += item.distance

        self.total_amount = total_distance * self.rate
