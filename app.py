import src.pdf as pdf
import src.database as database
import src.model as model
import src.args as args
import src.server as server

args = args.parse_args()

if args.server:
    server.app.run()
else:
    pdf_path = args.pdf_path
    if args.new:
        index = database.add_and_retrieve_document(documents=pdf.pdf_documents(pdf_path))
    else:
        index = database.load_documents()

    while True:
        user_input = input('You: ')
        if user_input.lower() == 'exit':
            break
        response = model.query_index(user_input, index)
        print(f'LLM: {response}')

