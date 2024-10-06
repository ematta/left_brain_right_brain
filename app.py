import src.pdf as pdf
import src.model as model
import src.args as args

pdf_path = args.parse__arg_for_pdf_path()

documents = pdf.parse_pdf_to_documents(pdf_path)

index = model.create_index(documents, use_huggingface=True)

while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        break
    response = model.query_documents(user_input, index)
    response.print_response_stream()
    print('')

