print("="*64) #used Chatgpt to help with concatenation
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("="*64)

full_name = "Daylen Hicks" #string
email = "dhicks4@ncat.edu"
hometown = "Henrico, NC"
graduation_semester = "Spring 2027"
major = "Computer Science"

print(f"Student: {full_name} | Email: {email}")
print(f"From: {hometown} | Graduating: {graduation_semester}")
print(f"Major: {major}\n")

print("=== ACADEMIC PROFILE ===")

current_courses = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"] #list
credit_hours = [3, 3, 3, 3]
gpa_history = [3.2, 3.6, 3.4, 3.7]
weekly_study_hours = 25
study_hours_per_subject = {
    "Programming": 10,
    "Math": 8,
    "English": 4,
    "History": 3
    }
study_hour_value = 5.0
total_credits = sum(credit_hours)
cumulative_gpa = sum(gpa_history) / len(gpa_history)

print(f"Current Semester: {total_credits} credits across {len(current_courses)} courses")
print(f"Cumulative GPA: {cumulative_gpa:.2f}")
print(f"Weekly Study Time: {weekly_study_hours} hours")
print(f"Academic Investment: ${study_hour_value} per study hour\n")

course_credits = {"COMP 163": 3, "MATH 150": 3, "ENG 101": 3, "HIS 105": 3}
professors = {"COMP 163": "Prof. Rhodes", "MATH 150": "Dr. Lee", "ENG 101": "Dr. Martinez", "HIS 105": "Dr. Brown"}
rooms = {"COMP 163": "M-Eric 300", "MATH 150": "Marteena 201", "ENG 101": "Crosby 121", "HIS 105": "Crosby 210"}
print("Current Courses:")
print(f"{current_courses[0]} - {credit_hours[0]} credits - {professors['COMP 163']} - {rooms['COMP 163']}")
print(f"{current_courses[1]} - {credit_hours[1]} credits - {professors['MATH 150']} - {rooms['MATH 150']}")
print(f"{current_courses[2]} - {credit_hours[2]} credits - {professors['ENG 101']} - {rooms['ENG 101']}")
print(f"{current_courses[3]} - {credit_hours[3]} credits - {professors['HIS 105']} - {rooms['HIS 105']}\n")

current_skills = {"Python basics", "HTML", "Problem solving", "Time management","Photography"} #set
skills_to_learn = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_iterest = {"Software development", "Web development", "Data science", "Game development"}
hobbies = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills}")
print(f"Learning Goals: {skills_to_learn}")
print(f"Career Interests: {career_iterest}")
print(f"Skills Currently Have: {len(current_skills)}")
print(f"Skills Want to Learn: {len(skills_to_learn)}\n")

monthly_budget = {"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100 } #Dictionary
daily_food_budget = round(monthly_budget["Food"] / 30, 2)
annual_budget = (
    monthly_budget["Food"] +
    monthly_budget["Entertainment"] +
    monthly_budget["Books"] +
    monthly_budget["Transportation"]
)*12 

print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_budget['Food'] + monthly_budget['Entertainment']
+ monthly_budget['Books'] + monthly_budget['Transportation']}")
print(f"Food: ${monthly_budget['Food']} (${daily_food_budget}/day)")
print(f"Entertainment: ${monthly_budget['Entertainment']}")
print(f"Books: ${monthly_budget['Books']}")
print(f"Transportation: ${monthly_budget['Transportation']}")
print(f"Annual Projection: ${annual_budget}\n")

emergency_contact = ("Mom", "Hannah Smith", "704-555-0199") #tuple
home_address = ("456 Oak Street", "Charlotte", "NC", "28202")
instagram_info = ("Instagram", "@jordan_codes", 312)
twitter_info = ("Twitter", "@jordandev", 127)
total_social_followers = instagram_info[2] + twitter_info[2]
contact_directory = {"Mom": "704-555-0199", "Roommate": "336-555-7821", "Academic Advisor": "336-334-5000"}

print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]}, {home_address[2]} {home_address[3]}")
print(f"Social Media Presence: {total_social_followers} followers across 2 platforms")
print(f"Key Contacts: {len(contact_directory)} people in directory\n")

total_courses_completed = 5
academic_load = total_credits + weekly_study_hours

print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {total_courses_completed}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {len(entertainment)} items")
print(f"Current Hobbies: {len(hobbies)} activities")

