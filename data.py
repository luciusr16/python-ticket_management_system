from models import User, Engineer, Team, Ticket
from system import TicketSystem

system = TicketSystem()

# Users
john = User("John Thompson", "johnt@user.com")
mary = User("Mary Jones", "maryj@user.com")
jack = User("Jack Ridley", "jackr@user.com")
susan = User("Susan Bronson", "susanb@user.com")



# Engineers list
alice = Engineer("Alice Brown", "aliceb@network.com")
adam = Engineer("Adam Jones", "adamj@cloud.com")
tom = Engineer("Tom Carter", "tomc@software.com")
james = Engineer("James Fernandes", "jamesf@cyber.com")

#adding engineers themselves to the management system
system.add_engineer(alice)
system.add_engineer(adam)
system.add_engineer(tom)
system.add_engineer(james)


# Teams list
network_team = Team("Network Team", "Networking")
cloud_team = Team("Cloud Team", "Cloud")
software_team = Team("Software Team", "Software")
cyber_team = Team("Cyber Team", "Cyber")

# adding all teams to the management system
system.add_team(network_team)
system.add_team(software_team)
system.add_team(cloud_team)
system.add_team(cyber_team)


# Adding engineers to the teams
network_team.add_engineer(alice)
cloud_team.add_engineer(adam)
software_team.add_engineer(tom)
cyber_team.add_engineer(james)

# Adding users to the ticket system
system.add_user(john)
system.add_user(mary)
system.add_user(jack)
system.add_user(susan)

#adding engineers
system.add_user(alice)
system.add_user(adam)
system.add_user(tom)
system.add_user(james)



#Creating and routing fake tickets to test functions in system.py
ticket1 = system.submit_ticket(
    john,
    "VPN not working",
    "VPN connection times out",
    "Networking",
    "High"
)

ticket2 = system.submit_ticket(
    john,
    "DNS issue",
    "Internal domain isn't resolving",
    "Networking",
    "Medium"
)

ticket3 = system.submit_ticket(
    mary,
    "Cloud issue",
    "Storage running low",
    "Cloud",
    "High"
)
ticket4 = system.submit_ticket(
  jack,
  "Cyber issue",
  "Locked out of pc",
  "Cyber",
  "High"
)

ticket5 = system.submit_ticket(
  susan,
  "Forgot password",
  "Cannot log in",
  "Software",
  "Medium"
)



system.route_ticket(ticket1)
system.route_ticket(ticket2)
system.route_ticket(ticket3)
system.route_ticket(ticket4)
system.route_ticket(ticket5)









