import case as c
import banc as b


class Grille(object):
    def __init__(self, taille, saison, jour=0):
        self.taille=taille
        self.saison=saison
        self.jour=jour
        self.contenu=[[0 for i in range (taille[0])] for j in range (taille[1])]


    def remplir_case(self):
        for i in range (self.taille[0]):
            for j in range (self.taille[1]):
                coord=(i,j)
                prof=-10
                T_surf=10
                charge=0
                bancs=[b.Banc(100,(i,j),"truite")]
                courant=1
                self.contenu[i][j]=c.Case (coord, prof, T_surf, charge, bancs, courant)


    def coord_to_case(self,coord):
        (i,j)=coord
        return self.contenu[i][j]


    def get_T_prof(self, case):
        return case.get_T_prof


    def get_pop_tot(self,case):
        return case.get_pop_tot



    def get_pop(self, case, banc):
        return case.get_pop

    def repro(self, case):
        case.repro()

    def deplacer(self, case):
        case.deplacer()

    def peche(self, case):
        case.peche()


