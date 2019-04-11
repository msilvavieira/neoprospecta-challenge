# neoprospecta-challenge
My attempt at the backend challenge for Neoprospecta!

To populate the database:

  1. make activate a virtualenv
  2. pip install -r requirements.txt
  3. ./manage.py getfasta


The app will download a compacted (gz) FASTA archive from https://www.arb-silva.de/fileadmin/silva_databases/release_128/Exports/SILVA_128_LSURef_tax_silva.fasta.gz, unpack it, then parse the data
and populate the database (sqlite).

Enjoy!
