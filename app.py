import src.pdf as pdf
import src.database as database
import src.model as model
import src.args as args

arguments = args.parse_args()

if arguments.server:
    import src.server as server
    server.app.run()
else:
    pdf_path = arguments.pdf_path
    if arguments.new:
        documents = pdf.pdf_documents(pdf_path)
        index = database.add_and_retrieve_document(documents=documents)
    else:
        index = database.load_documents()

    while True:
        user_input = input('You: ')
        if user_input.lower() == 'exit':
            break
        response = model.query_index(user_input, index, streaming=True)
        print(f'LLM: {response}')

