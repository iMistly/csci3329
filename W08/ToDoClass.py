class ToDo:
    def __init__(self) -> None:
        self.tasks = {"high": [], "mid": [], "low": []}

class Event:
    def __init__(self, name, date, location) -> None:
        self.name = name
        self.date = date
        self.location = location
        self.attendees = ["myself"]
        self.toDoList = ToDo()
        
    def changeLoc(self, newLocation):
        self.location = newLocation
        print(f"{len(self.attendess)} attendees need to be notified of this change.")