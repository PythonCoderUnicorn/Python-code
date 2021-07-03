
#-----------------
#  STAR TREK ALIENS
# BY: ZANE DAX
# DATE: JULY 3 2021
# ----------------


DELTA = ["Akritirian - 2373", "Aksani - 2377", "Ankari -2376", "Annari - 2374", "Antarian - 2377", "Arrithean", "Augris", "B'omar", "Ba'Neth", "Banea", "Benkaran", "Benthans", "Boray", "Borg", "Botha", "Brenari", "Briori", "Brunali", "Caatati", "Chokuzan", "Chessu", "Dala", "Devore", "Dinaali", "Dralian", "Drayan", "Dream Species", "Druoda", "Enaran", "Entabans", "Entharan", "Etanian", "Farn", "Fantome", "Garan", "Garenor", "Haakonian", "Hanonian", "Hazari", "Hirogen", "IIari", "IIidarian", "Imhotep", "Jye", "Kadi", "Kazon", "Kesat", "Kinbori", "Kmada", "Kobali", "Kolaati", "Kolhari", "Komar", "Kradin", "Kraylor", "Krenim", "Kyrian", "Ledosian", "Lokirrim", "MaKull", "Malkoth", "Malon", "Mari", "Mawasi", "Mikhal Travelers", "Mislenite", "Monean", "Morphinians", "Mylean", "N'Kree", "Nacene", "Nasari", "Nassordin", "Nechani", "Nezu", "Night Aliens", "Nihydron", "Norcadian", "Numiri", "Nuu'Bari", "Nygean", "Nyrian", "Ocampa", "Otrin", "Ovion", "Overlookers,", "Parein", "Pendari,", "Pensarkan", "Photonic lifeform", "Ponea", "Pralor", "Qomar", "Quarren", "Rakosan", "Ram Izad", "Ramuran", "Rilnar", "Sakari", "Serosian", "Shivolian", "Sikarian,", "Silver Blood", "Sky Spirit", "Species 116", "Species 125", "Species 149", "Species 259", "Species 262", "Species 263", "Species 312", "Species 571", "Species 5174", "Species 5973", "Species 6339", "Species 8472", "Srivani", "Swarm species", "Tak Tak", "Takarian," "Talax", "Taresian", "Tarkan", "Telsian", "Terkellian", "Terrellian", "Trabe", "Turei", "Vaadwaur", "Varro", "Vaskan", "Ventu", "Vhnori", "Vidiian", "Viorsa", "Vok'sha", "Vori", "Vostigye", "Voth", "Wyngari", "Wysanti", "Yallitian", "Zahl"]

ALPHA_BETA = ["Alcyone", "Aldean", "Algolian", "Antaran", "Antican", "Barzans", "Breen", "Enolian", "Ferengi", "Metrons", "Miradorn", "Na'Kuhl", "Nausicaans", "Triannons", "Tholian", "Saurian", "Sphere-Builders", "Rigellian", "Romulan", "Xindi"]

import numpy as np

x = np.random.randint(1, (len(DELTA) - 1))
z = np.random.randint(1, (len(ALPHA_BETA) - 1))

# print(x)

print("\n ---------------------------------")
print(f" Aliens to Dominate next (Delta): {DELTA[x]}")
print(f" Aliens to Dominate (Alpha/Beta): {ALPHA_BETA[z]}")
print("---------------------------------\n")