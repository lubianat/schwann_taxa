# Finding the taxa in Microscopical Researches


This small repo is dedicated to find the taxa in the book "Microscopical Researches" by Theodor Schwann. The English version of the book was published in 1847 and is available on https://www.biodiversitylibrary.org/bibliography/17276

The  text of the book is pulled with wget:

```
wget -O Microscopical_Researches.txt https://www.biodiversitylibrary.org/pagethumb/56510 
```

Then we will process the OCR with the tool TaxoNERD (https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.13778) available on GitHub at https://github.com/nleguillarme/taxonerd/tree/v1.3.1, based on the popular spaCy NER tool. 

```

The output of TaxoNERD will be a list of taxa found in the book.

The largest model (en_core_eco_biobert) does not run on my computer. I've run the mid sized en_core_eco_md model. 

The output is relatively dirty. The linking to GBIF, taxref or ncbi_taxonomy is not working here, I've opened an issue (https://github.com/nleguillarme/taxonerd/issues/24)

I've decided to clean the output manually. 
Some latin terms were misclassified as taxa, I've removed them.
Also, the text included also "Phytogenesis" by Schleiden, and the terms on it were not considered. 


The OCR from the biodiversity heritage library frequently converts the latin diphtong æ into "se" (e.g. frog's larvse) among other minor mistakes.

The TaxoNERD output also missed a few taxa that I've noticed manually, such as the kingfisher genus 'Alcedo' mentioned on page 47. Counts for "raven", "sparrow" and "Alcedo" were added manually.

Terms like "foetal sheep" and "frog larvae" were converted to "sheep" and "frog". 