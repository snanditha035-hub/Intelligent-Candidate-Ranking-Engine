import re
import pdfplumber

# -------------------------
# Read Resume
# -------------------------

pdf = pdfplumber.open("resumes/Resume_Aarav_Menon_Detailed.pdf")

text = ""

for page in pdf.pages:

    page_text = page.extract_text()

    if page_text:

        text += page_text + "\n"

pdf.close()

# -------------------------
# Clean Resume
# -------------------------

clean_text = text.replace("\n"," ")

clean_text = re.sub(r'\s+',' ',clean_text)

print(clean_text)

# extract email

email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

email = re.search(email_pattern,clean_text)

if email:

    email = email.group()

else:

    email = "Not Found"

print(email)

#extract phone number

phone_pattern = r'(\+91[- ]?)?[6-9]\d{9}'

phone = re.search(phone_pattern,clean_text)

if phone:

    phone = phone.group()

else:

    phone = "Not Found"

print(phone)

# extract linkedin

linkedin_pattern = r'https?://(www\.)?linkedin\.com/[^\s]+'

linkedin = re.search(linkedin_pattern,clean_text)

if linkedin:

    linkedin = linkedin.group()

else:

    linkedin = "Not Found"

print(linkedin)

#extract github

github_pattern = r'https?://(www\.)?github\.com/[^\s]+'

github = re.search(github_pattern,clean_text)

if github:

    github = github.group()

else:

    github = "Not Found"

print(github)

#extract name

lines = text.split("\n")

name = lines[0]

print(name)

#extract age

age_pattern = r'Age[: ]+(\d{2})'

age = re.search(age_pattern,text,re.IGNORECASE)

if age:

    age = age.group(1)

else:

    age = "Not Mentioned"

print(age)

# extract degree

degrees = [

"B.Tech",

"BE",

"B.E",

"M.Tech",

"M.E",

"BSc",

"MSc",

"PhD",

"Diploma"

]

degree = "Not Found"

for d in degrees:

    if d.lower() in clean_text.lower():

        degree = d

        break

print(degree)

 # extract cgpa

cgpa_pattern = r'CGPA[: ]+(\d+\.\d+)'

cgpa = re.search(cgpa_pattern,text,re.IGNORECASE)

if cgpa:

    cgpa = cgpa.group(1)

else:

    cgpa = "Not Found"

print(cgpa)

#extract percentage

percentage_pattern = r'(\d{2}\.?\d*)%'

percentage = re.search(percentage_pattern,text)

if percentage:

    percentage = percentage.group()

else:

    percentage = "Not Found"

print(percentage)

#extract expereince

experience_pattern = r'(\d+)\s+Years?'

experience = re.search(experience_pattern,text,re.IGNORECASE)

if experience:

    experience = experience.group(1)

else:

    experience = "0"

print(experience)

#extract skills

skills_database=[

"Python",

"Java",

"C",

"C++",

"SQL",

"MySQL",

"Machine Learning",

"Deep Learning",

"TensorFlow",

"PyTorch",

"HTML",

"CSS",

"JavaScript",

"React",

"NodeJS",

"Git",

"Docker",

"AWS",

"Azure",

"Arduino",

"ESP32",

"Embedded Systems",

"Verilog",

"MATLAB",

"PCB Design",

"VLSI"

]
skills=[]

for skill in skills_database:

    if skill.lower() in clean_text.lower():

        skills.append(skill)

print(skills)

# extract college 

college_keywords = [

"College",

"Institute",

"University"

]
lines = text.split("\n")

college = "Not Found"

for line in lines:

    for word in college_keywords:

        if word.lower() in line.lower():

            college = line.strip()

            break
print(college)

#extract branch

branches = [

"Computer Science",

"Electronics",

"Electronics and Communication",

"Mechanical",

"Civil",

"Information Technology",

"Artificial Intelligence",

"Data Science"

]
branch = "Not Found"

for b in branches:

    if b.lower() in clean_text.lower():

        branch = b

        break

print(branch)

#extract passing year

year_pattern = r'(20[0-4][0-9]|2050)'
years = re.findall(year_pattern,text)

print(years)
passing_year = years[-1]

#extracting project

projects = []

capture = False

for line in lines:

    if "projects" in line.lower():

        capture = True

        continue

    if capture:

        if line.strip()=="":
            continue

        if line.lower() in [

"internships",

"achievements",

"certifications",

"education"

]:

            break

        projects.append(line.strip())

# extract internship

internships=[]

capture=False

for line in lines:

    if "internship" in line.lower():

        capture=True

        continue

    if capture:

        if line.strip()=="":
            continue

        if line.lower() in [

"projects",

"certifications",

"achievements"

]:

            break

        internships.append(line.strip())

#extract certificate

certifications=[]

capture=False

for line in lines:

    if "certification" in line.lower():

        capture=True

        continue

    if capture:

        if line.strip()=="":
            continue

        if line.lower() in [

"projects",

"internships",

"achievements"

]:

            break

        certifications.append(line.strip())

#extract acheivements

achievements=[]

capture=False

for line in lines:

    if "achievement" in line.lower():

        capture=True

        continue

    if capture:

        if line.strip()=="":
            continue

        if line.lower() in [

"projects",

"internships",

"certifications"

]:

            break

        achievements.append(line.strip())

#extract languages

languages=[]

capture=False

for line in lines:

    if "languages" in line.lower():

        capture=True

        continue

    if capture:

        if line.strip()=="":
            continue

        languages.append(line.strip())

candidate={

"name":name,

"email":email,

"phone":phone,

"age":age,

"degree":degree,

"branch":branch,

"college":college,

"cgpa":cgpa,

"percentage":percentage,

"experience":experience,

"passing_year":passing_year,

"skills":skills,

"projects":projects,

"internships":internships,

"certifications":certifications,

"achievements":achievements,

" languages":languages,

"linkedin":linkedin,

"github":github

}
print("\n========== Candidate Details ==========\n")

for key,value in candidate.items():

    print(key," : ",value)
