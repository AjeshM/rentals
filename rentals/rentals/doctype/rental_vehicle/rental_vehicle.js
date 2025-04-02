// Copyright (c) 2025, Ajesh Meshram and contributors
// For license information, please see license.txt

frappe.ui.form.on("Rental_Vehicle", {
  refresh(frm) {
  },
  get_summary(frm) {
    frm.get_field("summary").$wrapper.append("<h1>Here is your summary.</h1>")
  }
});
