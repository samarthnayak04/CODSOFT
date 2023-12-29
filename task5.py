import tkinter as tk
from tkinter import simpledialog

class ContactBook:
    def __init__(self):
        self.contacts = []
        self.create_ui()

    def create_ui(self):
        self.window = tk.Tk()
        self.window.title("Contact Book")

        self.add_button = tk.Button(self.window, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(self.window, text="View Contacts", command=self.view_contacts)
        self.search_button = tk.Button(self.window, text="Search Contact", command=self.search_contact)
        self.delete_button = tk.Button(self.window, text="Delete Contact", command=self.delete_contact)

        self.add_button.pack()
        self.view_button.pack()
        self.search_button.pack()
        self.delete_button.pack()

        self.contact_list = tk.Listbox(self.window)
        self.contact_list.pack()

        self.window.mainloop()

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter Name:")
        phone = simpledialog.askstring("Input", "Enter Phone Number:")
        email = simpledialog.askstring("Input", "Enter Email:")
        address = simpledialog.askstring("Input", "Enter Address:")

        contact = {"name": name, "phone": phone, "email": email, "address": address}
        self.contacts.append(contact)

        print("Contact added successfully!")

    def view_contacts(self):
        self.contact_list.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter name or phone number to search:")
        found_contacts = []
        for contact in self.contacts:
            if search_term in contact["name"] or search_term in contact["phone"]:
                found_contacts.append(contact)
        if found_contacts:
            print("Found contacts:")
            for contact in found_contacts:
                print(f"- Name: {contact['name']}")
                print(f"- Phone: {contact['phone']}")
                print(f"- Email: {contact['email']}")
                print(f"- Address: {contact['address']}")
        else:
            print("No contacts found matching the search term.")
    def delete_contact(self):
        selected_contact = self.contact_list.curselection()
        if selected_contact:
            index = selected_contact[0]
            del self.contacts[index]
            self.view_contacts()  #

contact_book = ContactBook()
