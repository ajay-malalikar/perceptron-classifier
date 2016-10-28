import sys
import os


def main(dev, op):
    spam_count, ham_count = 0, 0
    correct_spam_count, correct_ham_count = 0, 0
    classified_as_spam, classified_as_ham = 0, 0

    for root, subdir, files in os.walk(dev):
        if len(files):
            if "ham" in root:
                ham_count += len(files)
            elif "spam" in root:
                spam_count += len(files)

    with open(op, "r", encoding="latin1") as fs:
        for data in fs:
            data = data.strip().split()
            if "ham" in data[1]:
                classified_as_ham += 1
                if data[0] == "ham":
                    correct_ham_count += 1
            elif "spam" in data[1]:
                classified_as_spam += 1
                if data[0] == "spam":
                    correct_spam_count += 1

    precision_spam = correct_spam_count / classified_as_spam
    precision_ham = correct_ham_count / classified_as_ham
    recall_spam = correct_spam_count / spam_count
    recall_ham = correct_ham_count / ham_count

    print("Precision(spam): " + str(precision_spam))
    print("Recall(spam): " + str(recall_spam))
    print("F1(spam): " + str((2 * precision_spam * recall_spam) / (precision_spam + recall_spam)))
    print("Precision(ham): " + str(precision_ham))
    print("Recall(ham): " + str(recall_ham))
    print("F1(ham): " + str((2 * precision_ham * recall_ham) / (precision_ham + recall_ham)))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])