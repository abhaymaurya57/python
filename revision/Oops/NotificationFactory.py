class Email:

    def send(self,message):
        print(f"Email Sent: {message}")

class SMS:

    def send(self,message):
        print(f"SMS Sent: {message}")

class PushNotification:

    def send(self,message):
        print(f"Push Notification Sent: {message}")


class NotificationFactory:

    @staticmethod
    def get_notification(notification_type):

        if notification_type.lower()=="email":
            return Email()
        
        elif notification_type.lower()=="sms":
            return SMS()
        
        elif notification_type.lower()=="push":
            return PushNotification()

        else:
            raise ValueError("Invalid Notification Type")
        
notification = NotificationFactory.get_notification("email")
notification.send("Welcome to WorkSphere")
print()

notification = NotificationFactory.get_notification("sms")
notification.send("Your OTP is 1234")
print()

notification = NotificationFactory.get_notification("push")
notification.send("You have a new message")