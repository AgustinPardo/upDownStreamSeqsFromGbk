# upDownStreamSeqsFromGbk

## upDownStreamSeqsFromgbk.py
### Input files:
#Genbank file to search the gen positions and extended sequences.
gbk_filename = "/home/agustin/workspace/upDownStreamSeqsFromGbk/karina/Tatroviride_IMI206040_0.gb" # <-Please change->
input_gbk_handle  = open(gbk_filename, "r")

#fasta of query sequences to take de gene id or txt with gene ids in the first colum (columns separated by \t). The first line of the txt(header of file) is avoid.
#Include file name and "fasta" or "txt" type file.
input_file_name_type=["/home/agustin/workspace/upDownStreamSeqsFromGbk/karina/IDcluster10.txt","txt"] # <-Please change->

### Output file:
#Fasta with the original sequences and the extended upstream and downstream sequences. 
fna_filename = "UpDownStream.fna" # <-Please change->

## Extract extended fasta
bash expand_fasta.sh < UpDownStream.fna

## Extract original fasta
bash original_fasta.sh < UpDownStream.fna
