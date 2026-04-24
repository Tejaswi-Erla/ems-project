import frappe
from frappe.utils import now_datetime

@frappe.whitelist()
def get_upcoming_events():
    return frappe.db.count("Event", {
        "starts_on": (">", now_datetime())
    })
