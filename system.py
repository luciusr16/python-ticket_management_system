from models import Ticket, Team, Engineer, User

class TicketSystem:
  def __init__(self):
    self.users = {}
    self.engineers = {}
    self.teams = {}
    self.tickets = {}
    self.next_ticket_id = 1

  def add_user(self, user):
    self.users[user.email.lower()] = user

  def add_team (self, team):
    self.teams[team.name.lower()] = team

  def add_engineer(self, engineer):
    self.engineers[engineer.email.lower()] = engineer

  def find_user(self, user_email):
    user = self.users.get(user_email.lower().strip())
    if user:
      return user
    return None

  def find_engineer(self, engineer_email):
    engineer = self.engineers.get(engineer_email.lower().strip())
    if engineer:
      return engineer
    return None

  def submit_ticket(self, user, title, description, category, priority):
    new_ticket = Ticket(self.next_ticket_id, title, description, category, priority, user)
    self.tickets[self.next_ticket_id] = new_ticket
    user.submitted_tickets.append(new_ticket)
    self.next_ticket_id += 1
    return new_ticket

  def find_ticket(self, ticket_id):
    ticket_found = self.tickets.get(ticket_id)
    if ticket_found:
      return ticket_found
    return None

  def route_ticket(self, ticket):
    ticket_category = ticket.category.lower()
    for team in self.teams.values():
      team_category = team.category.lower()
      if ticket_category == team_category:
        ticket.assigned_team = team
        team.tickets.append(ticket)
        return team
    return None

  def assign_ticket(self, ticket, engineer):
    engineer_team = engineer.team
    ticket_team = ticket.assigned_team
    if engineer_team is None:
      return False
    if ticket_team is None:
      return False
    if engineer_team != ticket_team:
      return False
    ticket.assigned_engineer = engineer.name
    engineer.assigned_tickets.append(ticket)
    ticket.status = "Assigned"
    return True

 




















