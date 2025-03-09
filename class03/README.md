# 📌 Class 3 Code 
## 🔗 [click here to access class code](https://colab.research.google.com/drive/1qV0yypafjBqE10NMxDEXoJ4glgMc1ECM?usp=sharing)
[https://colab.research.google.com/drive/1qV0yypafjBqE10NMxDEXoJ4glgMc1ECM?usp=sharing](https://colab.research.google.com/drive/1qV0yypafjBqE10NMxDEXoJ4glgMc1ECM?usp=sharing)

### ✅ Assignment 1: Password Strength Meter  
Work on the **Password Strength Meter** project from the repository:  
🔗 [Password Strength Meter - GitHub Repo](https://github.com/panaversity/learn-modern-ai-python/tree/main/CLASS_PROJECTS/02_password_strength_meter)

### ✅ Assignment 2: Student Report Card Generator: Data Input and Grade Calculation System

## Program Description
**Objective:** The program is designed to collect student data and generate report cards interactively. Users will input data for each student, and the program will compile this into a formatted report card, complete with grades based on the students' performance.

### Functionality
1. **Data Input:** When the program starts, it prompts the user to enter the following details for a student:
   - **Student Name:** [User inputs the student's name]
   - **Roll Number:** [User inputs the student's roll number]
     - **Math:** [User inputs marks obtained]
     - **Physics:** [User inputs marks obtained]
     - **Urdu:** [User inputs marks obtained]
     - **English:** [User inputs marks obtained]
     - **Computer:** [User inputs marks obtained]
   After the details for one student are entered, the program will display the message:
   "Record of [Student Name] inserted successfully. Do you want to insert more? Press 'Y' for Yes or 'N' for No."

2. **Continuation Logic:** If the user presses 'Y', the program will prompt the entry of another student's data. If the user presses 'N', the program will terminate the input phase and proceed to generate the report cards.

3. **Report Generation:**
   - The program will display a list of all students whose data has been entered.
   - For each student, a marksheet will be generated displaying the marks in each subject.
   - The program calculates the total marks obtained and the percentage.
   - Based on the percentage, the program assigns a grade according to the following scale:
     - 40 to 49%: Grade F
     - 50 to 59%: Grade C
     - 60 to 69%: Grade B
     - 70 to 79%: Grade A
     - 80% and above: Grade A+

### Additional Features
- **Error Handling:** The program will include basic error handling to manage non-numeric input for marks and invalid choices (other than 'Y' or 'N').
- **User Interface:** A simple text-based interface will guide the user through the data entry and report viewing process.
- **Flexibility:** Users can input any number of students in a session, making the program suitable for batch processing at the end of program.
