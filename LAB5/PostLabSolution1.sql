CREATE TABLE Participants (
    ParticipantID INTEGER PRIMARY KEY,
    LastName TEXT NOT NULL,
    FirstName TEXT NOT NULL,
    Address TEXT NOT NULL,
    City TEXT NOT NULL,
    State TEXT NOT NULL,
    PostalCode TEXT NOT NULL,
    PhoneNumber TEXT NOT NULL,
    DateOfBirth DATE NOT NULL
);

CREATE TABLE Classes (
    ClassID INTEGER PRIMARY KEY,
    Description TEXT NOT NULL,
    MaxPeople INTEGER NOT NULL,
    Fee REAL NOT NULL
);

CREATE TABLE Enrollments (
    EnrollmentID INTEGER PRIMARY KEY,
    ParticipantID INTEGER,
    ClassID INTEGER,
    ClassDate DATE NOT NULL,
    FOREIGN KEY(ParticipantID) REFERENCES Participants(ParticipantID),
    FOREIGN KEY(ClassID) REFERENCES Classes(ClassID)
);
