// Copyright (c) 2025, Ajesh Meshram and contributors
// For license information, please see license.txt

frappe.ui.form.on("Rental_Ride_Booking", {
  refresh(frm) {

  },
  rate(frm) {
    // recalculate total
    frm.trigger("update_total_amount")
  },
  update_total_amount(frm){
    let total_d = 0;
    for (let item of frm.doc.items) {
      total_d += item.distance
    }
    const amount = frm.doc.rate * total_d
    frm.set_value("total_amount", amount)
  }
});
frappe.ui.form.on("Rental_Ride_Booking_Item", {
  refresh(frm) {

  },
  // 
  // 
  distance(frm, cdt, cdn) {
    // console.log(cdt, cdn)
    // console.log(frappe.get_doc(cdt,cdn))
    // my_child = frappe.get_doc(cdt,cdn)
    // frappe.model.set_value(cdt,cdn,"source","Updated Source")
    frm.trigger("update_total_amount")
  },
  items_remove(frm){
    frm.trigger("update_total_amount")
  }
});