############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name 
        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        if isinstance(pairing, str):
            self.pairings.append(pairing) 
        
        if isinstance(pairing, list):
            self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code 

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk', 1998, 'green', True, True, 'muskmelon')
    muskmelon.add_pairing('mint')

    casaba = MelonType('cas', 2003, 'orange', False, False, 'casaba')
    casaba.add_pairing(['strawberries', 'mint'])

    crenshaw = MelonType('cren', 1996, 'green', False, False, 'crenshaw')
    crenshaw.add_pairing('proscuitto')

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, 'yellow watermelon')
    yellow_watermelon.add_pairing('ice cream')

    all_melon_types.extend([muskmelon, casaba, crenshaw, yellow_watermelon])
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name.capitalize()} pairs with")
        for item in melon.pairings:
            print(f"    -{item}")
        print('\n')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dictionary = {}
    for melon in melon_types: 
        melon_dictionary[melon.code] = melon
    
    return melon_dictionary

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    
    def __init__(self, 
                 melon_type, 
                 shape_rating, 
                 color_rating, 
                 origin_field, 
                 harvester):
        
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.origin_field = origin_field
        self.harvester = harvester

    def is_sellable(self): 
        if (self.color_rating > 5) and (self.shape_rating > 5) and (self.origin_field != 3): 
            return True
        else: 
            return False 


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    
    melons_by_id = make_melon_type_lookup(make_melon_types())
    
    melons_list = []

    melon1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    melons_list.extend([melon1, 
                        melon2, 
                        melon3, 
                        melon4, 
                        melon5, 
                        melon6, 
                        melon7, 
                        melon8, 
                        melon9])

    return melons_list


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons: 
        if melon.is_sellable() == True:
            sellable = 'CAN BE SOLD'
        else: 
            sellable = 'NOT SELLABLE'

        print(f"Harvested by {melon.harvester} from Field {melon.origin_field} ({sellable})")



# for testing in terminal 
get_sellability_report(make_melons(make_melon_types()))