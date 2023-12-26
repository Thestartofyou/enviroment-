import datetime
import random

class EcoFriendlyReminder:
    def __init__(self):
        self.reminders = [
            "Turn off lights when not in use.",
            "Use reusable bags when shopping.",
            "Reduce water usage by fixing leaks.",
            "Plant a tree or participate in a local tree planting event.",
            "Unplug electronic devices when not in use.",
            "Choose energy-efficient appliances.",
            "Take public transportation, carpool, or bike to reduce carbon footprint.",
            "Recycle paper, plastic, and glass.",
            "Conserve water by taking shorter showers.",
            "Buy locally-produced and sustainable products."
        ]

    def get_random_reminder(self):
        return random.choice(self.reminders)

    def generate_reminder(self):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        reminder = self.get_random_reminder()
        print(f"\n[{current_time}] Eco-Friendly Reminder: {reminder}\n")

if __name__ == "__main__":
    reminder_app = EcoFriendlyReminder()

    try:
        while True:
            reminder_app.generate_reminder()
            # Set the time interval for reminders (e.g., every 30 minutes)
            time_interval_minutes = 30
            time.sleep(time_interval_minutes * 60)

    except KeyboardInterrupt:
        print("\nEco-Friendly Reminder application terminated.")
