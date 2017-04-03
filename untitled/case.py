class Case(object):
    def __init__(self, coord, prof, T_surf, charge, bancs, courant):
        self.coord=coord
        self.prof=prof
        self.T_surf=T_surf
        self.charge=charge
        self.bancs=bancs
        self.courant=courant
        pop=0
        for i in bancs:
            pop+=i.get_pop

        self.pop=pop




    @property
    def get_T_prof(self):

        return self.T_surf, self.prof


    @property
    def get_pop(self, Banc):
        return self.Banc.get_pop

    @property
    def get_pop_tot(self):
        return self.pop




    def deplacer(self, Banc):
        pass

    def repro(self, Banc):
        pass

    def peche(self, Banc):
        pass




