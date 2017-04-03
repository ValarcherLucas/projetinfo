import partie as p

class Joueur(object):
    def __init__(self, humain):
        self.humain=humain

    def creer_partie(self,taille,saison):
        self.partie=p.Partie(taille,saison)


    def coord_to_case(self,coord):
        return self.partie.coord_to_case(coord)

    def get_T_prof(self, coord):
        case=self.coord_to_case(coord)
        print(self.partie.get_T_prof(case))
        return self.partie.get_T_prof(case)

    def get_pop(self, coord, banc):
        case=self.coord_to_case(coord)
        return self.partie.get_pop(case)

    def get_pop_tot(self,coord):
        case=self.coord_to_case(coord)
        print(self.partie.get_pop_tot(case))
        return self.partie.get_pop_tot(case)


    def peche(self, coord):
        case=self.coord_to_case(coord)
        return self.partie.peche(case)



if __name__ == "__main__":
    joueur=Joueur("humain")
    joueur.creer_partie((2,2),"ete")
    joueur.get_T_prof((1,1))
    joueur.get_pop_tot((1,1))

