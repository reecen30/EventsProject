from datetime import datetime

class Event:
    def __init__(self, title, description, date, time):
        self.title = title
        self.description = description
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.time = datetime.strptime(time, "%H:%M").time()

    def __repr__(self):
        return f"{self.title} on {self.date.strftime('%Y-%m-%d')} at {self.time.strftime('%H:%M')}"

class EventManager:
    def __init__(self):
        self.events = []

    def valid_date(self, date_text):
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def valid_time(self, time_text):
        try:
            datetime.strptime(time_text, "%H:%M")
            return True
        except ValueError:
            return False

    def add_event(self, title, description, date, time):
        if not self.valid_date(date) or not self.valid_time(time):
            return "Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time."
        new_event = Event(title, description, date, time)
        self.events.append(new_event)
        self.events.sort(key=lambda event: (event.date, event.time))
        return "Event added successfully."

    def list_events(self):
        if not self.events:
            return "No events scheduled."
        return "\n".join(repr(event) for event in self.events)

    def delete_event(self, title):
        for event in self.events:
            if event.title == title:
                self.events.remove(event)
                return "Event deleted."
        return "Event not found."

    def search_events(self, query):
        query = query.lower().strip()  # Convert query to lowercase and strip whitespace
        matches = [event for event in self.events if query in event.title.lower() or query in event.description.lower()]
        if not matches:
            return "No matching events found."
        return "\n".join(repr(event) for event in matches)

    def edit_event(self, original_title, new_title=None, new_description=None, new_date=None, new_time=None):
        original_title = original_title.strip()  # Strip whitespace from the original title
        for event in self.events:
            if event.title.lower() == original_title.lower():  # Case-insensitive comparison
                if new_title: event.title = new_title.strip()
                if new_description: event.description = new_description.strip()
                if new_date and self.valid_date(new_date): event.date = datetime.strptime(new_date.strip(),
                                                                                          "%Y-%m-%d").date()
                if new_time and self.valid_time(new_time): event.time = datetime.strptime(new_time.strip(),
                                                                                          "%H:%M").time()
                return "Event updated successfully."
        return "Event not found."


