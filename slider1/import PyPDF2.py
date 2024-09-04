import PyPDF2
import re

def search_integers_in_pdf(pdf_path, integers):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages

        # Iterate through each page
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text = page.extractText()

            # Search for integers in the text
            for integer in integers:
                matches = re.findall(r'\b{}\b'.format(integer), text)
                if matches:
                    print(f"Found {integer} on page {page_num + 1}: {matches}")

# Example usage
pdf_path = 'your_pdf_file.pdf'
integers_to_search = [123, 456, 789]  # List of integers to search for
search_integers_in_pdf(pdf_path, integers_to_search)
