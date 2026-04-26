Hello,

Here is your Weekly Event Summary:

Event: {{ doc.event }}

Participant: {{ frappe.get_doc("Participant", doc.participant).full_name }}

Event Date: {{ frappe.utils.formatdate(doc.event_date) }}

Status: {{ doc.status }}

Thank you.