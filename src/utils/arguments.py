import argparse


def int_range(minimum, maximum):
    def range_checker(arg):
        try:
            i = int(arg)
        except ValueError:
            raise argparse.ArgumentTypeError("must be an intetger")
        if i < minimum or i > maximum:
            raise argparse.ArgumentTypeError(f"must be in range [{str(minimum)}, {str(maximum)}]")
        return i

    return range_checker


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', dest='filename', required=False, default="test_data/test.png", type=str,
                        help='Path of the image file')
    parser.add_argument('-s', '--scale', dest='scale', required=False, default=1, type=int_range(1, 5),
                        help='Scale factor to enlarge image')
    args = parser.parse_args()
    return args.filename, args.scale
