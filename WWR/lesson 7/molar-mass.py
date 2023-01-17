def make_periodic_table():
    """Create, initialize, and return a dictionary
    that contains all known elements. Each key
    value pair in the dictionary is in this form:
    symbol : [name, symbol, atomic_mass]

    The unit for atomic mass is atomic mass
    units (amu) sometimes abbreviated as u
    """
    table = {
        # [symbol, name, atomic_mass]
        "Ac": ["Actinium", 227],
        "Ag": ["Silver", 107.8682],
        "Al": ["Aluminum", 26.9815386],
        "Am": ["Americium", 243],
and so forth
      "Y": ["Yttrium", 88.90585],
        "Yb": ["Ytterbium", 173.054],
        "Zn": ["Zinc", 65.38],
        "Zr": ["Zirconium", 91.224]
    }
    return table

total_mass = 0

    # For each element in the symbol_quantity_list:
    for sym_quant in symbol_quantity_list:

        # Split the element into symbol and quantity.
        symbol = sym_quant[0]
        quantity = sym_quant[1]

        # Get the atomic mass for the symbol.
        element = periodic_table_dict[symbol]
        atomic_mass = element[ATOMIC_MASS_INDEX]

        # Multiply the atomic mass by the quantity.
        # Add the product into the total mass.
        total_mass += atomic_mass * quantity

    return total_mass
