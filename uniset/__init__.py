from uniset._category import MAINCATEGORIES, SUBCATEGORIES

__all__ = SUBCATEGORIES + MAINCATEGORIES + ("WHITESPACE", "PUNCTUATION")
__version__ = "0.0.0"

import importlib
import string
from typing import FrozenSet


def __getattr__(name: str) -> FrozenSet[str]:
    if name in SUBCATEGORIES:
        return _get_subcategory_set(name)
    if name in MAINCATEGORIES:
        return _get_maincategory_set(name)
    if name == "WHITESPACE":
        return frozenset(string.whitespace) | _get_subcategory_set("Zs")
    if name == "PUNCTUATION":
        return frozenset(string.punctuation) | _get_maincategory_set("P")
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def _get_subcategory_set(subcategory: str) -> FrozenSet[str]:
    subcategory_module = importlib.import_module(
        "._category." + subcategory.lower(), __name__
    )
    return getattr(subcategory_module, subcategory)


def _get_maincategory_set(category: str) -> FrozenSet[str]:
    subcategories = {c for c in SUBCATEGORIES if c.startswith(category)}
    char_set = frozenset()
    for subcategory in subcategories:
        char_set |= _get_subcategory_set(subcategory)
    return char_set
