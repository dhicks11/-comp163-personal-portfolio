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

current_courses = ["COMP 163", "MATH 131", "SPCH 250", "HIST 106", "GEEN 111", "COMP 390"] #list  
credit_hours = [3, 4, 3, 3, 1, 3]
gpa_history = ["I dont have a GPA yet"]
weekly_study_hours = 20
study_hours_per_subject = {
    "Programming": 12,
    "Math": 5,
    "Speech": 1,
    "History": 2
    }
study_hour_value = 15.0
total_credits = sum(credit_hours)
cumulative_gpa = gpa_history

print(f"Current Semester: {total_credits} credits across {len(current_courses)} courses")
print(f"Cumulative GPA: {cumulative_gpa:}")
print(f"Weekly Study Time: {weekly_study_hours} hours")
print(f"Academic Investment: ${study_hour_value} per study hour\n")

course_credits = {"COMP 163": 3, "MATH 131": 4, "SPCH 250": 3, "HIS 106": 3, "GEEN 111": 1, "COMP 390": 3} #dictionary
professors = {"COMP 163": "Prof. Rhodes", "MATH 131": "Dr. Varathajah", "SPCH 250": "Prof. Vogleson", "HIS 106": "Prof. Devoe", "GEEN 111": "Dr. Parish", "COMP 390": "Prof. Pioro"}
rooms = {"COMP 163": "M-Eric 300", "MATH 131": "Marteena 233", "SPCH 250": "Online", "HIS 106": "Online", "GEEN 111": "Mcnair ", "COMP 390": "Mcnair 240"}
print("Current Courses:")
print(f"{current_courses[0]} - {credit_hours[0]} credits - {professors['COMP 163']} - {rooms['COMP 163']}")
print(f"{current_courses[1]} - {credit_hours[1]} credits - {professors['MATH 131']} - {rooms['MATH 131']}")
print(f"{current_courses[2]} - {credit_hours[2]} credits - {professors['SPCH 250']} - {rooms['SPCH 250']}")
print(f"{current_courses[3]} - {credit_hours[3]} credits - {professors['HIS 106']} - {rooms['HIS 106']}")
print(f"{current_courses[4]} - {credit_hours[4]} credits - {professors['GEEN 111']} - {rooms['GEEN 111']}")
print(f"{current_courses[5]} - {credit_hours[5]} credits - {professors['COMP 390']} - {rooms['COMP 390']}\n")

current_skills = {"Python basics", "Leadership", "Problem solving", "Time management", "Adaptability"} #set
skills_to_learn = {"JavaScript", "Data structures", "Git", "HTML", "C++"}
career_iterest = {"Software development", "Project Management", "Cybersecurity"}
hobbies = {"Gaming", "Basketball", "Family time", "Runnning", "Music"}
entertainment = {"Stranger Things", "American Dad", "Family Guy", "Breaking Bad", "Surfs up"}

print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills}")
print(f"Learning Goals: {skills_to_learn}")
print(f"Career Interests: {career_iterest}")
print(f"Skills Currently Have: {len(current_skills)}")
print(f"Skills Want to Learn: {len(skills_to_learn)}\n")

monthly_budget = {"Food": 150, "Entertainment": 50, "Books": 25, "Transportation": 150 } #Dictionary
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

emergency_contact = ("Mom", "Shalonda Hicks", "252-555-7777") #tuple
home_address = ("263 Windsor Lake Dr", "Henrico", "NC", "23236")
instagram_info = ("Instagram", "@kha1r3", 536)
twitter_info = ("Twitter", "@dtootrill", 120)
total_social_followers = instagram_info[2] + twitter_info[2]
contact_directory = {"Mom": "252-555-7777", "Roommate": "336-252-8963", "Academic Advisor": "336-334-6399"}

print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]}, {home_address[2]} {home_address[3]}")
print(f"Social Media Presence: {total_social_followers} followers across 2 platforms")
print(f"Key Contacts: {len(contact_directory)} people in directory\n")

total_courses_completed = 22
academic_load = total_credits + weekly_study_hours

print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {total_courses_completed}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {len(entertainment)} items")
print(f"Current Hobbies: {len(hobbies)} activities")

