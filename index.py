# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def main():
    my_email_address = os.environ.get("EMAIL_ADDRESS")
    api_key = os.environ.get('SENDGRID_API_KEY')

    message = Mail(from_email=my_email_address, to_emails=my_email_address)
    message.template_id = "d-c3aa70e759994d6cbbfed759ea22500c"

    SendGridAPIClient(api_key).send(message)


if __name__ == "__main__":
    main()
