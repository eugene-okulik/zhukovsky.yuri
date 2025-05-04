import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Logs folder")
parser.add_argument("--text", help="Searching text in logs")
args = parser.parse_args()

folder_path = args.path
search_text = args.text

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            # content = file.read()
            # print(content)
            for line_number, line in enumerate(file, start=1):
                words = line.split()
                for i, word in enumerate(words):
                    if word == search_text:
                        start_index = max(0, i - 5)
                        end_index = min(len(words), i + 6)
                        context = words[start_index:end_index]
                        print(f'Файл {filename} / строка {line_number}: {" ".join(context)}')
