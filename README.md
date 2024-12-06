# automate_vaccination
A reminder that will inform you to get vaccination for your pet (after 6 months)
# Lucy Vaccination Reminder Script

This Python script serves as a vaccination reminder system for your pet, Lucy. It calculates a six-month interval from the last vaccination date and sends an email reminder when the date arrives.

## Features

- Automatically calculates the next vaccination due date based on a six-month interval.
- Sends an email reminder using SMTP when the due date is reached.
- Runs continuously to check the date daily.

## Requirements

- Python 3.8+
- Gmail account for sending emails (or other SMTP-supported email providers).
- Internet access for email functionality.

## Technologies Used

- **smtplib**: To send email notifications.
- **datetime**: For date and time manipulation.
- **dateutil.relativedelta**: To calculate six-month intervals.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Pooja389/automate_vaccination.git
   cd automate_vaccination

2. **update the start date**
   ```bash
   start_date = dt.datetime(2024, 9, 25).date()
   ```
3. **run the script**
   ```bash
   python automate.py      
