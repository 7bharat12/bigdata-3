# -*- coding: utf-8 -*-
"""
Created on Sat May 20 15:38:25 2023

@author: bhara
"""

with open('Shakespeare.txt', 'r') as input_file:
    with open('intermediate_output.txt', 'w') as output_file:
        for line in input_file:
            line = line.strip()
            words = line.split()
            for word in words:
                output_file.write(f"{word}\t1\n")
