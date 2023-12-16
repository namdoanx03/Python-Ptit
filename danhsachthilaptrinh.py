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

num_teams = int(input())

teams = []
contestants = []


for _ in range(num_teams):
    team_name = input()
    university = input()
    team_id = f"Team{len(teams) + 1:02}"
    teams.append(Team(team_id, team_name, university))

num_contestants = int(input())


for _ in range(num_contestants):
    full_name = input()
    team_id = input()
    contestant_id = f"C{len(contestants) + 1:03}"
    contestants.append(Contestant(contestant_id, full_name, team_id))


sorted_contestants = sorted(contestants, key=lambda x: x.full_name)

for contestant in sorted_contestants:
    team = next(team for team in teams if team.team_id == contestant.team_id)
    print(f"{contestant.contestant_id} {contestant.full_name} {team.team_name} {team.university}")