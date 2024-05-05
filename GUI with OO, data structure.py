import pickle
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import os

class GUI:
    '''class to represent a GUI form to enter the employee, events, clients, guests, suppliers and venues details '''
    def __init__(self, master):
        self.master = master
        self.master.title("Event Management System")
        self.create_widgets()
        self.employees = [] # List to store employee data
        self.events = []  # List to store event data
        self.clients = []  # List to store clients data
        self.guests = []  # List to store guests data
        self.suppliers = []  # List to store suppliers data
        self.venues = []  # List to store venues data

    def create_widgets(self):
        # Frame for employee operations
        employee_frame = tk.Frame(self.master)
        employee_frame.pack()
        tk.Label(employee_frame, text="Employee Operations").pack()
        # Create entry fields for employee data
        self.create_entry_fields(employee_frame, "Employee")
        # Buttons for employee operations
        delete_employee_button = tk.Button(employee_frame, text="Delete Employee", command=self.delete_employee)
        delete_employee_button.pack()
        modify_employee_button = tk.Button(employee_frame, text="Modify Employee", command=self.modify_employee)
        modify_employee_button.pack()
        display_employee_button = tk.Button(employee_frame, text="Display Employee", command=self.display_employee)
        display_employee_button.pack()

        # Frame for event operations
        event_frame = tk.Frame(self.master)
        event_frame.pack()
        tk.Label(event_frame, text="Event Operations").pack()
        # Create entry fields for event data
        self.create_entry_fields(event_frame, "Event")
        # Buttons for event operations
        delete_event_button = tk.Button(event_frame, text="Delete Event", command=self.delete_event)
        delete_event_button.pack()
        modify_event_button = tk.Button(event_frame, text="Modify Event", command=self.modify_event)
        modify_event_button.pack()
        display_event_button = tk.Button(event_frame, text="Display Event", command=self.display_event)
        display_event_button.pack()

        # Frame for client operations
        client_frame = tk.Frame(self.master)
        client_frame.pack()
        tk.Label(client_frame, text="Client Operations").pack()
        # Create entry fields for client data
        self.create_entry_fields(client_frame, "Client")
        # Buttons for client operations
        delete_client_button = tk.Button(client_frame, text="Delete Client", command=self.delete_client)
        delete_client_button.pack()
        modify_client_button = tk.Button(client_frame, text="Modify Client", command=self.modify_client)
        modify_client_button.pack()
        display_client_button = tk.Button(client_frame, text="Display Client", command=self.display_client)
        display_client_button.pack()

        # Frame for guest operations
        guest_frame = tk.Frame(self.master)
        guest_frame.pack()
        tk.Label(guest_frame, text="Guest Operations").pack()
        # Create entry fields for guest data
        self.create_entry_fields(guest_frame, "Guest")
        # Buttons for guest operations
        delete_guest_button = tk.Button(guest_frame, text="Delete Guest", command=self.delete_guest)
        delete_guest_button.pack()
        modify_guest_button = tk.Button(guest_frame, text="Modify Guest", command=self.modify_guest)
        modify_guest_button.pack()
        display_guest_button = tk.Button(guest_frame, text="Display Guest", command=self.display_guest)
        display_guest_button.pack()

        # Frame for supplier operations
        supplier_frame = tk.Frame(self.master)
        supplier_frame.pack()
        tk.Label(supplier_frame, text="Supplier Operations").pack()
        # Create entry fields for supplier data
        self.create_entry_fields(supplier_frame, "Supplier")
        # Buttons for supplier operations
        delete_supplier_button = tk.Button(supplier_frame, text="Delete Supplier", command=self.delete_supplier)
        delete_supplier_button.pack()
        modify_supplier_button = tk.Button(supplier_frame, text="Modify Supplier", command=self.modify_supplier)
        modify_supplier_button.pack()
        display_supplier_button = tk.Button(supplier_frame, text="Display Supplier", command=self.display_supplier)
        display_supplier_button.pack()

        # Frame for venue operations
        venue_frame = tk.Frame(self.master)
        venue_frame.pack()
        tk.Label(venue_frame, text="Venue Operations").pack()
        # Create entry fields for venue data
        self.create_entry_fields(venue_frame, "Venue")
        # Buttons for venue operations
        delete_venue_button = tk.Button(venue_frame, text="Delete Venue", command=self.delete_venue)
        delete_venue_button.pack()
        modify_venue_button = tk.Button(venue_frame, text="Modify Venue", command=self.modify_venue)
        modify_venue_button.pack()
        display_venue_button = tk.Button(venue_frame, text="Display Venue", command=self.display_venue)
        display_venue_button.pack()

    def create_entry_fields(self, parent, entity):
        # Create entry fields (text boxes) for input data related to the specified entity
        tk.Label(parent, text=f"{entity} ID:").pack()
        entry_var = tk.StringVar()
        entry = tk.Entry(parent, textvariable=entry_var)
        entry.pack()
        add_button = tk.Button(parent, text=f"Add {entity}", command=lambda: self.add_entity(entity, entry_var.get()))
        add_button.pack()

    def create_entry_fields(self, parent, entity):
        tk.Label(parent, text=f"{entity} ID:").pack()
        entry_var = tk.StringVar()
        entry = tk.Entry(parent, textvariable=entry_var)
        entry.pack()
        add_button = tk.Button(parent, text=f"Add {entity}", command=lambda: self.add_entity(entity, entry_var.get()))
        add_button.pack()

    def add_entity(self, entity, ID):
        if entity == "Employee":
            # Gather employee details
            employee_ID = simpledialog.askstring("Input", "Enter employee ID")
            name = simpledialog.askstring("Input", "Enter employee name")
            department = simpledialog.askstring("Input", "Enter employee department")
            job_title = simpledialog.askstring("Input", "Enter employee job title")
            basic_salary = simpledialog.askfloat("Input", "Enter employee basic salary")
            age = simpledialog.askinteger("Input", "Enter employee age")
            date_of_birth = simpledialog.askstring("Input", "Enter employee date of birth")
            passport_details = simpledialog.askstring("Input", "Enter employee passport details")
            employee_type = simpledialog.askinteger("Input", "Enter employee type")
            employee = Employee(employee_ID, name, department, job_title, basic_salary, age, date_of_birth, passport_details, employee_type)
            self.employees.append(employee)
        elif entity == "Event":
            # Gather event details
            event_ID = simpledialog.askstring("Input", "Enter event ID")
            event_type = simpledialog.askstring("Input", "Enter event type")
            theme = simpledialog.askstring("Input", "Enter event theme")
            date = simpledialog.askstring("Input", "Enter event date")
            venue_address = simpledialog.askstring("Input", "Enter event venue address")
            client_ID = simpledialog.askstring("Input", "Enter client ID")
            invoice = simpledialog.askfloat("Input", "Enter event invoice")
            employee_ID = simpledialog.askstring("Input", "Enter employee ID")
            caterer = simpledialog.askstring("Input", "Enter caterer name")
            event = Event(event_ID, event_type, theme, date, venue_address, client_ID, invoice, employee_ID, caterer)
            self.events.append(event)
        elif entity == "Client":
            # Gather client details
            client_ID = simpledialog.askstring("Input", "Enter client ID")
            name = simpledialog.askstring("Input", "Enter client name")
            address = simpledialog.askstring("Input", "Enter client address")
            contact_details = simpledialog.askstring("Input", "Enter client contact details")
            budget = simpledialog.askfloat("Input", "Enter client budget")
            client = Client(client_ID, name, address, contact_details, budget)
            self.clients.append(client)
        elif entity == "Guest":
            # Gather guest details
            guest_ID = simpledialog.askstring("Input", "Enter guest ID")
            name = simpledialog.askstring("Input", "Enter guest name")
            address = simpledialog.askstring("Input", "Enter guest address")
            contact_details = simpledialog.askstring("Input", "Enter guest contact details")
            guest = Guest(guest_ID, name, address, contact_details)
            self.guests.append(guest)
        elif entity == "Supplier":
            # Gather supplier details
            supplier_ID = simpledialog.askstring("Input", "Enter supplier ID")
            name = simpledialog.askstring("Input", "Enter supplier name")
            contact_details = simpledialog.askstring("Input", "Enter supplier contact details")
            product_category = simpledialog.askstring("Input", "Enter supplier product category")
            address = simpledialog.askstring("Input", "Enter supplier address")
            email = simpledialog.askstring("Input", "Enter supplier email")
            delivery_time = simpledialog.askstring("Input", "Enter supplier delivery time")
            bank_details = simpledialog.askstring("Input", "Enter supplier bank details")
            supplier = Supplier(supplier_ID, name, contact_details, product_category, address, email, delivery_time, bank_details)
            self.suppliers.append(supplier)
        elif entity == "Venue":
            # Gather venue details
            venue_ID = simpledialog.askstring("Input", "Enter venue ID")
            name = simpledialog.askstring("Input", "Enter venue name")
            address = simpledialog.askstring("Input", "Enter venue address")
            contact = simpledialog.askstring("Input", "Enter venue contact")
            min_guests = simpledialog.askinteger("Input", "Enter minimum guests")
            max_guests = simpledialog.askinteger("Input", "Enter maximum guests")
            venue = Venue(venue_ID, name, address, contact, min_guests, max_guests)
            self.venues.append(venue)

    def delete_employee(self):
        # to delete an employee from the list
        employee_ID = simpledialog.askstring("Input", "Enter employee ID to delete")
        for employee in self.employees:
            if employee.employee_ID == employee_ID:
                self.employees.remove(employee)
                messagebox.showinfo("Success", "Employee deleted successfully")
                return
        messagebox.showerror("Error", "Employee not found")

    def modify_employee(self):
        # to modify employee details
        employee_ID = simpledialog.askstring("Input", "Enter employee ID to modify")
        for employee in self.employees:
            if employee.employee_ID == employee_ID:
                name = simpledialog.askstring("Input", "Enter new employee name")
                department = simpledialog.askstring("Input", "Enter new employee department")
                job_title = simpledialog.askstring("Input", "Enter new employee job title")
                basic_salary = simpledialog.askfloat("Input", "Enter new employee basic salary")
                age = simpledialog.askinteger("Input", "Enter new employee age")
                date_of_birth = simpledialog.askstring("Input", "Enter new employee date of birth")
                passport_details = simpledialog.askstring("Input", "Enter new employee passport details")
                employee_type = simpledialog.askinteger("Input", "Enter new employee type")
                employee = Employee(employee_ID, name, department, job_title, basic_salary, age, date_of_birth, passport_details, employee_type)
                self.employees.remove(employee)
                self.employees.append(employee)
                messagebox.showinfo("Success", "Employee modified successfully")
                return
        messagebox.showerror("Error", "Employee not found")

    def display_employee(self):
        #to display employee information
        employee_ID = simpledialog.askstring("Input", "Enter employee ID to display")
        for employee in self.employees:
            if employee.employee_ID == employee_ID:
                messagebox.showinfo("Employee Details", f"Employee ID: {employee.employee_ID}\nName: {employee.name}\nDepartment: {employee.department}\nJob Title: {employee.job_title}\nBasic Salary: {employee.basic_salary}\nAge: {employee.age}\nDate of Birth: {employee.date_of_birth}\nPassport Details: {employee.passport_details}\nEmployee Type: {employee.employee_type}")
                return
        messagebox.showerror("Error", "Employee not found")

    def delete_event(self):
        #to delete an event from the list
        event_ID = simpledialog.askstring("Input", "Enter event ID to delete")
        for event in self.events:
            if event.event_ID == event_ID:
                self.events.remove(event)
                messagebox.showinfo("Success", "Event deleted successfully")
                return
        messagebox.showerror("Error", "Event not found")

    def modify_event(self):
        #to modify event details
        event_ID = simpledialog.askstring("Input", "Enter event ID to modify")
        for event in self.events:
            if event.event_ID == event_ID:
                event_type = simpledialog.askstring("Input", "Enter new event type")
                theme = simpledialog.askstring("Input", "Enter new event theme")
                date = simpledialog.askstring("Input", "Enter new event date")
                venue_address = simpledialog.askstring("Input", "Enter new event venue address")
                client_ID = simpledialog.askstring("Input", "Enter new client ID")
                invoice = simpledialog.askfloat("Input", "Enter new event invoice")
                employee_ID = simpledialog.askstring("Input", "Enter new employee ID")
                caterer = simpledialog.askstring("Input", "Enter new caterer name")
                event = Event(event_ID, event_type, theme, date, venue_address, client_ID, invoice, employee_ID, caterer)
                self.events.remove(event)
                self.events.append(event)
                messagebox.showinfo("Success", "Event modified successfully")
                return
        messagebox.showerror("Error", "Event not found")

    def display_event(self):
        #to display event information
        event_ID = simpledialog.askstring("Input", "Enter event ID to display")
        for event in self.events:
            if event.event_ID == event_ID:
                messagebox.showinfo("Event Details", f"Event ID: {event.event_ID}\nEvent Type: {event.event_type}\nTheme: {event.theme}\nDate: {event.date}\nVenue Address: {event.venue_address}\nClient ID: {event.client_ID}\nInvoice: {event.invoice}\nEmployee ID: {event.employee_ID}\nCaterer: {event.caterer}")
                return
        messagebox.showerror("Error", "Event not found")

    def delete_client(self):
        #to delete an client from the list
        client_ID = simpledialog.askstring("Input", "Enter client ID to delete")
        for client in self.clients:
            if client.client_ID == client_ID:
                self.clients.remove(client)
                messagebox.showinfo("Success", "Client deleted successfully")
                return
        messagebox.showerror("Error", "Client not found")

    def modify_client(self):
        #to modify client details
        client_ID = simpledialog.askstring("Input", "Enter client ID to modify")
        for client in self.clients:
            if client.client_ID == client_ID:
                name = simpledialog.askstring("Input", "Enter new client name")
                address = simpledialog.askstring("Input", "Enter new client address")
                contact_details = simpledialog.askstring("Input", "Enter new client contact details")
                budget = simpledialog.askfloat("Input", "Enter new client budget")
                client = Client(client_ID, name, address, contact_details, budget)
                self.clients.remove(client)
                self.clients.append(client)
                messagebox.showinfo("Success", "Client modified successfully")
                return
        messagebox.showerror("Error", "Client not found")

    def display_client(self):
        #to display client information
        client_ID = simpledialog.askstring("Input", "Enter client ID to display")
        for client in self.clients:
            if client.client_ID == client_ID:
                messagebox.showinfo("Client Details", f"Client ID: {client.client_ID}\nName: {client.name}\nAddress: {client.address}\nContact Details: {client.contact_details}\nBudget: {client.budget}")
                return
        messagebox.showerror("Error", "Client not found")

    def delete_guest(self):
        #to delete an guest from the list
        guest_ID = simpledialog.askstring("Input", "Enter guest ID to delete")
        for guest in self.guests:
            if guest.guest_ID == guest_ID:
                self.guests.remove(guest)
                messagebox.showinfo("Success", "Guest deleted successfully")
                return
        messagebox.showerror("Error", "Guest not found")

    def modify_guest(self):
        #to modify guest details
        guest_ID = simpledialog.askstring("Input", "Enter guest ID to modify")
        for guest in self.guests:
            if guest.guest_ID == guest_ID:
                name = simpledialog.askstring("Input", "Enter new guest name")
                address = simpledialog.askstring("Input", "Enter new guest address")
                contact_details = simpledialog.askstring("Input", "Enter new guest contact details")
                guest = Guest(guest_ID, name, address, contact_details)
                self.guests.remove(guest)
                self.guests.append(guest)
                messagebox.showinfo("Success", "Guest modified successfully")
                return
        messagebox.showerror("Error", "Guest not found")

    def display_guest(self):
        # to display guest information

        guest_ID = simpledialog.askstring("Input", "Enter guest ID to display")
        for guest in self.guests:
            if guest.guest_ID == guest_ID:
                messagebox.showinfo("Guest Details", f"Guest ID: {guest.guest_ID}\nName: {guest.name}\nAddress: {guest.address}\nContact Details: {guest.contact_details}")
                return
        messagebox.showerror("Error", "Guest not found")

    def delete_supplier(self):
        #to delete an supplier from the list

        supplier_ID = simpledialog.askstring("Input", "Enter supplier ID to delete")
        for supplier in self.suppliers:
            if supplier.supplier_ID == supplier_ID:
                self.suppliers.remove(supplier)
                messagebox.showinfo("Success", "Supplier deleted successfully")
                return
        messagebox.showerror("Error", "Supplier not found")

    def modify_supplier(self):
        #to modify supplier details
        supplier_ID = simpledialog.askstring("Input", "Enter supplier ID to modify")
        for supplier in self.suppliers:
            if supplier.supplier_ID == supplier_ID:
                name = simpledialog.askstring("Input", "Enter new supplier name")
                contact_details = simpledialog.askstring("Input", "Enter new supplier contact details")
                product_category = simpledialog.askstring("Input", "Enter new supplier product category")
                address = simpledialog.askstring("Input", "Enter new supplier address")
                email = simpledialog.askstring("Input", "Enter new supplier email")
                delivery_time = simpledialog.askstring("Input", "Enter new supplier delivery time")
                bank_details = simpledialog.askstring("Input", "Enter new supplier bank details")
                supplier = Supplier(supplier_ID, name, contact_details, product_category, address, email, delivery_time, bank_details)
                self.suppliers.remove(supplier)
                self.suppliers.append(supplier)
                messagebox.showinfo("Success", "Supplier modified successfully")
                return
        messagebox.showerror("Error", "Supplier not found")

    def display_supplier(self):
        #to display supplier information
        supplier_ID = simpledialog.askstring("Input", "Enter supplier ID to display")
        for supplier in self.suppliers:
            if supplier.supplier_ID == supplier_ID:
                messagebox.showinfo("Supplier Details", f"Supplier ID: {supplier.supplier_ID}\nName: {supplier.name}\nContact Details: {supplier.contact_details}\nProduct Category: {supplier.product_category}\nAddress: {supplier.address}\nEmail: {supplier.email}\nDelivery Time: {supplier.delivery_time}\nBank Details: {supplier.bank_details}")
                return
        messagebox.showerror("Error", "Supplier not found")

    def delete_venue(self):
        # to delete an venue from the list
        venue_ID = simpledialog.askstring("Input", "Enter venue ID to delete")
        for venue in self.venues:
            if venue.venue_ID == venue_ID:
                self.venues.remove(venue)
                messagebox.showinfo("Success", "Venue deleted successfully")
                return
        messagebox.showerror("Error", "Venue not found")

    def modify_venue(self):
        #to modify venue details
        venue_ID = simpledialog.askstring("Input", "Enter venue ID to modify")
        for venue in self.venues:
            if venue.get_name() == venue_ID:
                venue.name = simpledialog.askstring("Input", "Enter new venue name")
                venue.address = simpledialog.askstring("Input", "Enter new venue address")
                venue.contact = simpledialog.askstring("Input", "Enter new venue contact")
                venue.min_guests = simpledialog.askinteger("Input", "Enter new minimum guests")
                venue.max_guests = simpledialog.askinteger("Input", "Enter new maximum guests")
                messagebox.showinfo("Success", f"Venue with ID {venue_ID} modified.")
                return
        messagebox.showerror("Error", f"No venue found with ID {venue_ID}.")
    def display_venue(self):
        #to display venue information
        venue_ID = simpledialog.askstring("Input", "Enter venue ID to display")
        for venue in self.venues:
            if venue.get_name() == venue_ID:
                messagebox.showinfo("Venue Details", str(venue))
                return
        messagebox.showerror("Error", f"No venue found with ID {venue_ID}.")


from enum import Enum
from datetime import datetime

class EmployeeType(Enum):
    #define employee types using an Enum.
    Sales_Manager = 1
    SALESPERSON = 2
    MARKETING_MANAGER = 3
    MARKETER = 4
    ACCOUNTANT = 5
    DESIGNER = 6
    HANDYMAN = 7

class Employee:
    def __init__(self, employee_ID, name, department, job_title, basic_salary, age, date_of_birth, passport_details, employee_type):
        # Initialize an Employee object with the provided attributes.
        self.employee_ID = employee_ID
        self.name = name
        self.department= department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth= date_of_birth
        self.passport_details = passport_details
        self.employee_type = employee_type


    def get_ID(self):
        return self.employee_ID

    def get_name(self):
        return self.name

    def get_department(self):
        return self.department

    def get_job_title(self):
        return self.job_title

    def set_basic_salary(self, new_salary):
        self.salary = new_salary

    def get_employee_details(self):
        return f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.salary}, Type: {self.employee_type.value}"

    def __str__(self):
        return self.get_employee_details()

class Manager(Employee):
    def __init__(self, employee_ID, name, department, job_title, basic_salary, age, date_of_birth, passport_details, manager_ID, employee_type):
        # Initialize a Manager object by inheriting from the Employee class.
        super().__init__(employee_ID, name, department, job_title, basic_salary, age, date_of_birth, passport_details, employee_type)
        self.manager_ID = manager_ID

    def get_manager_ID(self):
        return self.manager_ID

    def set_manager_ID(self):
        self.manager_ID = manager_ID

    def participate_in_event(self, event):
        self.event = event

    def __str__(self):
        return f"{super().__str__()}, Manager ID: {self.manager_ID}"


class Event:
    class Event_type(Enum):
        # Define event types using an Enum.
        WEDDING = "wedding"
        BIRTHDAY = "birthday"
        THEMED_PARTY = "themed party"
        GRADUATION = "graduation"


    def __init__(self, event_ID, event_type, theme, date, venue_address, client_ID, invoice, employee_ID,caterer):
        # Initialize an Event object with the provided attributes.
        self.event_ID = event_ID
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.venue_address = venue_address
        self.client_ID = client_ID
        self.invoice = invoice
        self.employee_ID = employee_ID
        self.employees = []  # list of Employee objects
        self.caterer = caterer  # composition: Event has a Caterer
        self.suppliers = []  # Aggregation:

 #setters and getters
    def get_event_type(self):
        return self.event_type

    def get_theme(self):
        return self.theme

    def get_date(self):
        return self.date

    def get_venue_address(self):
        return self.venue_address

    def get_client(self):
        return self.client

    def get_invoice(self):
        return self.invoice

    def add_employee(self, employee):
        self.employees.append(employee)  # Append the employee object to the employees list

    def get_employees(self):
        return self.employees  # Return the employees list

    def get_employees(self):
        return self.employees

    def get_client_ID(self):
        return self.client_ID

    def set_client_ID(self, client_ID):
        self.client_ID = client_ID

    def set_caterer(self, caterer):
        self.caterer = caterer

    def get_caterer(self):
        return self.caterer

    def set_suppliers(self, supplier_list):
        self.suppliers = supplier_list

    def __str__(self):
        return f"Event ID: {self.event_ID}, Type: {self.event_type}, Theme: {self.theme}, Date: {self.date}, Venue: {self.venue}, Client ID: {self.client_ID}, Invoice: {self.invoice}, Employee ID: {self.employee_ID}"

class Client:
    # Initialize a Client object with the provided attributes.
    def __init__(self, client_ID, name, address, contact_details, budget):
        self.client_ID= client_ID
        self.name= name
        self.address= address
        self.contact_details= contact_details
        self.budget= budget

    def get_name(self):
        # Get the client's name.
        return self.name

    def get_address(self):
        # Get the client's address.
        return self.address

    def get_budget(self):
        # Get the client's budget.
        return self.budget

    def set_budget(self, budget):
        # Set the client's budget.
        self.budget = budget

    def get_client_ID(self):
        # Get the client's unique identifier.
        return self.client_ID

    def set_client_ID(self, client_ID):
        self.client_ID = client_ID

    def get_client_details(self):
        # Get additional client details (e.g., contact information).
        return self.contact_details


    def __str__(self):
        # Return a string representation of the Client object.
        return f"Client ID: {self.client_ID}, Name: {self.name}, Address: {self.address}, Budget: {self.budget}"

class Guest:
    def __init__(self, guest_ID, name, address, contact_details):
        self.guest_ID= guest_ID
        self.name= name
        self.address= address
        self.contact_details= contact_details

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_guest_details(self):
        return self.get_guest_details


    def __str__(self):
        return f"Guest ID: {self.guest_ID}, Name: {self.name}, Address: {self.address}, Contact Details: {self.contact_details}"


class Venue:
    def __init__(self, venue_ID, name, address, contact, min_guests, max_guests):
        self.venue_ID= venue_ID
        self.name= name
        self.address= address
        self.contact= contact
        self.min_guests= min_guests
        self.max_guests= max_guests

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_contact(self):
        return self.ontact

    def calculate_capacity(self):
        try:
            if self.max_guests < self.min_guests:
                raise ValueError("Maximum guests cannot be less than minimum guests")
            capacity_range = self.max_guests - self.min_guests
            return f"Minimum guests: {self.min_guests}, Maximum guests: {self.max_guests}, Capacity range: {capacity_range} guests"
        except ValueError as e:
            return f"Error: {e}"

    def set_address(self):
        self.address= address

    def add_event(self, event):
        self.events.append(event)

    def get_events(self):
        return self.events

    def __str__(self):
        return f"Venue {self.venue_ID}: {self.name}\nAddress: {self.address}\nContact: {self.contact}\nCapacity: {self.calculate_capacity()}"


class Caterer:
    def __init__(self, caterer_ID, name, address, contact_details, menu, min_guests, max_guests ):
        self.caterer_ID= caterer_ID
        self.name= name
        self.address= address
        self.contact_details= contact_details
        self.menu= menu
        self.min_guests= min_guests
        self.min_guests=min_guests
        self.max_guests=max_guests

    def get_caterer_name(self):
        return self.name

    def get_caterer_address(self):
        return self.address

    def get_contact_details(self):
        return self.contact_details

    def set_menu(self, menu):
        self.menu = menu

    def add_event(self, event):
        self.events.append(event)

    def remove_event(self, event):
        self.events.remove(event)

    def get_events(self):
        return self.events

    def __str__(self):
        return f"Caterer ID: {self.caterer_ID}, Name: {self.name}, Address: {self.address}, Contact Details: {self.contact_details}, Menu: {self.menu}, Min Guests: {self.min_guests}, Max Guests: {self.max_guests}"

class Supplier:
    def __init__(self, supplier_ID, name, contact_details, product_catagory, address, email, delivery_time, bank_details):
        self.supplier_ID= supplier_ID
        self.name= name
        self.contact_details= contact_details
        self.product_catagory= product_catagory
        self.address = address
        self.email = email
        self.delivery_time = delivery_time
        self.bank_details = bank_details

    def get_name(self):
        return self.name

    def get_contact_details(self):
        return self.contact_details

    def get_product_catagory(self):
        return self.product_catagory

    def get_delivery_time(self):
        return self.delivery_time

    def get_bank_details(self):
        return self.bank_details

    def set_bank_details(self):
        self.bank_details= bank_details

    def __str__(self):
        return f"Supplier ID: {self.supplier_ID}, Name: {self.name}, Contact Details: {self.contact_details}, Product Category: {self.product_category}, Address: {self.address}, Email: {self.email}, Delivery Time: {self.delivery_time}, Bank Details: {self.bank_details}"


def load_data(self):
    try:
        # Check if the data file exists

        if os.path.exists('event_management_data.pkl'):
            # If the file exists, open it for reading in binary mode
            with open('event_management_data.pkl', 'rb') as input:
                # Load the data from the file
                data = pickle.load(input)
                # Assign loaded data to instance variables
                self.employees = data['employees']
                self.events = data['events']
                self.clients = data['clients']
                self.guests = data['guests']
                self.suppliers = data['suppliers']
                self.venues = data['venues']
                # Show a success message
            messagebox.showinfo("Load", "Data loaded successfully!")
        else:
            # If the file does not exist, show an error message
            messagebox.showerror("Load", "No data file found.")
    except (FileNotFoundError, EOFError, pickle.UnpicklingError) as e:
        # Handle specific exceptions related to file reading or unpickling errors
        messagebox.showerror("Load", f"Error while loading data: {e}")

def create_save_load_buttons(self):
    tk.Button(self.master, text="Save Data", command=self.save_data).pack()
    tk.Button(self.master, text="Load Data", command=self.load_data).pack()

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()