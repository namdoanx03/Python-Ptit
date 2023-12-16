class Team:
    def __init__(self, team_id, team_name, university):
        self.team_id = team_id
        self.team_name = team_name
        self.university = university

class Contestant:
    def __init__(self, contestant_id, full_name, team_id):
        self.contestant_id = contestant_id
        self.full_name = full_name
        self.team_id = team_id

# Read the number of teams
num_teams = int(input())

teams = []
contestants = []

# Read information about the teams
for _ in range(num_teams):
    team_name = input()
    university = input()
    team_id = f"Team{len(teams) + 1:02}"
    teams.append(Team(team_id, team_name, university))

# Read the number of contestants
num_contestants = 0
try:
    num_contestants = int(input())
except ValueError:
    print("Invalid input for the number of contestants.")

# Read information about the contestants
for _ in range(num_contestants):
    full_name = input()
    team_id = input()
    contestant_id = f"C{len(contestants) + 1:03}"
    contestants.append(Contestant(contestant_id, full_name, team_id))

# Sort the list of contestants by full name (lexicographic order)
sorted_contestants = sorted(contestants, key=lambda x: x.full_name)

# Print the sorted list of contestants
for contestant in sorted_contestants:
    team = next(team for team in teams if team.team_id == contestant.team_id)
    print(f"{contestant.contestant_id} {contestant.full_name} {team.team_name} {team.university}")