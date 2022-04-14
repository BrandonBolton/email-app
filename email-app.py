import smtplib, csv


def email_message(name):
    return \
        f"""Hello {name}, 
    
        this is to test to make sure email messages are working 
        
        same with multi line.
        """


def send_email(name, email):

    print(email_message(name))
    print(f"Email successfully sent to {name} at {email}")


with open("contact_list.csv", 'r') as contact_list:
    """
    Opens the CSV file named contact_list.csv and skips over the first line. 
    After that, it iterates throughout the file pulling each name and 
    """
    reader = csv.reader(contact_list, delimiter=',')
    next(reader)
    for name, email in reader:
        print(f"Sending email to {name} at {email}")
        send_email(name, email)

