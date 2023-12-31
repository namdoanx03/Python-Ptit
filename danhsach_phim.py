from datetime import datetime

class Genre:
    def __init__(self, id, name):
        self.id = 'TL{:03d}'.format(id)
        self.name = name

    def __str__(self):
        return self.name

class Film:
    def __init__(self, id, genre, date, name, length):
        self.id = 'P{:03d}'.format(id)
        self.genre = genre
        self.date = date
        self.name = name
        self.length = length

    def __str__(self):
        return f'{self.id} {self.genre} {self.date} {self.name} {self.length}'


genres, films = [], []
n, m = [int(i) for i in input().split()]
for i in range(n):
    genres.append(Genre(i+1, input()))
for i in range(m):
    genre_id = input()
    genre = next((g for g in genres if g.id == genre_id), None)
    for i in range(m):
        id = input()
        for f in genres:
            if f.id == id:
                films.append(Film(i+1, f, input(), input(), int(input())))

films.sort(key=lambda e: (datetime.strptime(e.date, '%d/%m/%Y'), e.name, -e.length))
print(*films, sep='\n')