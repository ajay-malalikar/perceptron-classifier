import os
import random
import subprocess
import sys


def randon_file_generator(path):
    spam_list = []
    ham_list = []
    for d, s, f in os.walk(path):
        for file in f:
            if "spam" in d:
                spam_list.append(os.path.join(d, file))
            else:
                ham_list.append(os.path.join(d, file))

    for i in range(5):
        random.shuffle(spam_list)
        random.shuffle(ham_list)

    n = int(len(spam_list)/10)
    spam_list = spam_list[:n]
    for i in range(n):
        subprocess.call('cp ' + spam_list[i] + ' train-10percent/spam/', shell=True)
    n = int(len(ham_list) / 10)
    ham_list = ham_list[:n]
    for i in range(n):
        subprocess.call('cp ' + ham_list[i] + ' train-10percent/ham/', shell=True)

randon_file_generator(sys.argv[1])
