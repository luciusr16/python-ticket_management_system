# this will be the interaactive menu for the user

from data import system

while True:
  print("Welcome to the ticket management system")
  print("\n1. SUBMIT TICKET")
  print("2. FIND TICKETS")
  print("3. VIEW ALL TICKETS")
  print("4. VIEW MY TICKETS")

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












