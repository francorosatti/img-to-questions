import argparse


def validate_arguments(args):
    if args.filename is None:
        exit(f"Filename argument --filename is required.")


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', dest='filename', required=False, default="test_data/test.png", type=str,
                        help='Path of the image file')
    args = parser.parse_args()
    validate_arguments(args)
    return args.filename
