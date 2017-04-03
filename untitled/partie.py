import grille as g

class Partie(object):
    def __init__(self,taille,saison):
        """

        :param taille: taille de la grille
        :type taille: tuple
        :param saison: saison
        :type saison:string
        :return:
        """
        self.taille=taille
        self.saison=saison
        self.grille=g.Grille(self.taille,self.saison)
        self.grille.remplir_case()


    def get_T_prof(self,case):
        return self.grille.get_T_prof(case)


    def coord_to_case(self,coord):
        return self.grille.coord_to_case(coord)


    def get_pop(self,case,espece):
        return self.grille.get_pop(case, banc)

    def get_pop_tot(self,case):
        self.grille.get_pop_tot(case)


    def repro(self):
         return self.grille.repro()

    def deplacer(self):
         pass

    def peche(self,case):
         pass

