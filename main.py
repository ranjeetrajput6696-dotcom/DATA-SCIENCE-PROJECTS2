# ================================
# STEP 1 : CREATE PROJECT FOLDER
# ================================

mkdir DATA-SCIENCE-PROJECTS

cd DATA-SCIENCE-PROJECTS


# ================================
# STEP 2 : CREATE ALL FILES/FOLDERS
# ================================

mkdir Data-Analysis
mkdir Machine-Learning
mkdir Deep-Learning
mkdir NLP-Projects
mkdir PowerBI-Dashboard
mkdir SQL-Projects
mkdir Excel-Projects
mkdir Dataset

type nul > README.md
type nul > requirements.txt
type nul > .gitignore
type nul > LICENSE
type nul > main.py


# ================================
# STEP 3 : INITIALIZE GIT
# ================================

git init


# ================================
# STEP 4 : ADD ALL FILES
# ================================

git add .


# ================================
# STEP 5 : COMMIT FILES
# ================================

git commit -m "Initial Commit - Data Science Projects"


# ================================
# STEP 6 : CREATE MAIN BRANCH
# ================================

git branch -M main


# ================================
# STEP 7 : CONNECT GITHUB REPOSITORY
# ================================

git remote add origin https://github.com/your-username/DATA-SCIENCE-PROJECTS.git


# Example
# git remote add origin https://github.com/ranjeetkumar/DATA-SCIENCE-PROJECTS.git


# ================================
# STEP 8 : PUSH CODE TO GITHUB
# ================================

git push -u origin main


# ================================
# STEP 9 : FUTURE UPDATE COMMANDS
# ================================

git add .

git commit -m "Project Updated"

git push
