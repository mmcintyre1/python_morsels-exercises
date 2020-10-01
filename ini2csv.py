import argparse
from configparser import ConfigParser
import csv
from functools import partial


def get_config_keys(config):
    return [s[0] for s in config.items(config.sections()[0])]


def collapse_config(config):
    data = [['header'] + get_config_keys(config)]
    for section in config.sections():
        section_data = [section]
        for k in config[section]:
            section_data.append(config[section][k])
        data.append(section_data)

    return data


def run(ini_file, csv_file, collapsed=False):
    config = ConfigParser()
    config.read_file(ini_file)

    if collapsed:
        data = collapse_config(config)
    else:
        data = [
            [section, k, config[section][k]] for section in config.sections()
            for k in config[section]
        ]

    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)


def main():
    parser = argparse.ArgumentParser()
    # we can use this, but windows doesn't like the lack of newline for the csv file
    # parser.add_argument('ini_file', argparse.FileType('rt'))

    # with the partial, it only applies partial arguments but allows us
    # to open a file when invoked
    parser.add_argument('ini_file', type=partial(open, mode='rt', newline=''))
    parser.add_argument('csv_file', type=partial(open, mode='wt', newline=''))
    parser.add_argument('--collapsed', action='store_true')

    args = parser.parse_args()

    run(args.ini_file, args.csv_file, args.collapsed)


if __name__ == "__main__":
    main()


