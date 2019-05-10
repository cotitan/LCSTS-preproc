# LCSTS-preproc
preprocessing of chinese summarization dataset LCSTS

## dependencies
- xmltodict==0.11.0
- stanfordcorenlp=3.9.1.1

## LCSTS
A text summarization dataset collected from Sina Weibo social media, contains 2.4M news and corresponding title. Contains 3 files in xml format:
- PART_I.txt, for training, around 2.39m instance
- PART_II.txt, for validation, around 10k instance
- PART_III.txt, for test, 1066 instance

Average length of tokenized article and summary.

|Avg. article len|Avg. summary len|
|-|-|
|63.76|10.34|

## usage
- Parse xml file, seprate article and summary into two files.
```
python parser.py PART_I.txt
```
which will generate two files named as PART_I.article and PART_I.summary
- tokenize and replace digits with \'#\'. 
```
python tokenizer.py PART_I.article tokenized/PART_I.article
```
We use stanfordcorenlp to tokenize so it'll take a long while for PART_I.article, about 3-5 hours.
