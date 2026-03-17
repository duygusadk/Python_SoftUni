class Email:
    def __init__(self, sender, receiver, content):
        self.is_sent = False
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_sent = True

    def get_info(self):
        return (f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
                )


line = input()
emails = []
while line != "Stop":
    lines = line.split()
    sender = lines[0]
    receiver = lines[1]
    content = lines[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    line = input()

send_emails = list(map(lambda x: int(x), input().split(", ")))

for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())
