import spacy
import scispacy
nlp = spacy.load("en_core_sci_scibert")
text = """Asthma, allergic rhinitis, food allergy, and atopic dermatitis are common childhood diseases
with several different underlying mechanisms, i.e., endotypes of disease. Metabolomics has the
potential to identify disease endotypes, which could beneficially promote personalized prevention
and treatment. Here, we summarize the findings from metabolomics studies of children with
atopic diseases focusing on tyrosine and tryptophan metabolism, lipids (particularly, sphingolipids),
polyunsaturated fatty acids, microbially derived metabolites (particularly, short-chain fatty acids),
and bile acids. We included 25 studies: 23 examined asthma or wheezing, five examined allergy
endpoints, and two focused on atopic dermatitis. Of the 25 studies, 20 reported findings in the pathways
of interest with findings for asthma in all pathways and for allergy and atopic dermatitis in most
pathways except tyrosine metabolism and short-chain fatty acids, respectively. Particularly, tyrosine,
3-hydroxyphenylacetic acid, N-acetyltyrosine, tryptophan, indolelactic acid, 5-hydroxyindoleacetic
acid, p-Cresol sulfate, taurocholic acid, taurochenodeoxycholic acid, glycohyocholic acid, glycocholic
acid, and docosapentaenoate n-6 were identified in at least two studies. This pathway-specific review
provides a comprehensive overview of the existing evidence from metabolomics studies of childhood
atopic diseases. The altered metabolic pathways uncover some of the underlying biochemical
mechanisms leading to these common childhood disorders, which may become of potential value in
clinical practice."""
doc = nlp(text)
print(doc.ents)
