"""A script to autogenerate uniset._category package."""
import collections
from pathlib import Path
import sys
import unicodedata

unicode_chars = frozenset(chr(c) for c in range(sys.maxunicode + 1))

# Group Unicode characters by category
skip_subcategories = {"Co", "Cn"}  # Skip "private use" and "not assigned" categories
skip_maincategories = {"C"}  # Skip "Other" category
by_category = collections.defaultdict(list)
for c in unicode_chars:
    category = unicodedata.category(c)
    if category not in skip_subcategories:
        by_category[category].append(c)

# Make main categories (initial letter only)
main_categories = {
    sub_category[0]
    for sub_category in by_category
    if sub_category[0] not in skip_maincategories
}

# Create a separate Python module for each category
for category, chars in by_category.items():
    module_text = f"{category} = frozenset({tuple(chars)!r})\n"
    module_path = Path(f"uniset/_category/{category.lower()}.py")
    module_path.write_text(module_text)

# Write uniset._category.__init__.py
init_text = f'''\
"""A package containing category-based sets of Unicode code points.

THIS PACKAGE IS AUTO-GENERATED. DO NOT EDIT!
"""

SUBCATEGORIES = {tuple(by_category)!r}
MAINCATEGORIES = {tuple(main_categories)!r}
'''
Path("uniset/_category/__init__.py").write_text(init_text)
