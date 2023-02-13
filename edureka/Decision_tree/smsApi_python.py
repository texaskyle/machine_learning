# works with both python 2 and 3
from __future__ import print_function

import africastalking


class SMS:
    def __init__(self):
		# Set your app credentials
	    self.username = "evans3345"
        self.api_key = "f1fb7660d9ffcee4ac4c12d34c5e615ad29d9b2eba911ac4e6ee42487273f32a"

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self):
            # Set the numbers you want to send to in international format
            recipients = ["+254713YYYZZZ", "+254733YYYZZZ"]

            # Set your message
            message = "I'm a lumberjack and it's ok, I sleep all night and I work all day";

            # Set your shortCode or senderId
            sender = "shortCode or senderId"
            try:
				# Thats it, hit send and we'll take care of the rest.
                response = self.sms.send(message, recipients, sender)
                print (response)
            except Exception as e:
                print ('Encountered an error while sending: %s' % str(e))

if __name__ == '__main__':
    SMS().send()