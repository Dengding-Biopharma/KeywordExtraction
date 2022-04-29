import spacy
import scispacy
nlp = spacy.load("en_ner_bionlp13cg_md")
text = """Lung cancer remains the most common cause of cancer deaths worldwide, yet there is 
currently a lack of diagnostic noninvasive biomarkers that could guide treatment decisions. 
Small molecules (<1500 Da) were measured in urine collected from 469 lung cancer patients and 
536 population controls using unbiased liquid chromatography-mass spectrometry. Clinical 
putative diagnostic and prognostic biomarkers were validated by quantitation and normalized to 
creatinine levels at two different time points and further validated in an independent sample set, 
which comprises 80 cases and 78 population controls, with similar demographic and clinical 
characteristics when compared to the training set. Creatine riboside (IUPAC name: 2-{2-
[(2R,3R,4S,5R)-3,4-dihydroxy-5-(hydroxymethyl)-oxolan-2-yl]-1-
methylcarbamimidamido}acetic acid), a novel molecule identified in this study, and Nacetylneuraminic acid (NANA), were each significantly (P <0.00001) elevated in non–small cell 
lung cancer (NSCLC) and associated with worse prognosis (hazard ratio (HR) =1.81 [P 
=0.0002], and 1.54 [P =0.025], respectively). Creatine riboside was the strongest classifier of 
lung cancer status in all and stage I-II cases, important for early detection, and also associated 
with worse prognosis in stage I-II lung cancer (HR =1.71, P =0.048). All measurements were 
highly reproducible with intraclass correlation coefficients ranging from 0.82 - 0.99. Both 
metabolites were significantly (P <0.03) enriched in tumor tissue compared to adjacent nontumor tissue (N =48), thus revealing their direct association with tumor metabolism. Creatine 
riboside and NANA may be robust urinary clinical metabolomic markers that are elevated in 
tumor tissue and associated with early lung cancer diagnosis and worse prognosis.
"""
doc = nlp(text)
print(doc.ents)
print("TEXT", "START", "END", "ENTITY TYPE")
for ent in doc.ents:
    print(ent.text)
