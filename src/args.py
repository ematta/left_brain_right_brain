import argparse


def parse__args():
    """
    Parse a command line argument for the path to a PDF file.

    Returns an argparse.Namespace object with a single attribute, 'pdf_path',
    which is the path to the PDF file.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdf-path', type=str, required=False)
    parser.add_argument('--server', type=bool, required=False)
    args = parser.parse_args()
    return args