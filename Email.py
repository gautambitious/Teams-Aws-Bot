import credentials
class Email:
    def __init__(self, recipient):
        self.user = credentials.email
        self.pwd = credentials.password
        self.recipient = recipient
        self.body = "Teams Bot Email bruh!"

    def __send_email(self, user, pwd, recipient, subject, body):
        import smtplib
        if '@' not in credentials.email:
            print("Edit credentials.py to recieve Emails")
            return
        FROM = user
        TO = recipient if isinstance(recipient, list) else [recipient]
        SUBJECT = subject
        TEXT = body

        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(user, pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            print('successfully sent the mail')
        except Exception as e:
            print(e)
            print("failed to send mail")

    def success(self):
        self.__send_email(self.user, self.pwd, self.recipient,
                          "Teams Bot Running Started", self.body)

    def failure(self):
        self.__send_email(self.user, self.pwd, self.recipient,
                          "Teams Bot Running Failed", self.body)
