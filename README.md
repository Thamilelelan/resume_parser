# Resume Parser with CSV Export  

This project is part of Task 3 for my internship at **Cothon Solutions**. A Python-based tool that extracts key information from resumes in PDF format and organizes it into a CSV file. 

## Overview  

The Resume Parser automates the process of extracting essential details from resumes, saving time and effort in manual data handling. It identifies sections like **Experience**, **Education**, and **Skills** and stores the parsed information in a structured CSV format.

## Features  

- Reads PDF resumes and extracts text using the **PyPDF2** library.  
- Identifies and organizes the following sections:  
  - **Experience**  
  - **Education**  
  - **Skills**  
- Formats and cleans the extracted data for better readability.  
- Saves the organized data into a CSV file for further use.

## Requirements  

- Python 3.x  
- Libraries:  
  - `PyPDF2`  
  - `re`  

## Usage  

1. Clone the repository:  
2. Install the required libraries
3. Place the PDF resume in the same directory as the script ( with the name `sample-resume` or change the file path in the code ).
4. Run the script
5. Check the output CSV file for the parsed data

### Note

A sample resume and the ouput csv file are give in the repository for reference. Delete them if you want
