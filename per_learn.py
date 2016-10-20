import os
import sys
import random
import timeit
import json
max_iter = 20
import cProfile

def main():
    path = "train"
    file_list = []
    b = 0
    vocab = {}
    file_contents = {}

    for root, subdir, files in os.walk(path):
        if len(files):
            for f in files:
                file_list.append(os.path.join(root, f))

    for i in range(max_iter):
        # No shuffle required for first iteration
        if i != 0:
            random.shuffle(file_list)

        n = len(file_list)
        for j in range(n):
            file_path = file_list[j]
            alpha = b
            y = 1 if "spam" in file_path else -1

            # Avoid opening and reading the file for each iteration. So save it in dictionary
            if i == 0:
                with open(file_path, "r", encoding="latin1") as fs:
                    if i == 0:
                        content = fs.read().strip().split()
                        file_contents[file_path] = content
            else:
                content = file_contents[file_path]
            if j == 0:
                alpha = 0
            else:
                if word in vocab:
                    alpha += vocab[word]
            if y*alpha <= 0:
                for word in content:
                    if word in vocab:
                        vocab[word] += y
                    else:
                        vocab[word] = y
                b += y

    with open("per_model.txt", 'w') as fs:
        fs.write(json.dumps((vocab, b)))


if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print("Update process:" + str(end - start))
    cProfile.run('main()', 'myFunction.profile')


import pstats
stats = pstats.Stats('myFunction.profile')
stats.strip_dirs().sort_stats('time').print_stats()
