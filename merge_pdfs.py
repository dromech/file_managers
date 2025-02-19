import os
import sys
from PyPDF2 import PdfMerger

def merge_pdfs_in_folder(folder_path, output_path):
    # Ensure the folder exists
    if not os.path.isdir(folder_path):
        print(f"Error: The specified path '{folder_path}' is not a directory.")
        sys.exit(1)

    # Find all PDFs in the given folder
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    pdf_files.sort()

    if not pdf_files:
        print(f"No PDF files found in '{folder_path}'.")
        sys.exit(1)

    merger = PdfMerger()
    for pdf in pdf_files:
        full_path = os.path.join(folder_path, pdf)
        merger.append(full_path)
    merger.write(output_path)
    merger.close()

    print(f"All PDFs in '{folder_path}' have been merged into {output_path}")

if __name__ == "__main__":
    # Usage:
    # python merge_pdfs.py /path/to/folder output.pdf
    # If no output filename is given, defaults to "merged_output.pdf"
    #
    # If you just provide a folder path:
    # python merge_pdfs.py /path/to/folder
    # It will merge all PDFs into "merged_output.pdf".
    
    if len(sys.argv) < 2:
        print("Usage: python merge_pdfs.py /path/to/folder [output.pdf]")
        sys.exit(1)

    folder_path = sys.argv[1]
    output_pdf = sys.argv[2] if len(sys.argv) > 2 else "merged_output.pdf"

    merge_pdfs_in_folder(folder_path, output_pdf)