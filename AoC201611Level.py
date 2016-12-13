def isGenerator(obj):
    return obj[-1] == 'G'

def matchWith(chipOrGenerator):
    return chipOrGenerator[0] + 'M' if isGenerator(chipOrGenerator) else 'G'

class Level:
    def __init__(self, number, contents=[]):
        self.number = number
        self.contents = contents

    def generators(self):
        return sorted([obj for obj in self.contents if isGenerator(obj)])

    def microchips(self):
        return sorted([obj for obj in self.contents if not isGenerator(obj)])

    def pairs(self):
        return [(generator, matchWith(generator))
                for generator in self.generators()
                if matchWith(generator) in self.microchips()]

    def pairedMicrochips(self):
        return [pair[1] for pair in self.pairs()]

    def pairedGenerators(self):
        return [pair[0] for pair in self.pairs()]

    def unpairedMicrochips(self):
        return [chip for chip in self.microchips() if matchWith(chip) not in self.contents]

    def unpairedGenerators(self):
        return [generator for generator in self.generators() if matchWith(generator) not in self.contents]

    def isSafe(self):
        return not (self.unpairedMicrochips() and self.generators())

    def generatorsThatCanLeave(self):
        return [g for g in self.generators() if self.safeToLeave(g)]

    def safeToLeave(self, chipOrGenerator):
        return isGenerator(chipOrGenerator) and matchWith(chipOrGenerator) not in self.contents

    def fullContents(self):
        return "Level {0}: pairs {1}, generators {2}, microchips {3}, pairedchips, {4}, pairedgenerators {5}, unpairedchips {6}, unpairedgenerators {7}".format(
            self.number, self.pairs(), self.generators(), self.microchips(), self.pairedMicrochips(), self.pairedGenerators(), self.unpairedMicrochips(), self.unpairedGenerators())

    def __str__(self):
        return "Level {0}: {1}".format(self.number, self.contents)