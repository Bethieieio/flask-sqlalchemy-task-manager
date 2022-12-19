from sqlalchemy import Column, Integer, String, Text, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from taskmanager import db

class Category(db.Model):
    # schema for category model //  this course is a waste of money
    id = Column(Integer, primary_key=True)
    category_name = Column(String(25), unique=True, nullable=False)
    tasks = relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Task(db.Model):
    # schema for task model
    id = Column(Integer, primary_key=True)
    task_name = Column(String(50), unique=True, nullable=False)
    task_description = Column(Text, nullable=False)
    is_urgent = Column(Boolean, default=False, nullable=False)
    due_date = Column(Date, nullable=False)
    category_id = Column(Integer, ForeignKey("category.id", ondelete="Cascade"), nullable=False)
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )