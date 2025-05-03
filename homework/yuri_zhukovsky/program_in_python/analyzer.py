import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Logs folder")
parser.add_argument("--text", help="Searching text in logs")
args = parser.parse_args()
