import argparse


def parse_args():
    """
    Parse the command line arguments using the argparse library.

    Returns:
        An object of type argparse.Namespace containing the parsed arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdf-path', type=str, required=False)
    parser.add_argument('--server', type=bool, required=False)
    parser.add_argument('--new', type=bool, required=False)
    args = parser.parse_args()
    return args