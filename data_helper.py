from pathlib import Path
import csv

LEGISLATORS_DATA_PATH = Path('./static', 'legislators.csv')



def get_legislators():
    """
    return all legislators (a list of dicts)
    """

    txt = LEGISLATORS_DATA_PATH.read_text()
    lines = txt.splitlines()
    rows = list(csv.DictReader(lines))
    return rows



def get_chamber(chamber):
    """
    Easy-to-call wrapper around filter_by_chamber
    """
    return filter_by_chamber(chamber)


def filter_by_chamber(chamber):
    """
    chamber <str>:
        This is either 'senate' or 'house'

    In the unitedstates/congress-legislators datafile, they use
    a non-helpfully named field of "type" to distinguish between
    Senate and House, e.g. 'sen' and 'rep'

    This function is a light wrapper that provides something a
    little more human sensible for input -- the name of the
    legislative chamber
    """

    thetype = ''
    if chamber.lower() == 'house':
        thetype = 'rep'
    elif chamber.lower() == 'senate':
        thetype = 'sen'

    fdata = []
    for r in get_legislators():
        if r['type'] == thetype:
            fdata.append(r)
    return fdata



