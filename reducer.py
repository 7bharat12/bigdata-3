# -*- coding: utf-8 -*-
"""
Created on Sat May 20 15:40:10 2023

@author: bhara
"""

word_counts = {}

with open('intermediate_output.txt', 'r') as file:
    for line in file:
        parts = line.strip().split('\t')

        if len(parts) != 2:
            continue

        word, count = parts
        count = int(count)

        if word in word_counts:
            word_counts[word] += count
        else:
            word_counts[word] = count

with open('final_output.txt', 'w') as output_file:
    for word, count in word_counts.items():
        output_file.write(f"{word}\t{count}\n")



