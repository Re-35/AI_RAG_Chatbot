def concate_docs(doc_path):
    with open("ML_ChatBot\Data\concateneted_docs.txt", "a", encoding='utf-8') as f:
        with open(doc_path, "r", encoding='utf-8') as reader:
            for line in reader:
                f.write(line)

    print("Done!")


# using the function:
concate_docs("ML_ChatBot\Data\Hands_on_book.txt")
concate_docs("ML_ChatBot\Data\Andrew_NG_notes.txt")
concate_docs("ML_ChatBot\Data\Static.txt")