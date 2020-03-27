from Bio import SeqIO

fasta_filename="secuencia_nucleotidos.fasta"
gbk_filename = "st5.gbk"
fna_filename = "300UpDownStream.fna"

input_fasta_handle  = open(fasta_filename, "r")
input_gbk_handle  = open(gbk_filename, "r")
output_handle = open(fna_filename, "w")

sequence_ids=[]
for record in SeqIO.parse(input_fasta_handle, 'fasta'):
	sequence_ids.append(record.id)

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

				new_feature_location = SeqFeature.FeatureLocation(feature.location.start-300, feature.location.end+300, feature.location.strand)
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

input_fasta_handle.close()
input_gbk_handle.close()
output_handle.close()
