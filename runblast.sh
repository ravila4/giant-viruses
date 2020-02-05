blastp -db fasta.fa -query database.fa \
    -outfmt "6 std stitle qcovs" -num_threads 10 -out out.blast