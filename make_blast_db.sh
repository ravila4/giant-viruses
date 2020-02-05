#!/bin/bash
TYPE=${TYPE:-prot}
[[ ! -z ${1} ]] && INFILE=${1} || exit 1
shift
makeblastdb -in ${INFILE} -dbtype ${TYPE} -parse_seqids ${@} -blastdb_version 5