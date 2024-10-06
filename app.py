import src.pdf as pdf
import src.model as model
import src.args as args

arguments = args.parse__args()

pdf_path = arguments.pdf_path

if arguments.server:
    import src.server as server
    server.app.run()
else:
    documents = pdf.parse_pdf_to_documents(pdf_path)
    index = model.create_index(documents, use_huggingface=True)

    while True:
        user_input = input('You: ')
        if user_input.lower() == 'exit':
            break
        response = model.query_documents(user_input, index, streaming=True)
        print(f'LLM: {response}')

