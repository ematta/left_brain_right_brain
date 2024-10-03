# type: ignore
import src.pdf as pdf
import src.llama_index as llama
import argparse

# Parse arguments and set the first argument as the path to the PDF file
parser = argparse.ArgumentParser(
    prog='ChatWithPDF',
    description='Chat with a PDF using LLMs')

parser.add_argument('pdf_path', type=str, help='Path to the PDF file')

args = parser.parse_args()

pdf_path = args.pdf_path

llama_docs = pdf.parse_pdf_to_llamaindex(pdf_path)

index = llama.load_documents(llama_docs)

query_engine = index.as_query_engine()

response = query_engine.query("Summarize the book in 5 sentences.")

print(response)
