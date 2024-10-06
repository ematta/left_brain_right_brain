import argparse


def parse__arg_for_pdf_path():
    """
    Parse the --pdf-path argument from the command line.

    Returns:
        The path to the PDF file to parse.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdf-path', type=str, required=True)
    args = parser.parse_args()
    pdf_path = args.pdf_path
    return pdf_path