import spacy
import scispacy
from spacy import displacy

# spacy.load("en_ner_bc5cdr_md")
# spacy.load(" en_ner_bionlp13cg_md")

import en_ner_bc5cdr_md   
import en_ner_bionlp13cg_md
import random
import pandas as pd


text_data = {}
label_dict = set()
pubmed_dataset = pd.read_csv('../COVID-Dataset/metadata_April10_2020.csv', encoding = "ISO-8859-1")
nlp = spacy.load("en_ner_bc5cdr_md")
nlp = spacy.load("en_ner_bionlp13cg_md")

for index, row in pubmed_dataset.iterrows():
    if index==300: break
    text=str(row['title'])+str(row['abstract'])
    doc=nlp(text)
    text_data[index]=[]
    for ent in doc.ents:
        label_dict.add(ent.label_)
        text_data[index].append([ent.text, ent.start_char, ent.end_char, ent.label_])
    print(index)
# print("TEXT DATA: ", text_data)
print(label_dict)
# -
text = '''Myeloid derived suppressor cells (MDSC) are immature 
          myeloid cells with immunosuppressive activity. 
          They accumulate in tumor-bearing mice and humans 
          with different types of cancer, including hepatocellular 
          carcinoma (HCC).'''
doc = nlp(text)
print("list(doc.sents): ", list(doc.sents))
# -
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
    print('-------')
# -
displacy.render(doc, style="ent")