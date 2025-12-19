from agent import lead_agent

if __name__ == "__main__":
    "A sample data file to test the agent. Write the emails for the users."
    leads = [
        {"name": "Ava", "email": "vanshikabansalyoyo@gmail.com", "budget": 2000, "location": "Brampton", "message": "Looking to rent a 2-bedroom apartment starting February."},
        {"name": "Liam", "email": "", "budget": 500000, "location": "Toronto", "message": "Interested in buying a 3-bedroom house within 6 months."},
        {"name": "Sophia", "email": "", "budget": 1500, "location": "Mississauga", "message": "Looking for rental options for a studio apartment."}
    ]

    for lead in leads:
        lead_agent(lead)
