import PyPDF2

def count_words_in_pdf(pdf_file_path):
    """Counts the total number of words in a PDF file."""
    
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        total_word_count = 0

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()

            # Handle potential encoding issues
            try:
                page_words = page_text.split()
            except UnicodeDecodeError:
                print(f"Warning: Encoding issue on page {page_num + 1}")
                page_words = []
            total_word_count += len(page_words)
    return total_word_count

# Example usage:
pdf_file_path = "chapter2.pdf"  # Replace with the actual file path
word_count = count_words_in_pdf(pdf_file_path)
print("Total word count:", word_count)
