from app import app
from models import db, TodoItem

with app.app_context():
    db.create_all()

    # Check if the database is already seeded
    if not TodoItem.query.first():
        todos = [
            TodoItem(title="Buy groceries", description="Purchase milk, eggs, bread, and fruit", completed=False),
            TodoItem(title="Finish project report", description="Complete the final draft of the project report", completed=True),
            TodoItem(title="Call plumber", description="Schedule a visit to fix the leaking sink", completed=False),
            TodoItem(title="Workout", description="Complete a 30-minute cardio session", completed=True),
            TodoItem(title="Read a book", description="Read 'The Great Gatsby' by F. Scott Fitzgerald", completed=False),
            TodoItem(title="Plan weekend trip", description="Make an itinerary for the weekend trip to the mountains", completed=True),
            TodoItem(title="Attend meeting", description="Join the team meeting at 10 AM", completed=False),
            TodoItem(title="Pay bills", description="Pay electricity and internet bills", completed=True),
            TodoItem(title="Clean the house", description="Vacuum and dust all rooms", completed=False),
            TodoItem(title="Write blog post", description="Draft a new post for the tech blog", completed=True),
            TodoItem(title="Update software", description="Install the latest updates for the operating system", completed=False),
            TodoItem(title="Prepare dinner", description="Cook pasta with homemade tomato sauce", completed=True)
        ]

        db.session.add_all(todos)
        db.session.commit()
    else:
        print("Database is already seeded!")
