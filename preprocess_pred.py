#!/usr/bin/python3 

from argparse import ArgumentParser
from preprocess import process_file

import common


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--raw_data', help='Path to source data file', required=True)
    parser.add_argument('--raw_names', help='Path to source names file', required=True)

    parser.add_argument("-mc", "--max_contexts", dest="max_contexts", default=200,
                        help="number of max contexts to keep", required=False)
    parser.add_argument("-wvs", "--word_vocab_size", dest="word_vocab_size", default=1301136,
                        help="Max number of origin word in to keep in the vocabulary", required=False)
    parser.add_argument("-pvs", "--path_vocab_size", dest="path_vocab_size", default=911417,
                        help="Max number of paths to keep in the vocabulary", required=False)
    parser.add_argument("-tvs", "--target_vocab_size", dest="target_vocab_size", default=261245,
                        help="Max number of target words to keep in the vocabulary", required=False)

    parser.add_argument("-wh", "--word_histogram", dest="word_histogram",
                        help="word histogram file", metavar="FILE", required=True)
    parser.add_argument("-ph", "--path_histogram", dest="path_histogram",
                        help="path_histogram file", metavar="FILE", required=True)
    parser.add_argument("-th", "--target_histogram", dest="target_histogram",
                        help="target histogram file", metavar="FILE", required=True)
    parser.add_argument("-o", "--output_name", dest="output_name",
                        help="output name - the base name for the created dataset", metavar="FILE", required=True,
                        default='data')
    args = parser.parse_args()

    _, _, _, word_to_count = common.common.load_vocab_from_histogram(args.word_histogram, start_from=1,
                                                                     max_size=int(args.word_vocab_size),
                                                                     return_counts=True)
    _, _, _, path_to_count = common.common.load_vocab_from_histogram(args.path_histogram, start_from=1,
                                                                     max_size=int(args.path_vocab_size),
                                                                     return_counts=True)
    _, _, _, target_to_count = common.common.load_vocab_from_histogram(args.target_histogram, start_from=1,
                                                                       max_size=int(args.target_vocab_size),
                                                                       return_counts=True)

    process_file(file_path=args.raw_data, data_file_role="test", dataset_name=args.output_name,
                 word_to_count=word_to_count, path_to_count=path_to_count,
                 max_contexts=int(args.max_contexts), names_path=args.raw_names)
