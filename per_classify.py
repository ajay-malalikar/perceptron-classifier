import os
import json
import sys
import timeit


def main(path, op):
    model = None
    with open("per_model.txt", "r", encoding="latin1") as fs:
        model = json.loads(fs.read())
    try:
        os.remove(op)
    except OSError:
        pass
    opfile = open(op, "a", encoding="latin1")
    for root, subdir, files in os.walk(path):
        if len(files):
            for f in files:
                with open(root+"/"+f, "r", encoding="latin1") as fs:
                    content = fs.read().strip().split()
                    alpha = model[1]
                    for word in content:
                        if word in model[0]:
                            alpha += model[0][word]
                    if alpha > 0:
                        # Spam
                        opfile.write("spam " + root + "/" + f + '\n')
                    else:
                        # Ham
                        opfile.write("ham " + root + "/" + f + '\n')
    opfile.close()


if __name__ == "__main__":
    start = timeit.default_timer()
    main(sys.argv[1], sys.argv[2])
    end = timeit.default_timer()
    print(str(end-start))
