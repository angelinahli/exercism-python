""" 
Set of allergens and their values:
* eggs (1)
* peanuts (2)
* shellfish (4)
* strawberries (8)
* tomatoes (16)
* chocolate (32)
* pollen (64)
* cats (128)
"""

class Allergies(object):

    scores = {'eggs': 1, 
              'peanuts': 2, 
              'shellfish': 4,
              'strawberries': 8,
              'tomatoes': 16,
              'chocolate': 32,
              'pollen': 64,
              'cats': 128}

    def __init__(self, score):
        self.score = score
        self.lst = [a for a, s in self.scores.items() if s & score]

    def is_allergic_to(self, allergen):
        return allergen in self.lst

if __name__ == "__main__":
    # Testing area
    print Allergies(3).lst
    # print Allergies(257).lst