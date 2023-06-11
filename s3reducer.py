# -*- coding: utf-8 -*-
"""
Created on Mon May 22 20:28:04 2023

@author: bharat
"""

import boto3

s3 = boto3.resource('s3')
bucket_name = 'shakespearebucket'
file_key = 'intermediate_output.txt'

word_counts = {}

# Read the file from S3
s3_object = s3.Object(bucket_name, file_key)
file_content = s3_object.get()['Body'].read().decode('utf-8')

# Perform word count
for line in file_content.split('\n'):
    parts = line.strip().split('\t')

    if len(parts) != 2:
        continue

    word, count = parts
    count = int(count)

    if word in word_counts:
        word_counts[word] += count
    else:
        word_counts[word] = count

# Print the word counts
for word, count in word_counts.items():
    print(f"{word}\t{count}")
