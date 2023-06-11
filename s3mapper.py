# -*- coding: utf-8 -*-
"""
Created on Mon May 22 20:26:36 2023

@author: bharat
"""

import boto3

s3 = boto3.resource('s3')

input_bucket = 'shakespearebucket'
input_file_key = 'Shakespeare.txt'

output_bucket = 'shakespearebucket'
output_file_key = 'intermediate_output.txt'

input_object = s3.Object(input_bucket, input_file_key)
input_data = input_object.get()['Body'].read().decode('utf-8')

with open(output_file_key, 'w') as output_file:
    for line in input_data.split('\n'):
        line = line.strip()
        words = line.split()
        for word in words:
            output_file.write(f"{word}\t1\n")

s3.Object(output_bucket, output_file_key).upload_file(output_file_key)
