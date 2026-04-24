app_name = "ems"
app_title = "EMS"
app_publisher = "Your Name"
app_description = "Event Management System"
app_email = "your@email.com"
app_license = "MIT"

doc_events = {
    "Registration": {
        "after_insert": "ems.api.after_registration"
    }
}


scheduler_events = {
    "daily": [
        "ems.api.send_event_reminders"
    ]
}
app_include_css = "/assets/ems/css/custom.css"
