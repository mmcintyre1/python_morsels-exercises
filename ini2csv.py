import configparser
import csv
import sys


def read_config(config_location):
    config = configparser.ConfigParser()
    config.read(config_location)
    return config


def output_csv(data, output_location):
    with open(output_location, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(data)


def run(config_location, output_location, collapsed=False):
    config = read_config(config_location)
    if collapsed:
        data = []

    else:
        data = [
            [section, k, config[section][k]] for section in config.sections()
            for k in config[section]
        ]

    output_csv(data, output_location)


def main(sys_argv):
    config_location, output_location = sys_argv
    run(config_location, output_location)


if __name__ == "__main__":
    main(sys.argv[1:])


