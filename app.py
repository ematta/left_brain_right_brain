import src.pdf as pdf
import src.model as llama
import src.args as args

pdf_path = args.parse__arg_for_pdf_path()()

documents = pdf.parse_pdf_to_documents(pdf_path)

index = llama.create_index(documents, use_huggingface=True)

query_engine = index.as_query_engine(streaming=True)

while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        break
    response = query_engine.query(user_input)
    response.print_response_stream()
    print('')

