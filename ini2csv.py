import configparser
import csv
from os import PathLike
import sys


def read_config(config_location: PathLike) -> configparser.ConfigParser:
    """
    Reads a config file.
    :param config_location: location of a config file
    :return: a configparser object
    """
    config = configparser.ConfigParser()
    config.read(config_location)
    return config


def output_csv(data, output_location):
    pass


def run(config_location, output_location):
    pass


def main(sys_argv):
    config_location, output_location = sys_argv
    run(config_location, output_location)


if __name__ == "__main__":
    main(sys.argv[1:])


