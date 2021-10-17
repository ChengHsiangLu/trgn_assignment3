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

* python3 new_ensg2hugo.py -f2 Homo_sapiens.GRCh37.75.gtf expres.anal.csv

### Description

1. "wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz".
2. "gunzip Homo_sapiens.GRCh37.75.gtf.gz"
3. read the file of Homo_sapiens.GRCh37.75.gtf and create a dictionary of "gene_id" and "gene_name" by using regex.
4. "wget https://raw.githubusercontent.com/davcraig75/unit/master/expres.anal.csv"
5. use the dixtionary to change the second column of "expres.anal.csv" file into "gene_name" by using regex.(ex:gene_id "ENSG00000223972"---> gene_name "DDX11L1")
6. Last, the new file of final_Hugo.csv will be created.

### Known Issues

1. Need to target right places to match IDs.
2. Use the right tool to replace gene_id with gene_name.

## histogram.py

### Usage

* python3 HIS.py -f4 expres.anal.csv

### Description

* Creates a histogram as a png(ex:final_HIS.png) from "expres.anal.csv" by choosing the column with integers or floats.(ex:-f4,-f5)

### Known Issues

1. install medplotlib to create a plot.
2. change string valves into integers or floats.
