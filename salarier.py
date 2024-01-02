from abc import ABC , abstractmethod
class Employe(ABC):
    nombre_instances = 0

    def __init__(self, nom ="", num_secu = 0, etat_civil ="", adresse =""):
        Employe.nombre_instances += 1
        self._matricule = Employe.nombre_instances
        self._nom = nom
        self._num_secu = num_secu
        self._etat_civil = etat_civil
        self._adresse = adresse
    @property
    def get_matricule(self):
        return self._matricule
    @property
    def get_numsec(self):
        return self._nom
    @property
    def get_etatcivile(self):
        return self._etat_civil
    @property
    def get_adress(self):
        return self._adresse
    
    
    def afficher_informations(self):
        print(f"Matricule: {self._matricule}")
        print(f"Nom: {self._nom}")
        print(f"Numéro de Sécurité Sociale: {self._num_secu}")
        print(f"État Civil: {self._etat_civil}")
        print(f"Adresse: {self._adresse}")

    def __eq__(self, other):
        return isinstance(other, Employe) and self._matricule == other._matricule and self.__salaire == other.__salaire
    
    
    @abstractmethod
    def salairi(self):
        pass


class Patron(Employe):
    def __init__(self, nom , num_secu, etat_civil , adresse , salaire=0 , primerisque=0):
        super().__init__(nom, num_secu, etat_civil, adresse)
        self.__salaire = salaire
        self.__primerisque = primerisque
    @property
    def get_salaire(self):
        return self.__salaire
    @property
    def get_prime_risque(self):
        return self.__primerisque
    
    def set_salaire(self,newsalaire):
        self.__salaire = newsalaire

    def set_primeris(self,newprime):
        self.__primerisque = newprime

    def salairi(self):
        s = self.get_salaire + self.get_prime_risque
        return s




    def afficher_informations(self):
        super().afficher_informations()
        print(f"Salaire: {self.__salaire}")
        print(f"Prime de Risque: {self.__primerisque}")
        print(f"salire total est:{self.salairi()}")


class Vendeur(Employe):
    def __init__(self, nom, num_secu, etat_civil, adresse, salaire, commission=0,superieur=""):
        super().__init__(nom, num_secu, etat_civil, adresse)
        self.__salaire = salaire
        self.__commission = commission
        self.__superieur = superieur

    @property
    def get_salaire(self):
        return self.__salaire
    
    @property
    def get_commission(self):
        return self.__commission
    
    @property
    def get_superieur(self):
        return self.__superieur
    
    
    def set_salaire(self,newsalaire):
        self.__salaire = newsalaire

    def set_primeris(self,newcommission):
        self.__commission = newcommission
     
    def set_superieur(self,newsuperieur) :
        self.__superieur = newsuperieur



    def salairi(self):
        s1 = self.get_commission + self.get_salaire
        return s1
        
    
    def afficher_informations(self):
        super().afficher_informations()
        print(f"Salaire: {self.get_salaire}")
        print(f"Commission: {self.get_commission}")
        print(f"totale de salaire est:{self.salairi()}")
        print(f"le superieur hierique est:{self.get_superieur}")


class Caissiere(Employe):
    def __init__(self, nom, num_secu, etat_civil, adresse, salaire,superieur=""):
        super().__init__(nom, num_secu, etat_civil, adresse)
        self.__salaire = salaire
        self.__superieur = superieur

    @property
    def get_salaire(self):
        return self.__salaire
    @property
    def get_superieur(self):
        return self.__superieur
    
 
    def set_salaire(self,newsalaire):
        self.__salaire = newsalaire

     
    def set_superieur(self,newsuperieur) :
        self.__superieur = newsuperieur

    def afficher_informations(self):
        super().afficher_informations()
        print(f"Salaire: {self.get_salaire}")
        print(f"superieur:{self.get_superieur}")

    def salairi(self):
        pass

patron = Patron("anas",5424,"marier","darhom",5555,200)
vendeur = Vendeur("soulaiman",5522,"marier","darhom",6000,500,"yassine")
caissier =Caissiere("zata",3358,"marier","darhoom",2000,"belhaf")

print(patron.afficher_informations())
print(patron.__eq__(vendeur))

print(vendeur.afficher_informations())
print(vendeur.__eq__(caissier))

print(caissier.afficher_informations())
print(caissier.__eq__(patron))
       



