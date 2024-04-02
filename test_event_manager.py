import unittest
from event_manager import EventManager

class TestEventManager(unittest.TestCase):
    def setUp(self):
        """Set up a fresh instance of EventManager for each test method."""
        self.manager = EventManager()

    def test_add_and_list_events(self):
        """Test adding an event and then listing events."""
        self.manager.add_event("Test Event", "This is a test.", "2024-01-01", "12:00")
        self.assertIn("Test Event", self.manager.list_events(), "Event should be listed after being added.")

    def test_search_event(self):
        """Test searching for an added event."""
        self.manager.add_event("Search Event", "Event to be searched.", "2024-02-02", "14:00")
        search_result = self.manager.search_events("Search")
        self.assertIn("Search Event", search_result, "Should find the event with 'Search' in the title.")

    def test_edit_event(self):
        """Test editing an existing event's title."""
        original_title = "Original Event"
        new_title = "Edited Event"
        self.manager.add_event(original_title, "Event before edit.", "2024-03-03", "16:00")
        self.manager.edit_event(original_title, new_title=new_title)
        events_after_edit = self.manager.list_events()
        self.assertIn(new_title, events_after_edit, "The event title should be updated to 'Edited Event'.")

    def test_delete_event(self):
        """Test deleting an event."""
        event_title = "Event to Delete"
        self.manager.add_event(event_title, "This event will be deleted.", "2024-04-04", "18:00")
        self.manager.delete_event(event_title)
        self.assertNotIn(event_title, self.manager.list_events(), "Deleted event should not be listed.")

if __name__ == '__main__':
    unittest.main()
