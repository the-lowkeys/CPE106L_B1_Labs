"""
File: student.py
Resources to manage a student's name and test scores.
"""
import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __eq__(self, other):
        """Tests for equality based on student names."""
        return self.name == other.name

    def __lt__(self, other):
        """Tests for less than based on student names."""
        return self.name < other.name

    def __ge__(self, other):
        """Tests for greater than or equal to based on student names."""
        return self.name >= other.name

def main():
    """A simple test."""
    students = [Student("Ken", 5), Student("Ben", 5), Student("Jen", 5), Student("Len", 5), Student("Ren", 5)]
    
    # Set scores for each student
    for student in students:
        for i in range(1, 6):
            student.setScore(i, random.randint(50, 100))
    
    # Shuffle the students
    random.shuffle(students)
    
    # Sort the students
    students.sort()
    
    # Print each student's information
    for student in students:
        print(student)

if __name__ == "__main__":
    main()



