
<h2>Evolutionary Algorithm: Language Processing</h2><br>
Extractive Summarization

Install all required packages (pandas, numpy, mlxtend, and PyMuPDF (fitz) version 1.18.9) in the environment.yml, and run python main.py from the project's root directory with the following command-line arguments.
1. name/path to the input pdf file
2. length (number of sentences) of the summary

Example command:
python main.py sample_input.pdf 10

The program will output the summary in the terminal, in addition to creating output.pdf, which has the extractive summary sentences highlighted in yellow.

Main.py reads the input pdf file using PyMuPDF, tags the content and extracts the paragraphs, encodes a similarity matrix representing the sentence similarities for all the paragraph sentences, and calls ea.py that finds the optimal summary by an evolutionary process.
