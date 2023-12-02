from twilio.rest import Client
import os

def send_sms_alert(image_file):
    # Twilio credentials
    account_sid = 'ACe0a5331165b4c76425458d064d6418e0'
    auth_token = 'b4d21da21cd0de59a271f88155c98c97'
    twilio_phone_number = '+16305818955'
    recipient_phone_number = '+917620196708'  # The phone number to which you want to send the alert

    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    # Message content
    message_body = f"Alert! Accident detected: {image_file}"

    try:
        # Send SMS
        message = client.messages.create(
            body=message_body,
            from_=twilio_phone_number,
            to=recipient_phone_number
        )
        print(f"SMS sent successfully. SID: {message.sid}")
    except Exception as e:
        print(f"Error sending SMS: {str(e)}")

# Example usage:
# image_path = 'path/to/your/image.jpg'
# send_sms_alert(image_path)
