import PyPDF2
import re
import csv

def extract_pdf_data(file_path):

    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        

        text = re.sub(r'\n+', '\n', text).strip()


        experience = ""
        education = ""
        skills = ""

        lines = text.split('\n')
        section = None

        for line in lines:
            line = line.strip()
            

            if line.lower().startswith("experience"):
                section = "experience"
                continue
            elif line.lower().startswith("education"):
                section = "education"
                continue
            elif line.lower().startswith("skills"):
                section = "skills"
                continue
     
            if section == "experience":
                experience += " " + line
            elif section == "education":
                education += " " + line
            elif section == "skills":
                skills += " " + line


        experience = experience.strip()
        education = education.strip()
        skills = skills.strip()
        
        if experience:
            experience = experience[0].upper() + experience[1:]
        if education:
            education = education[0].upper() + education[1:]
        if skills:
            skills = skills[0].upper() + skills[1:]


        formatted_experience = re.sub(r'●', '\n●', experience).strip()
        formatted_education = education
        formatted_skills = re.sub(r'●', '\n●', skills).strip()

        return formatted_experience, formatted_education, formatted_skills

    except FileNotFoundError:
        return "Error: File not found. Please check the file path."
    except Exception as e:
        return f"An error occurred: {e}"

def save_to_csv(experience, education, skills, output_file):

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Section", "Content"]) 
        writer.writerow(["Experience", experience])
        writer.writerow(["Education", education])
        writer.writerow(["Skills", skills])

if __name__ == "__main__":
    file_path = "sample-resume.pdf"  # Change this to the actual path of your PDF file
    output_csv = "parsed_resume.csv"  # Name of the output CSV file


    result = extract_pdf_data(file_path)
    if isinstance(result, tuple):
        experience, education, skills = result

  
        save_to_csv(experience, education, skills, output_csv)
        print(f"Extracted data has been saved to {output_csv}.")
    else:
        print(result)
