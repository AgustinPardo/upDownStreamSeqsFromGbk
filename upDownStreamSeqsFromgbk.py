from Bio import SeqIO, SeqFeature

#Input files:
#Genbank file to search the gen positions and extended sequences.
gbk_filename = "/home/agustin/workspace/upDownStreamSeqsFromGbk/karina/Tatroviride_IMI206040_0.gb" # <-Please change->
input_gbk_handle  = open(gbk_filename, "r")

#fasta of query sequences to take de gene id or txt with gene ids in the first colum (columns separated by \t). The first line of the txt(header of file) is avoid.
#Include file name and "fasta" or "txt" type file.
input_file_name_type=["/home/agustin/workspace/upDownStreamSeqsFromGbk/karina/IDcluster10.txt","txt"] # <-Please change->

#Output file:
#Fasta with the original sequences and the extended upstream and downstream sequences. 
fna_filename = "UpDownStream.fna" # <-Please change->
output_handle = open(fna_filename, "w")

#How much to extend.
upstream=1500 # <-Please change->
downstream=0  # <-Please change->

def get_ids_input(file_input, file_type):
        input_handle  = open(file_input, "r")
        if file_type =="fasta":
                sequence_ids=[]
                for record in SeqIO.parse(input_fasta_handle, 'fasta'):
                        sequence_ids.append(record.id)
        if file_type =="txt":
                id_lines=input_handle.readlines()
                sequence_ids=[x.split("\t")[0][:-3] for x in id_lines[1:]]
        input_handle.close()
        return sequence_ids

sequence_ids = get_ids_input(input_file_name_type[0],input_file_name_type[1])

for gb_record in SeqIO.parse(input_gbk_handle, "genbank"):
	for feature in gb_record.features:
		if feature.type == "gene":
			if feature.qualifiers["locus_tag"][0] in sequence_ids:
				# print("original")
				# print(feature.location.start-feature.location.end)
				# print (">", feature.location, gb_record.id, feature.qualifiers["locus_tag"][0])
				# print (feature.location.extract(gb_record).seq)
				output_handle.write(">%s %s %s\n%s\n" % (
					   feature.location,
					   gb_record.id,
					   feature.qualifiers["locus_tag"][0],
					   feature.location.extract(gb_record).seq
					   ))

				new_feature_location = SeqFeature.FeatureLocation(feature.location.start-upstream, feature.location.end+downstream, feature.location.strand)
				# print("Upstream - Downstream extended")
				# print(new_feature_location.start-new_feature_location.end)
				# print (">", new_feature_location, gb_record.id,feature.qualifiers["locus_tag"][0])
				# print (new_feature_location.extract(gb_record).seq)

				output_handle.write(">%s %s %s\n%s\n" % (
					   new_feature_location,
					   gb_record.id,
					   feature.qualifiers["locus_tag"][0],
					   new_feature_location.extract(gb_record).seq
					   ))

input_gbk_handle.close()
output_handle.close()
