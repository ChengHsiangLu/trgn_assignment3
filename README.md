# trgn_assignment3

## extract_phonenum.py

### Usage

* python3 extract_phonenum.py mytextfile.txt

### Description

1. Extracts phone numbers from a text file, and prints formatted phone numbers.
2. One-line per phone number formatted as [+][country code] (AreaCode) [local phone number]. [+][country code] optional output if number is international. Create a script called extract_phonenum.py which extracts phone numbers from text file.

### Known Issues
1. Need to understand the basic knowledge of regular expression.
2. Creat a format of regex that can match every phone numbers in an article.

## ensg2hugo.py

### Usage

* python3 ensg2hugo.py [-f][0-9] [file]

### Description

* Key hints. You need to read the Homo_sapiens.GRCh37.75.gtf to create a dictionary, whereby you lookup the Ensembl name and replace it with the HUGO name.

### Known Issues

1. Need to target right places to match IDs.
2. Use the right tool to replace ensembl ID with Hugo ID.

## histogram.py

### Usage

* python3 histogram.py [-f][0-9] [file]

### Description

* Creates a histogram as a png from a file using the specified column in a tab delimited file.

### Known Issues

1. install medplotlib to create a plot.
2. understand how to use medplotlib.
