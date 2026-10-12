"""Utilitare mici, sigure pentru pandas 3 (coloane text Arrow) si tabele goale."""
import pandas as pd


def lookup(keys, table):
    """Echivalent 'left join' pe index: pentru fiecare cheie din `keys` intoarce randul din `table` (NaN daca lipseste).
    Nu foloseste merge/join, care pica pe tabele goale cu tipuri Arrow diferite. Rezultatul are aceeasi lungime ca `keys`."""
    t = table.copy()
    t.index = t.index.astype(object)
    return t.reindex(pd.Index(pd.Series(keys).astype(object)))
