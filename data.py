from models import User, Engineer, Team, Ticket
from system import TicketSystem

system = TicketSystem()

john = User("John", "john.doe@example.com")

alice = Engineer("Alice Brown", "alice.example.com")

network_team = Team("Network Team", "Networking")


ticket1 = Ticket(
    1,
    "VPN connection failing",
    "Unable to connect to the company VPN from home.",
    "Networking", "High", john
)

network_team.add_engineer(alice)

team = alice.team
if team is not None:
  print(team)
else:
  print("no team ")




