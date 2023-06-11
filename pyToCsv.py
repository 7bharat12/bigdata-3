# -*- coding: utf-8 -*-
"""
Created on Mon May 22 21:10:51 2023

@author: bhara
"""

import csv

text_file = 'final_output.txt'
csv_file = 'final_output.csv'

with open(text_file, 'r') as input_file, open(csv_file, 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)

    for line in input_file:
        row = line.strip().split('\t')  # Adjust the delimiter if needed
        csv_writer.writerow(row)
