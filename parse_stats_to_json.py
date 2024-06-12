import json
from pprint import pprint

"""Read and clean the log file"""
def string_cleaner(string: str) -> str:
    return string.replace(' ', '').replace('\n', '')

#reading log file
with open('stats.log', 'r') as fp:
    data = fp.readlines()
   
def main():
    main_data = {}
    for i in data:
        if "-" not in i:
            new_data = [string_cleaner(value) for value in i.split("|")]
            new_data.pop(1) if len(new_data) > 1 else ""
            if new_data[1].isdigit():
                main_data[new_data[0]] = int(new_data[1])
            else:
                new_data[1]
    pprint(main_data)
#Storing the clean data in json file for the project
    with open('new_data.json', 'w') as fp:
        json.dump(main_data, fp, indent=4)
        pprint(main_data)


if __name__ == '__main__':
    main()


