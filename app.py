import src.pdf as pdf
import src.database as database
import src.model as model
import src.args as args
import src.server as server

parsed = args.parse_args()

if parsed.server:
    server.app.run()
else:
    pdf_path = parsed.pdf_path
    if parsed.new:
        doc_pdf = pdf.load_documents(pdf_path)
        index = database.add_documents_and_retrieve_index(documents=doc_pdf)
    else:
        index = database.load_documents()

    while True:
        user_input = input('You: ')
        if user_input.lower() == 'exit':
            break
        response = model.query_index(user_input, index)
        print(f'LLM: {response}')
