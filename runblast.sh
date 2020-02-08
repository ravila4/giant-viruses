#!/bin/sh

blastp -db $1 -query $2 -outfmt "6 std stitle qcovs" -num_threads 4 -out out.blast

