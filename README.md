# trgn_assignment3

## extract_phonenum.py

### Usage

* python3 extract_phonenum.py mytextfile.txt

### Description

1. Extracts phone numbers from a text file (ex: mytextfile.txt), and prints foratted phone numbers.
2. One-line per phone number formatted as +(country code) (AreaCode) (local phone number). +(country code) optional output if number is international. Create a script called extract_phonenum.py which extracts phone numbers from text file.

### Known Issues
1. Need to understand the basic knowledge of regular expression.
2. Creat a format of regex that can match every phone numbers in an article.

## ensg2hugo.py

### Usage

* ./ensg2hugo.py > retest.tsv

### Description

1. "wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz".
2. "gunzip Homo_sapiens.GRCh37.75.gtf.gz"
3. "head -200 Homo_sapiens.GRCh37.75.gtf > mini.gtf"
4. read the mini.gtf to create a dictionary.
5. use regular expression to match the column of "gene_id" and "gene_name".
6. Last, I will replace the column of"gene_id" with "gene_name".(ex:gene_id "ENSG00000223972"---> gene_name "DDX11L1")

### Known Issues

1. Need to target right places to match IDs.
2. Use the right tool to replace gene_id with gene_name.

## histogram.py

### Usage

* python3 histogram.py

### Description

* Creates a histogram as a png from a file using in a tab delimited file.

### Known Issues

1. install medplotlib to create a plot.
2. understand how to use medplotlib.
