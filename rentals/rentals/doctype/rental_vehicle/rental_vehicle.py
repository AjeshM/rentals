# Copyright (c) 2025, Ajesh Meshram and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator


# class Rental_Vehicle(Document):
#     pass


class Rental_Vehicle(WebsiteGenerator):
    def before_save(self):
        self.set_title()

    def set_title(self):
        self.title = f"{self.make} {self.model} {self.year}"
