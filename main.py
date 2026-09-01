# this will be the interaactive menu for the user

from data import system


def submit_a_ticket():
      email = input("Please enter your email")
      user = system.find_user(email)
      if user is None:
        print("User not found")
        return
      title = input("Enter ticket title: ")
      description = input ("Enter description: ")
      print("1. Networking")
      print("2. Cyber")
      print("3 Software")
      print("4. Cloud")
      category_choice = input("Select category for ticket: ")
      if category_choice == "1":
        category_choice = "Networking"
      elif category_choice == "2":
        category_choice = "Cyber"
      elif category_choice == "3":
        category_choice = "Software"
      elif category_choice == "4":
        category_choice = "Cloud"
      priority = input("Enter priority (High, Medium, Low ?):  ")
      ticket = system.submit_ticket(user, title, description, category_choice, priority)
      team = system.route_ticket(ticket)
      print("Successfully submitted your ticket")
      print(f"Please take note of your ticket ID: {ticket.ticket_id}")
      print(f"  \n Submitted by: {ticket.submitted_by.name}")
      print(f" Title: {ticket.title}")
      print(f" Description: {ticket.description}")
      print(f" Category: {ticket.category}")
      print(f" Priority: {ticket.priority}")
      if team is not None:
        print(f"Assigned team: {team.name}")
      else:
        print("No matching team was found")


def view_my_tickets():
      email = input("Please enter your email: ")
      user = system.find_user(email)
      if user is None:
        print("Please enter a valid email")
      elif not user.submitted_tickets:
        print("No submitted tickets")
      else:
        print(f"\n All tickets for {user.name}")
        user_tickets = user.submitted_tickets
        for ticket in user_tickets:
            print(f" \nStatus: {ticket.status}")
            print(f" Ticket ID: {ticket.ticket_id}")
            print(f" Title: {ticket.title}")
            print(f" Description: {ticket.description}")
            print(f" Category: {ticket.category}")
            print(f" Priority: {ticket.priority}")


def check_ticket():
    email = input("Please enter your email: ")
    user = system.find_user(email)
    if user is None:
      print("Please enter a valid email ")
    else:
      ticket_id = int(input("Please enter your ticket ID: "))
      ticket = system.find_ticket(ticket_id)
      if ticket is None:
        print("\nTicket ID is not found")
      elif ticket.submitted_by != user:
        print("\nThis ticket does not belong to you ")
      elif ticket.assigned_engineer is None:
         print("No assigned engineer yet ")
      print(f"\nYour ticket is currently being handled by the {ticket.assigned_team.name}")
      print(f" Assigned engineer: {ticket.assigned_engineer}")
      print(f" Status: {ticket.status}")
      print(f" Title: {ticket.title}")
      print(f" Description: {ticket.description}")
      print(f" Category: {ticket.category}")
      print(f" Priority: {ticket.priority}")


def view_team_queue():
   email = input("Enter email: ")
   engineer = system.find_engineer(email)
   if engineer is None:
      print("No engineer found with a matching email")
      return
   team_name = input("Enter the team name: ").lower().strip()
   team = system.teams.get(team_name)
   if team is None:
      print("Team name not found in our system")
      return
   if engineer.team != team:
      print("You cannot view tickets for another team")
      return

   open_tickets = []
   for ticket in team.tickets:
      if ticket.assigned_engineer is None:
         open_tickets.append(ticket)

   if not open_tickets:
      print("No open tickets for your team ")
      return

   print(f"All open tickets for: {team.name}")
   for ticket in team.tickets:
        print(f"\nTicket ID: {ticket.ticket_id}")
        print(f"Title: {ticket.title}")
        print(f"Description: {ticket.description}")
        print(f"Priority: {ticket.priority}")
        print(f"Status: {ticket.status}")
        print(f"Submitted by: {ticket.submitted_by.email}")


def take_ticket():
   email = input("Please enter your email: ")
   engineer = system.find_engineer(email)
   if engineer is None:
      print("No engineer was found")
      return
   team_tickets = engineer.team.tickets
   print(f"Open tickets for: {engineer.team.name}")
   available_tickets = []

   for ticket in team_tickets:
      if ticket.assigned_engineer is None:
        available_tickets.append(ticket)
        print(f"\nTicket ID: {ticket.ticket_id}")
        print(f"Title: {ticket.title}")
        print(f"Description: {ticket.description}")
        print(f"Priority: {ticket.priority}")
        print(f"Status: {ticket.status}")
        print(f"Submitted by: {ticket.submitted_by.email}")
   if not available_tickets:
      print("There are no available tickets")
      return
   ticket_id = int(input("Enter ticket ID you would like to take: "))
   ticket_found = system.find_ticket(ticket_id)

   if ticket_found is None:
        print("No ticket ID found")
        return

   if ticket_found.assigned_team != engineer.team:
        print("Ticket is not from the same team ")
        return
   if ticket_found.assigned_engineer is not None:
      print("This ticket has already been taken")
      return

   assigned = system.assign_ticket(ticket, engineer)
   if assigned:
    print("\nSuccessfully assigned ticket ")
    print(f"\nTicket: {ticket.ticket_id}")
    print(f"Assigned to: {engineer.name}")
   else:
      print("Ticket failed to be assigned")





def engineer_panel():
   while True:
        print("\n--- ENGINEER PANEL ---")
        print("1. View all open team tickets ")
        print("2. Assign yourself a ticket  ")
        print("3. Back")

        choice = input("\nPick an option: ")
        if choice == "1":
           view_team_queue()
        elif choice == "2":
           take_ticket()
        elif choice == "3":
           break

def user_panel():
   while True:
        print("\n--- USER PANEL ---")
        print("1. Submit a Ticket")
        print("2. View all my submitted tickets")
        print("3. Check progress on a submitted ticket")
        print("4. Back")

        choice = input("\nPick an option: ")

        if choice == "1":
            submit_a_ticket()

        elif choice == "2":
            view_my_tickets()

        elif choice == "3":
            check_ticket()

        elif choice == "4":
            break

        else:
            print("Invalid option.")

while True:
    print("\n================================")
    print("   TICKET MANAGEMENT SYSTEM")
    print("================================")

    print("\n1. User Panel")
    print("2. Engineer Panel")
    print("3. Exit")

    choice = input("\nPick an option: ")

    if choice == "1":
        user_panel()

    elif choice == "2":
        engineer_panel()

    elif choice == "3":
        print("Goodbye.")
        break

    else:
        print("Invalid option.")









