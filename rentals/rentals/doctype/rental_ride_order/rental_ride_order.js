// Copyright (c) 2025, Ajesh Meshram and contributors
// For license information, please see license.txt

frappe.ui.form.on("Rental_Ride_Order", {
  refresh(frm) {
    console.log("On refresh")
    if(frm.doc.status !== "Accepted"){
      frm.add_custom_button("Accept", () => {
        // status => Accepted
        frm.set_value("status", "Accepted");
        // save the form
        frm.save()
      },"Actions")
    }
    if(frm.doc.status !== "Rejected"){
      frm.add_custom_button("Reject", () => {
        // status => Accepted
        frm.set_value("status", "Rejected");
        // save the form
        frm.save()
      },"Actions")
    }
    
  },
});
