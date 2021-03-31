

import re,colections
# /Users/tower/Documents/作业/nlp/aclImdb/train/neg/65_4.txt

datasetpath="/Users/tower/Documents/作业/nlp/aclImdb/train/pos"

def get_words(file):
    with open(file) as f:
        words_box=[]
        for line in f:
            if re.match(r'[a-zA-Z0-9]*',line):
                words_box.extend(line.strip().split())
    return colections.Couter(words_box)

print(get_words("../aclImdb/train/neg/65_4.txt"))