# upDownStreamSeqsFromGbk

### Set requirements

```python
pip install -r requirements.txt
```

## upDownStreamSeqsFromgbk.py
### Input files:
Genbank file to search the gene positions and extended sequences.

```python
gbk_filename = "/home/agustin/Tatroviride_IMI206040_0.gb" # <-Please change->
```
Fasta of query sequences to take de gene id or txt with gene ids in the first colum (columns separated by \t). The first line of the txt(header of file) is avoid.
Include file name and "fasta" or "txt" file type:

```python
input_file_name_type=["/home/agustin/IDcluster10.txt","txt"] # <-Please change->
```
### Output file:
The output is a fasta file format with the original sequences and the extended upstream and downstream sequences. Set the name of the output file:

```python
fna_filename = "UpDownStream.fna" # <-Please change->
```

### How much to extend.
Select how much base pairs extend to upstream or downastream side from the original genes start and end:

```python
upstream=1500 # <-Please change->
downstream=0  # <-Please change->
```

### Run.

```python
python3 upDownStreamSeqsFromgbk.py
```

## Extract extended fasta
bash expand_fasta.sh < UpDownStream.fna

## Extract original fasta
bash original_fasta.sh < UpDownStream.fna

## Extract extended region from upstream
awk '{if (/^>/) print $0; else print(substr($1,1,1500)) }' extended.fasta 

## Extract extended region from downstream
awk '{if (/^>/) print $0; else print(substr($1, length($1)-1500, length($1))) }' extended.fasta 

