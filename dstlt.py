class Team:
    def __init__(self, id, name, school):
        self.id = 'Team{:02d}'.format(id)
        self.name = name
        self.school =school
class ThiSinh:
    def __init__(self, id, name, team):
        self.id = 'C{:03d}'.format(id)
        self.name = name
        self.team = team
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.team.name} {self.team.school}'

teams = [Team(i+1, input(), input()) for i in range(int(input()))]      
student = []
for i in range(int(input())):
    name, team = input(), input()
    for f in teams:
        if f.id == team:
            student.append(ThiSinh(i+1, name, f))
            break
student.sort( key= lambda x: x.name)
print(*student, sep='\n')