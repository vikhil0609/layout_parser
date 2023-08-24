import time
import datetime
import requests
from PyPDF2 import PdfReader
import io

url = 'https://blr1.vultrobjects.com/patents/document/161854667/azure_file/734a86a80c081b874bcd674c7ee9ea68.pdf'
# url = 'https://blr1.vultrobjects.com/patents/2023/05/08/0cdbf1ca1b7d8ff2f3ba1f80a0d95eda.pdf'

start_time = datetime.datetime.now()

# Download the PDF
response = requests.get(url)
pdf_bytes = response.content

# Create a PDF reader object
pdf_reader = PdfReader(io.BytesIO(pdf_bytes))

# Loop through each page and save it as separate bytes
page_bytes_list = []
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    page_text = page.extract_text()
    page_bytes = page_text.encode('utf-8')  # Convert text to bytes
    page_bytes_list.append(page_bytes)

for page in page_bytes_list:
    print(page)

# Print the total number of pages
print("Total Pages:", len(page_bytes_list))

end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print("Elapsed Time:", elapsed_time)
