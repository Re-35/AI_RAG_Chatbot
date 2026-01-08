import pdfplumber

def convert(path, file_name):
    with pdfplumber.open(path) as pdf_file, open(file_name, "w", encoding="utf-8") as f:
        for page in pdf_file.pages:
            text = page.extract_text()
            if text:
                f.write(text + '\n')

    print("Process Done for " + file_name)


# Use function:

convert("ML_ChatBot\Data\Hands_On_Machine_Learning_with_Scikit_Learn_Keras_and_TensorFlow.pdf", "Hands_on_book.txt")
convert("ML_ChatBot\Data\Andrew Ng Complete Machine learning Notes.pdf", "Andrew_NG_notes.txt")
convert("ML_ChatBot\Data\math4ml.pdf", "math_ML.txt")