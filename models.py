
class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.submitted_tickets = []

class Engineer(User):
  def __init__(self, name, email):
    super().__init__(name, email)
    self.team = None
    self.assigned_tickets = []


class Team:
    def __init__(self, name, category):
      self.name = name
      self.category = category
      self.engineers = []
      self.tickets = []
    def add_engineer(self, engineer):
         self.engineers.append(engineer)
         engineer.team = self

class Ticket:
       def __init__(
        self,
        ticket_id,
        title,
        description,
        category,
        priority,
        submitted_by
    ):
        self.ticket_id = ticket_id
        self.title = title
        self.description = description
        self.category = category
        self.priority = priority
        self.status = "Open"
        self.submitted_by = submitted_by
        self.assigned_team = None
        self.assigned_engineer = None
        self.updated_status = None
        self.comments = []
        
