{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "02c397fe-fb6e-4719-920c-454bbf373ba7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--2021-10-14 20:35:49--  http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz\n",
      "Resolving ftp.ensembl.org (ftp.ensembl.org)... 193.62.197.76\n",
      "Connecting to ftp.ensembl.org (ftp.ensembl.org)|193.62.197.76|:80... connected.\n",
      "HTTP request sent, awaiting response... 200 OK\n",
      "Length: 39344043 (38M) [application/x-gzip]\n",
      "Saving to: ‘Homo_sapiens.GRCh37.75.gtf.gz’\n",
      "\n",
      "Homo_sapiens.GRCh37 100%[===================>]  37.52M   655KB/s    in 62s     \n",
      "\n",
      "2021-10-14 20:36:52 (620 KB/s) - ‘Homo_sapiens.GRCh37.75.gtf.gz’ saved [39344043/39344043]\n",
      "\n"
     ]
    }
   ],
   "source": [
    "!wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "bc641381-9f6c-4493-9145-54ea32583e26",
   "metadata": {},
   "outputs": [],
   "source": [
    "!gunzip Homo_sapiens.GRCh37.75.gtf.gz"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "cbce4b6a-fa22-43ef-b374-0d77b8fc3a3b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "#!genome-build GRCh37.p13\n",
      "#!genome-version GRCh37\n",
      "#!genome-date 2009-02\n",
      "#!genome-build-accession NCBI:GCA_000001405.14\n",
      "#!genebuild-last-updated 2013-09\n",
      "1\tpseudogene\tgene\t11869\t14412\t.\t+\t.\tgene_id \"ENSG00000223972\"; gene_name \"DDX11L1\"; gene_source \"ensembl_havana\"; gene_biotype \"pseudogene\";\n",
      "1\tprocessed_transcript\ttranscript\t11869\t14409\t.\t+\t.\tgene_id \"ENSG00000223972\"; transcript_id \"ENST00000456328\"; gene_name \"DDX11L1\"; gene_source \"ensembl_havana\"; gene_biotype \"pseudogene\"; transcript_name \"DDX11L1-002\"; transcript_source \"havana\";\n",
      "1\tprocessed_transcript\texon\t11869\t12227\t.\t+\t.\tgene_id \"ENSG00000223972\"; transcript_id \"ENST00000456328\"; exon_number \"1\"; gene_name \"DDX11L1\"; gene_source \"ensembl_havana\"; gene_biotype \"pseudogene\"; transcript_name \"DDX11L1-002\"; transcript_source \"havana\"; exon_id \"ENSE00002234944\";\n",
      "1\tprocessed_transcript\texon\t12613\t12721\t.\t+\t.\tgene_id \"ENSG00000223972\"; transcript_id \"ENST00000456328\"; exon_number \"2\"; gene_name \"DDX11L1\"; gene_source \"ensembl_havana\"; gene_biotype \"pseudogene\"; transcript_name \"DDX11L1-002\"; transcript_source \"havana\"; exon_id \"ENSE00003582793\";\n",
      "1\tprocessed_transcript\texon\t13221\t14409\t.\t+\t.\tgene_id \"ENSG00000223972\"; transcript_id \"ENST00000456328\"; exon_number \"3\"; gene_name \"DDX11L1\"; gene_source \"ensembl_havana\"; gene_biotype \"pseudogene\"; transcript_name \"DDX11L1-002\"; transcript_source \"havana\"; exon_id \"ENSE00002312635\";\n"
     ]
    }
   ],
   "source": [
    "!head Homo_sapiens.GRCh37.75.gtf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "009a0445-9ab4-4df9-a6e5-865d9a0d66d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "!head -300 Homo_sapiens.GRCh37.75.gtf > mini.gtf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "89958296-525b-4c06-ae25-03b08788c145",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--2021-10-14 20:37:24--  https://raw.githubusercontent.com/davcraig75/unit/master/expres.anal.csv\n",
      "Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.109.133, 185.199.110.133, 185.199.111.133, ...\n",
      "Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.109.133|:443... connected.\n",
      "HTTP request sent, awaiting response... 200 OK\n",
      "Length: 1535008 (1.5M) [text/plain]\n",
      "Saving to: ‘expres.anal.csv.1’\n",
      "\n",
      "expres.anal.csv.1   100%[===================>]   1.46M  --.-KB/s    in 0.05s   \n",
      "\n",
      "2021-10-14 20:37:25 (27.7 MB/s) - ‘expres.anal.csv.1’ saved [1535008/1535008]\n",
      "\n"
     ]
    }
   ],
   "source": [
    "!wget https://raw.githubusercontent.com/davcraig75/unit/master/expres.anal.csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "fc1c129b-c544-4ace-8b6c-bdd312b593d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Overwriting BBB.py\n"
     ]
    }
   ],
   "source": [
    "%%file BBB.py\n",
    "import sys\n",
    "import fileinput\n",
    "import re\n",
    "\n",
    "\n",
    "if sys.argv[1][0:2] == \"-f\":\n",
    "    column_number = int(re.findall(r'\\d+',sys.argv[1])[0])\n",
    "    f_opt=1\n",
    "else:\n",
    "    column_number = 2\n",
    "    f_opt=0\n",
    "\n",
    "    \n",
    "creat_dict= sys.argv[1+f_opt]\n",
    "idname_Hugo={}\n",
    "for line in fileinput.input(creat_dict):\n",
    "#     print(line)\n",
    "    g_id = re.findall('gene_id \\\"(.*?)\"',line, re.I)\n",
    "    g_name = re.findall('gene_name \\\"(.*?)\"',line, re.I)\n",
    "    if g_id:\n",
    "        if g_name:\n",
    "            idname_Hugo[g_id[0]] = g_name[0]\n",
    "#             print(g_id[0] +\":\"+ g_name[0])\n",
    "#             print(idname_Hugo)\n",
    "sample = open('final_Hugo.csv', 'w')\n",
    "# print(idname_Hugo)\n",
    "unit_change=sys.argv[2+f_opt]\n",
    "for line in fileinput.input(unit_change):\n",
    "    org_data = re.sub(r\"(ENSG\\d+)\\.\\d*\", r\"\\1\", line)\n",
    "    org_data = re.split(',',org_data.replace( '\"' ,'').replace('\\n',''))\n",
    "#     print(org_data)\n",
    "    if org_data[0] == '': \n",
    "        turn_into_str = str(org_data)[1:-1]\n",
    "        final_text = turn_into_str.replace(\"\\'\", \"\")\n",
    "        print(final_text, file = sample)\n",
    "        continue\n",
    "    if org_data[1] in idname_Hugo:\n",
    "#         print(\"*\")\n",
    "#         print(idname_Hugo[org_data[1]])\n",
    "        org_data[column_number-1] = idname_Hugo[org_data[1]]\n",
    "#         print(org_data)\n",
    "\n",
    "\n",
    "        turn_into_str = str(org_data)[1:-1]\n",
    "        final_text = turn_into_str.replace(\"\\'\", \"\")\n",
    "        print(final_text, file = sample)\n",
    "sample.close()   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "eb0722f7-08d2-42cd-b601-187ca202ec96",
   "metadata": {},
   "outputs": [],
   "source": [
    "!python BBB.py -f4 mini.gtf expres.anal.csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "1ada4e12-ca5e-45c4-9dd1-0232302281d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import sys\n",
    "# import re\n",
    "# import fileinput\n",
    "\n",
    "# ens2gene={}\n",
    "# with open (\"mini.gtf\",'r') as file:\n",
    "#     for line in file:\n",
    "#         matches = re.findall('.*gene_id \"(.*?)\".*gene_name \"(.*?)\";',line)\n",
    "#         if matches:\n",
    "#             line = re.sub(matches[0][0],matches[0][1],line)\n",
    "#             print(line)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d0b4f2f-bdaf-418d-8ca4-4159ca8f66a9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
