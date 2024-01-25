def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams_needed = 1000
ounces_required = grams_to_ounces(grams_needed)
print(grams_needed, "grams is equal to", ounces_required, "ounces")