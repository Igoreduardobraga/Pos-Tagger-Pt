# POS Tagging in Portuguese using BERT and Mac-Morpho

This repository presents a solution for the task of Part-of-Speech (POS) tagging in Brazilian Portuguese using a BERT-based model fine-tuned on the Mac-Morpho corpus.

## Objective

The main goal is to automatically label each word in a sentence with its corresponding grammatical category (e.g., noun, verb, adjective), taking context into account. We use a pre-trained transformer model fine-tuned specifically for POS tagging in Portuguese, ensuring high performance with low computational cost.

## Motivation

The decision to use a pre-fine-tuned model was based on:

- Avoiding the need to train a model from scratch, saving time and resources.
- Starting with high accuracy, as the model was trained for the exact task on the target language.
- Simplifying the development and evaluation process, making the solution more accessible and reproducible.

## Project Structure

The Jupyter notebook provided walks through the following steps:

1. **Data Loading**: Load train, validation, and test files from the Mac-Morpho corpus.
2. **Model Initialization**: Load the `lisaterumi/postagger-portuguese` model from Hugging Face.
3. **Tag Prediction**: Apply the model to predict POS tags for input sentences.
4. **Evaluation**: Compute precision, recall, F1-score, and generate a classification report.
5. **Visual Analysis**: Display bar plots for metrics and a confusion matrix.
6. **Error Analysis**: Identify common misclassifications and underperforming tags.

## Results

- The model achieved strong performance, with most classes having F1-scores above 0.5.
- High-performing tags include `V` (verb), `ART` (article), `PU` (punctuation), and `NPROP` (proper noun).
- Lower performance was observed on tags such as `ADV` (adverb), `NUM` (numeral), and particularly `CUR`, which was rarely predicted correctly.

## Requirements

- Python 3.8+
- Required packages:
  - pandas
  - scikit-learn
  - transformers
  - torch
  - matplotlib
  - seaborn
  - numpy

Install with:

```bash
pip install -r requirements.txt
```

(ou instale manualmente conforme sua necessidade)

## How to use

1. Clone the repository:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

2. Download the Mac-Morpho corpus:

Avaiable at: http://nilc.icmc.usp.br/macmorpho/macmorpho-v3.tgz

3. Extract and place the following files in the root directory:

- macmorpho-train.txt
- macmorpho-dev.txt
- macmorpho-test.txt

4. Run the notebook to reproduce the analysis and results.

## References:

NILC/USP – Mac-Morpho Corpus: http://nilc.icmc.usp.br/macmorpho/

Modelo pré-treinado: lisaterumi/postagger-portuguese

Biblioteca Transformers: https://huggingface.co/transformers/