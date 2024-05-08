class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
    
    def mark_as_read(self):
        self.has_been_read = True

inbox = []

def  populate_inbox():
    
    inbox.append(Email("sender@example.com","Welcome to HyperionDev!", "Hello There"))
    inbox.append(Email("course@example.com", "Great work on the bootcamp!", "Good Job" ))
    inbox.append(Email("cogrammar@example.com", "Your excellent marks", "Great work"))
    
def list_emails():
    for i, email in enumerate(inbox):
        print(f"{i+1}. {email.subject_line}")
        
def read_email(index):
    email = inbox[index - 1]
    email.mark_as_read()
    print(f"From: {email.email_address}")
    print(f"Subject: {email.subject_line}")
    print(f"Content: {email.email_content}")

def main():
    populate_inbox()
    while True:
        print("Menu:")
        print("1. Read an email")
        print("2. View unread emails")
        print("3. Quit application")
        choice = input("Enter your choice:")
        
        if choice =="1":
            list_emails()
            index = int(input("Enter the index of the email you want to read: "))
            read_email(index)
        elif choice == "2":
            pass
        elif choice == "3":
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
main()