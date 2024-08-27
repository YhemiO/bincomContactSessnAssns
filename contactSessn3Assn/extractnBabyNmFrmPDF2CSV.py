import csv
import pdfplumber
from bs4 import BeautifulSoup

# Step 1: Extract text from PDF
pdf_file_path = r"C:\Users\yemmys_pc\python_dev_beginner\classes\contact_sesssion_2\tablesourcecode1000.pdf"
html_content = ""

with pdfplumber.open(pdf_file_path) as pdf:
    for page_number in range(len(pdf.pages)):  # total pages if less
        page = pdf.pages[page_number]
        text = page.extract_text()
        html_content += text

# Step 3: Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Step 4: Extract data from the parsed HTML
headers = [header.text for header in (soup.find_all('th'))[1:]]
rows = soup.find_all('tr')

# Prepare data for CSV
data = [headers]
for row in rows[1:]:
    cols = row.find_all('td')
    data.append([col.text for col in cols[1:]])


# Save to CSV
csv_file_path = 'popularity_in_2008.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print(f"Data successfully written to {csv_file_path}")
