import spacy
import scispacy
nlp = spacy.load("en_core_sci_scibert")
print(nlp)
quit()
text = """Myeloid derived suppressor cells (MDSC) are immature 
myeloid cells with immunosuppressive activity. 
They accumulate in tumor-bearing mice and humans 
with different types of cancer, including hepatocellular 
carcinoma (HCC)."""
doc = nlp(text)
print(doc.ents)