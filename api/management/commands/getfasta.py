import gzip
import requests
from django.core.management.base import BaseCommand
from api.models import Entry, Kingdom, Species


class Command(BaseCommand):
    help = "GET the specified fasta archive, defaults to default_fasta"

    def handle(self, *args, **options):
        data = requests.get('https://www.arb-silva.de/fileadmin/silva_databases/release_128/Exports/SILVA_128_LSURef_tax_silva.fasta.gz')
        fasta = gzip.decompress(data.content).decode()
        entries = fasta.split('>')[1:5001]

        _labels_ = set()

        for e in entries:
            fasta_parser = FastaParser(e)

            sequence = fasta_parser.sequence
            access_id = fasta_parser.access_id
            kingdom_label = fasta_parser.kingdom
            species_label = fasta_parser.species

            if not kingdom_label in _labels_:
                _labels_.add(kingdom_label)
                kingdom = Kingdom(label=kingdom_label)
                kingdom.save()
            else:
                kingdom = Kingdom.objects.get(label=kingdom_label)

            if not species_label in _labels_:
                _labels_.add(species_label)
                species = Species(label=species_label)
                species.save()
            else:
                species = Species.objects.get(label=species_label)

            e = Entry(access_id=access_id, kingdom=kingdom, species=species, sequence=sequence)
            e.save()



class FastaParser():
    def __init__(self, entry):
        self.entry = entry.split('\n')

        classification_data = self.entry[0].split(';')
        id_and_kingdom = classification_data[0].split(' ')

        self.access_id = id_and_kingdom[0]
        self.kingdom = id_and_kingdom[1]
        self.species = classification_data[-1]
        self.sequence = self.entry[1]

