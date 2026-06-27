# Intelligent Candidate Ranking Engine

## Overview

This project is an AI-powered Applicant Tracking System (ATS) that automatically ranks candidates based on their resumes and a given job description.

The system extracts information from PDF resumes, stores candidate data in MySQL, calculates a matching score, ranks candidates, and displays the results using a Streamlit dashboard.

---

## Technologies Used

- Python
- MySQL
- Streamlit
- Pandas
- PDFPlumber
- Regular Expressions

---

## Features

- Resume Parsing
- Skill Extraction
- Education Extraction
- Experience Extraction
- Candidate Ranking
- Job Description Matching
- Dashboard Visualization

---

## Folder Structure

CandidateRanking/
│
├── resumes/
├── app.py
├── extractor.py
├── ranking.py
├── database.py
├── requirements.txt
└── README.md

---

## How to Run

Install dependencies

pip install -r requirements.txt

Run the dashboard

streamlit run app.py

---

## Developed By

Nanditha S