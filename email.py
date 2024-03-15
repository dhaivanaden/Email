"""
This module implements an email simulator using Object-Oriented Programming (OOP).
It includes an Email class and functions to populate an inbox, list emails, and read emails.
"""

class Email:
    """
    Class representing an email with sender's address, subject line, content, and read status.
    """
    def __init__(self, email_address, subject_line, email_content):
        """
        Initialize an Email instance with given address, subject line, and content.
        By default, the email is marked as unread (has_been_read = False).
        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        """
        Mark the email as read.
        """
        self.has_been_read = True

    def __str__(self):
        return f"From: {self.email_address}\nSubject: {self.subject_line}\nContent: {self.email_content}"

class EmailSimulator:
    """
    Class representing an email simulator with an inbox.
    """
    def __init__(self):
        self.inbox = []

    def populate_inbox(self):
        """
        Populate the inbox with three sample emails.
        """
        email1 = Email("sender1@example.com", "Hello", "Just saying hello.")
        email2 = Email("sender2@example.com", "Important", "This is an important email.")
        email3 = Email("sender3@example.com", "Spam", "This is a spam email.")
        self.inbox.extend([email1, email2, email3])

    def list_emails(self):
        """
        Print the subject line of each email in the inbox, along with a corresponding number.
        Unread emails are marked as such.
        """
        for idx, email in enumerate(self.inbox, start=1):
            print(f"{idx}. {'(Unread)' if not email.has_been_read else '        '} {email.subject_line}")

    def read_email(self, index):
        """
        Display the selected email and mark it as read.
        """
        if 1 <= index <= len(self.inbox):
            email = self.inbox[index-1]
            print(f"\n{'='*30}\n{email}\n{'='*30}")
            email.mark_as_read()
        else:
            print("\nInvalid email number.")

def run_email_simulator():
    """
    Run the email simulator.
    """
    email_simulator = EmailSimulator()
    email_simulator.populate_inbox()

    while True:
        print("\nList of Emails:")
        email_simulator.list_emails()

        user_choice = input('''\nWould you like to:
        1. Read an email
        2. Quit application
        Enter selection: ''').strip()

        if user_choice == '1':
            email_index = int(input("Enter the email number to read: "))
            email_simulator.read_email(email_index)

        elif user_choice == '2':
            print("\nQuitting application.")
            break

        else:
            print("\nOops - incorrect input.")

# Run the email simulator
run_email_simulator()
