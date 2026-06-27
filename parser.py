import pdfplumber

resume_path = "resumes/Resume_Aarav_Menon_Detailed.pdf"

pdf = pdfplumber.open(resume_path)

text = ""

for page in pdf.pages:

    page_text = page.extract_text()

    if page_text:

        text = text + page_text + "\n"

pdf.close()

print(text)

