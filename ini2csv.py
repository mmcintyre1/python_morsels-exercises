import argparse
import configparser
import csv


def read_config(config_location):
    config = configparser.ConfigParser()
    config.read(config_location)
    return config


def output_csv(data, output_location):
    with open(output_location, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(data)


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


def run(config_location, output_location, collapsed=False):
    config = read_config(config_location)
    if collapsed:
        data = collapse_config(config)
    else:
        data = [
            [section, k, config[section][k]] for section in config.sections()
            for k in config[section]
        ]

    output_csv(data, output_location)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('--collapsed', action='store_true')

    args = parser.parse_args()

    run(args.input, args.output, args.collapsed)


if __name__ == "__main__":
    main()


