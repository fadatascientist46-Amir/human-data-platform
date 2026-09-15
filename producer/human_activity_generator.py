# Import json to convert Python dictionaries into JSON format
import json

# Import random to generate random values
import random

# Import datetime to create event timestamps
from datetime import datetime, timezone

# Import Faker to generate realistic/random data
from faker import Faker


# Create a Faker object
fake = Faker()


# List of possible user activities
EVENT_TYPES = [
    "login",
    "logout",
    "page_view",
    "search",
    "click",
    "purchase",
    "feedback",
    "support_request"
]


# List of application pages
PAGES = [
    "home",
    "products",
    "product_details",
    "search",
    "cart",
    "checkout",
    "profile",
    "support"
]


# List of devices users can use
DEVICES = [
    "mobile",
    "desktop",
    "tablet"
]


# List of countries
COUNTRIES = [
    "PK",
    "US",
    "UK",
    "AE",
    "CA",
    "SA"
]


# Function to create ONE human activity event
def generate_event():

    # Create one event as a Python dictionary
    event = {

        # Generate a unique event ID
        "event_id": fake.uuid4(),

        # Generate a random user ID
        "user_id": f"USR{random.randint(10000, 99999)}",

        # Randomly select what the user did
        "event_type": random.choice(EVENT_TYPES),

        # Randomly select the page
        "page": random.choice(PAGES),

        # Randomly select the device
        "device": random.choice(DEVICES),

        # Randomly select the country
        "country": random.choice(COUNTRIES),

        # Create the current UTC timestamp
        "timestamp": datetime.now(timezone.utc).isoformat(),

        # Generate a random session ID
        "session_id": f"SES{random.randint(10000, 99999)}"
    }

    # Return the generated event
    return event


# Function to generate multiple events
def generate_events(number_of_events=1000):

    # Create an empty list to store events
    events = []

    # Repeat the process for the required number of events
    for _ in range(number_of_events):

        # Generate one event and add it to the list
        events.append(generate_event())

    # Return all generated events
    return events


# Run this part only when this file is executed directly
if __name__ == "__main__":

    # Generate 1,000 human activity events
    events = generate_events(1000)

    # Define where the data will be saved
    output_file = "data/human_activity.json"

    # Open/create the output file in write mode
    with open(output_file, "w") as file:

        # Go through every generated event
        for event in events:

            # Convert the dictionary into JSON
            # and write one event per line
            file.write(json.dumps(event) + "\n")

    # Print how many events were generated
    print(f"Generated {len(events)} events.")

    # Print where the data was saved
    print(f"Saved to: {output_file}")