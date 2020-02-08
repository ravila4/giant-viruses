#!/bin/sh

blastp -db $1 -query $2 -outfmt "6 std stitle qcovs" -num_threads 10 -out out.blast

