#! /usr/bin/env python
"""Script that creates a new problem folder starting
from the problem's URL"""

import argparse
import os
import shutil
import stat

import requests
import tomd

from bs4 import BeautifulSoup
from yaspin import yaspin

parser = argparse.ArgumentParser(description='Creates a new AoC folder.')
parser.add_argument('url', type=str, help='The URL of the problem')
parser.add_argument('session', type=str, help='The value of the "session" cookie')
args = parser.parse_args()

url = args.url
session = args.session
cookies = dict(session=session)

url_parts = url.split('/')
year = url_parts[-3]
day = url_parts[-1]

response = requests.get(
    url,
    cookies=cookies)
if response.status_code != 200:
    print("Oops... Something does not work :( " \
        "the request failed with status {}".format(response.status_code))
    quit()

# Setup folder structure
problem_folder = '{}/{}'.format(year, day)
if not os.path.exists(problem_folder):
    os.makedirs(problem_folder)

readme_file_path = '{}/README.md'.format(problem_folder)
input_file_path = '{}/input'.format(problem_folder)
boilerplate_folder = 'boilerplates/{}'.format(year)

# Start parsing the problem
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# Write the readme file with the problem statement
with open(readme_file_path, "w") as readme:
    for i, day in enumerate(soup.find_all('article', class_='day-desc')):
        part = i+1

        with yaspin(text=f"Adding problem text for part {part}") as spinner:
            readme.write(tomd.Tomd(str(day)).markdown)
            spinner.ok("✔ ")

        next_sibling = day.next_sibling.next_sibling
        if next_sibling.name == 'p' \
                and next_sibling.text[:4] == 'Your':
            print(" Found solution to part {}! Good work!".format(part))
            readme.write("\n<details><summary>Spoiler alert!</summary>\n\n"
                         "<p>{}</p></details>\n".format(next_sibling.text))

# Download the problem input, if exists
with yaspin(text="Downloading the input file") as spinner:
    file_url = '{}/input'.format(url)
    file_response = requests.get(file_url, stream=True, cookies=cookies)
    if file_response.status_code == 200:
        with open(input_file_path, "w") as _input:
            _input.write(file_response.text)
            spinner.ok("✔ ")

# Clone the boilerplate
for boilerplate_file in os.listdir(boilerplate_folder):
    source_file = os.path.join(boilerplate_folder, boilerplate_file)
    dest_file = os.path.join(problem_folder, boilerplate_file)
    if not os.path.exists(dest_file):
        shutil.copyfile(source_file, dest_file)

    _, file_extension = os.path.splitext(dest_file)
    if file_extension == '.py':
        st = os.stat(dest_file)
        os.chmod(dest_file, st.st_mode | stat.S_IEXEC)
