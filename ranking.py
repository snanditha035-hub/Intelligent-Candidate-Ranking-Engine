# ranking.py

import re

def read_job_description(filename):

    with open(filename, "r", encoding="utf-8") as file:
        jd = file.read()

    return jd

#read job description

job_description = read_job_description("job_description.txt")

print(job_description)

#clean

job_description = job_description.lower()

job_description = re.sub(r"\s+", " ", job_description)

#create skill database

skills_database = [

"python",

"java",

"c",

"c++",

"sql",

"mysql",

"machine learning",

"deep learning",

"tensorflow",

"pytorch",

"embedded systems",

"iot",

"arduino",

"pcb design",

"matlab",

"aws",

"azure",

"docker",

"git",

"linux",

"verilog"

]

#extract

required_skills=[]

for skill in skills_database:

    if skill in job_description:

        required_skills.append(skill)

print(required_skills)

#candidate skill

candidates = [

{
    "name": "Aarav",
    "degree": "B.Tech",
    "skills": ["python","sql","embedded systems","iot"],
    "experience": 2,
    "projects": [
        "AI Resume Ranking System using NLP",
        "Machine Learning Student Performance Prediction"
    ],
    "certifications": [
        "IBM Machine Learning",
        "Google Data Analytics"
    ]
},

{
    "name": "Priya",
    "degree": "B.Tech",
    "skills": ["python","iot","arduino","embedded systems"],
    "experience": 1,
    "projects": [
        "Smart Home Automation",
        "IoT Weather Monitoring System"
    ],
    "certifications": [
        "Arduino Programming",
        "IoT Fundamentals"
    ]
},

{
    "name": "Rahul",
    "degree": "B.Tech",
    "skills": ["verilog","c","embedded systems"],
    "experience": 0,
    "projects": [
        "4-bit ALU using Verilog"
    ],
    "certifications": [
        "Verilog HDL Basics"
    ]
}

]
for candidate in candidates:
#compare skills

 matched=[]

 for skill in candidate["skills"]:

    if skill.lower() in required_skills:

        matched.append(skill)

#skill score

skill_score = (

len(matched)

/

len(required_skills)

) * 100

print(skill_score)

#expereince score

required_experience = 1

candidate_experience = candidate["experience"]

if candidate_experience >= required_experience:

    experience_score = 100

else:

    experience_score = (

candidate_experience

/

required_experience

)*100
    
#education score

if candidate["degree"].lower()=="b.tech":

    degree_score=100

else:

    degree_score=0

#certificate score

certificate_score=80

#project score

project_keywords = []

for skill in skills_database:

    if skill.lower() in job_description.lower():

        project_keywords.append(skill)

print(project_keywords)
candidate["projects"]
candidate_projects = " ".join(candidate["projects"]).lower()
matched_projects = []

for keyword in project_keywords:

    if keyword.lower() in candidate_projects:

        matched_projects.append(keyword)

print(matched_projects)
if len(project_keywords) > 0:

    project_score = (

        len(matched_projects)

        /

        len(project_keywords)

    ) * 100

else:

    project_score = 0

print(project_score)



final_score = (

    skill_score * 0.45 +

    experience_score * 0.20 +

    degree_score * 0.10 +

    certificate_score * 0.10 +

    project_score * 0.15

)

print(final_score)

#rankings

candidates=[

{

"name":"Aarav",

"score":92

},

{

"name":"Priya",

"score":84

},

{

"name":"Rahul",

"score":79

}

]
candidates.sort(

key=lambda x:x["score"],

reverse=True
)
rank=1

for candidate in candidates:

    print(

rank,

candidate["name"],

candidate["score"]

)

    rank+=1