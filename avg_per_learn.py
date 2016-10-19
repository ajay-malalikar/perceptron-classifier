import os
import sys
import random
import timeit
import json
max_iter = 20


def main(path):
    file_list = []
    b = 0
    vocab = {}
    for root, subdir, files in os.walk(path):
        if len(files):
            for f in files:
                file_list.append(root + "/" + f)

    for i in range(20):
        random.shuffle(file_list)
        n = len(file_list)
        for j in range(n):
            file_path = file_list[j]
            alpha = b
            y = 1 if "spam" in file_path else -1

            with open(file_path, "r", encoding="latin1") as fs:
                content = fs.read().strip().split()
                for word in content:
                    if word in vocab:
                        alpha += vocab[word]

                if y*alpha <= 0:
                    for word in content:
                        if word in vocab:
                            vocab[word] += y
                        else:
                            vocab[word] = y
                    b += y
    model = (vocab, b)
    with open("per_model.txt", 'w') as fs:
        fs.write(json.dumps(model))

if __name__ == "__main__":
    start = timeit.default_timer()
    main(sys.argv[1])
    end = timeit.default_timer()
    print("Update process:" + str(end - start))