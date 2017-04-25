#!/usr/bin/env python
# encoding: utf-8
"""
Concrete poetry is where you replace every word that rhymes with concrete with
concrete, right?

A thing for https://github.com/NaPoGenMo/NaPoGenMo2017
"""
from __future__ import print_function, unicode_literals
import argparse
import re

# from pprint import pprint


# These rhymes found using Pronouncing, with one or two removed:
# >>> import pronouncing  # pip install pronouncing
# >>> pronouncing.rhymes("concrete")
CONCRETE_RHYMES = [
    'amit', 'backseat', 'beat', 'beet', 'breit', 'bridgette',
    'bufete', 'chafete', 'cheat', 'cleat', 'cliett', 'compete', 'complete',
    'conceit', 'crete', 'deceit', 'deet', 'defeat', 'delete', 'deplete',
    'discreet', 'discrete', 'downbeat', 'eat', 'effete', 'elite', 'elite',
    'excrete', 'feat', 'feet', 'fleet', 'freet', 'gamete', 'greet', 'grete',
    'heat', 'incomplete', 'indiscreet', 'jobete', 'keitt', 'kriete', 'lalit',
    'lanete', 'leet', 'leete', 'leite', 'marguerite', 'marquerite', 'meat',
    'meet', 'mete', 'mistreat', 'murveit', 'neat', 'neet', 'non-compete',
    'noncompete', 'obsolete', 'offbeat', 'peat', 'peet', 'peete', 'pete',
    'petite', 'piet', 'piette', 'pleat', 'poteat', 'prete', 'puneet', 'quiett',
    'receipt', 'receipt', 'repeat', 'repeat', 'replete', 'retreat', 'seat',
    'secrete', 'sheet', 'shumeet', 'skeat', 'skeet', 'skeete', 'sleet',
    'street', 'streett', 'suite', 'sweatt', 'sweet', 'swete', 'teat', 'teet',
    'threatt', 'threet', 'thweatt', 'treat', 'tveit', 'tweet', 'uncomplete',
    'unseat', 'vanfleet', 'vanvliet', 'veit', 'vliet', 'wheat', 'wheat']


regex = "(\W+)(" + "|".join(CONCRETE_RHYMES) + ")(\W+)"
CONCRETE_RE = re.compile(regex, re.IGNORECASE)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Concrete poetry is where you replace every word that "
                    "rhymes with concrete with concrete, right?",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "-f", "--filename", default="input/pg1041.txt",
        help="Input filename of poetry")
    args = parser.parse_args()

    with open(args.filename) as f:
        text = f.read().decode("utf-8")

    text = CONCRETE_RE.sub(r"\1CONCRETE\3", text)
    print(text.encode("utf-8"))

# End of file
