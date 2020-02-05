#!/usr/bin/env python

import pandas as pd
import click
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


@click.command()
@click.version_option(version='0.0.2')
@click.argument('csvfile', nargs=1)
@click.argument('idcol', nargs=1)
@click.argument('seqcol', nargs=1)
@click.option('--fafile', '-f', default='sequences.fa')
@click.option('--descol', '-d', multiple=True)
def csv_to_fasta(csvfile, idcol, seqcol,
                 fafile='sequences.fa', descol=()):
    df = pd.read_csv(csvfile)
    df.dropna(subset=[seqcol, idcol], inplace=True)
    if not all(descol):
        records = [SeqRecord(Seq(str(row[seqcol])), id=row[idcol]) for id,
                   row in df.iterrows()]
    else:
        descol = list(descol)
        records = []
        for id, row in df.iterrows():
            desstr = []
            for idr, r in row[descol].to_dict().items():
                desstr.append("{}={}".format(idr, r))
            records.append(SeqRecord(Seq(str(row[seqcol])), id=row[idcol],
                           description=" ".join(desstr)))
    SeqIO.write(records, fafile, 'fasta')


if __name__ == "__main__":
    csv_to_fasta()
