import random
from js import document

teams = ["Blue Bears", "Red Bulldogs", "Yellow Tigers", "Green Hornets"]

def check_eligibility(event):
    registered = document.getElementById("registered").value.lower()
    medical = document.getElementById("medical").value.lower()
    grade_str = document.getElementById("grade").value
    grade = int(grade_str.split()[1])
    
    output = document.getElementById("output")
    
    if registered != "yes":
        message = "You are NOT eligible.<br>Please register online first."
    elif medical != "yes":
        message = "You are NOT eligible.<br>Please secure a medical clearance."
    elif not (7 <= grade <= 10):
        message = "You are NOT eligible.<br>Grade level must be between 7 and 10."
    else:
        team = random.choice(teams)
        message = f"Congratulations! You are eligible to join the Intramurals.<br>Your assigned team is: {team}"
    
    output.innerHTML = message
