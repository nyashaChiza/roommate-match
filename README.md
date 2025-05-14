
````markdown
# RoommateMatch Platform

RoommateMatch is a web-based prototype developed to help students at university find compatible roommates based on lifestyle preferences, habits, and personal values. By allowing students to customize their profiles and match criteria, RoommateMatch aims to reduce roommate conflicts and create more harmonious living environments within university accommodations.

## Project Objective

The main objective of this project is to develop an intelligent and user-friendly web application that matches students with compatible roommates. The system addresses the limitations of random roommate assignments by enabling preference-based matching, which can lead to better social experiences, academic performance, and overall satisfaction in student housing.

## Project Description

Many students experience difficulties with roommates due to mismatched lifestyles, schedules, and habits. RoommateMatch solves this by allowing students to:

- Register and complete detailed profiles
- Indicate preferences such as cleanliness, sleep schedule, study habits, and social type
- View potential roommate matches based on compatibility
- Ask and answer personalized questions before committing to a roommate match

The platform also includes administrative tools for managing users and reviewing matches.

## Features

### 1. Student Registration & Authentication
- Secure signup and login system
- Email-based registration with student ID

### 2. Customizable Student Profiles
- Profile includes sleep habits, study preferences, cleanliness, social behavior, and roommate gender preference

### 3. Compatibility Matching
- Simple rule-based algorithm compares preferences and suggests top matches
- Compatibility score shown for each match

### 4. Interest-Based Matching Flow
- Students can "Mark as Interested" in a compatible profile
- Recipient receives interest notification and can respond

### 5. Custom Roommate Questions
- Each student can define up to 3 personal questions
- When a match interest is sent, the recipient answers those questions before confirming

### 6. Admin Panel
- View all student profiles and match history
- Ability to manage users and oversee matches

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: Django Templates + Bootstrap (or Tailwind)
- **Database**: SQLite (for prototype)
- **Deployment**: PythonAnywhere or Heroku (free tier)

## Installation (Development)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/roommatematch.git
   cd roommatematch
````

2. Create a virtual environment and activate it:

   ```bash
   python -m venv env
   source env/bin/activate  # or env\Scripts\activate on Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start development server:

   ```bash
   python manage.py runserver
   ```

## Future Enhancements

* Feedback and rating system after roommate pairing
* Mobile app integration using React Native or Flutter
* Machine learning-based matching model
* Real-time messaging between matched students

## License

This project is for educational and prototype purposes only. All rights reserved.

---

