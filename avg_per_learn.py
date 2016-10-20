import os
import sys
import random
import timeit
import json


def main(path):
    file_list = []
    b = 0
    vocab = {}
    weighted_vocab = {}
    beta = 0
    c = 1

    for root, subdir, files in os.walk(path):
        if len(files):
            for f in files:
                file_list.append(os.path.join(root, f))

    for i in range(30):
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
                        alpha += vocab[word][0]

                if y * alpha <= 0:
                    for word in content:
                        if word in vocab:
                            vocab[word][0] += y
                            vocab[word][1] += y*c
                        else:
                            vocab[word] = [y, y*c]
                    b += y
                    beta += y * c
    for k, v in vocab.items():
        weighted_vocab[k] = vocab[k][0] - ((1 / c) * vocab[k][1])
    beta = 1 - ((1 / c) * beta)

    model = (weighted_vocab, beta)
    with open("per_model.txt", 'w') as fs:
        fs.write(json.dumps(model))


if __name__ == "__main__":
    start = timeit.default_timer()
    main(sys.argv[1])
    end = timeit.default_timer()
    print("Avg process:" + str(end - start))