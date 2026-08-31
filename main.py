# this will be the interaactive menu for the user

from data import system

while True:
  print(" \nWelcome to the ticket management system")
  print("\nUSER PANEL:")
  print("1. SUBMIT TICKET")
  print("2. VIEW MY TICKETS")
  print("3. GET TICKET UPDATE")

  print("5. ENGINEER DASHBOARD")
  print("6. TEAM DASHBOARD")
  print("7. EXIT")
  choice = input("\nPick an option above: ")
  if choice == "1":
    email = input("Please enter your email")
    user = system.find_user(email)
    if user is not None:
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
      else:
        print("Please select a number from list above: ")
        continue
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
    else:
        print("User not found")
  elif choice == "2":
      email = input("Please enter your email: ")
      user = system.find_user(email)
      if user is None:
        print("Please enter a valid email")
      elif not user.submitted_tickets:
        print("No submitted tickets")
      else:
        user_tickets = user.submitted_tickets
        print(f"\n All tickets for {user.name}")
        for ticket in user_tickets:
           print(f" \nStatus: {ticket.status}")
           print(f" Ticket ID: {ticket.ticket_id}")
           print(f" Title: {ticket.title}")
           print(f" Description: {ticket.description}")
           print(f" Category: {ticket.category}")
           print(f" Priority: {ticket.priority}")

  elif choice == "3":
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
      else:
        print(f"\nYour ticket is currently being handled by the {ticket.assigned_team.name}")
        print(f" Status: {ticket.status}")
        print(f" Title: {ticket.title}")
        print(f" Description: {ticket.description}")
        print(f" Category: {ticket.category}")
        print(f" Priority: {ticket.priority}")



















