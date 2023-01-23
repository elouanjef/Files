class Values:
    def __init__(self):
        self.average_waits_dict = {} ## Temps moyen de séjour
        self.average_waits = []
        self.arrivee = 10 ## A
        self.nbexecs = 100 ## valeur optimale trouvée avec la tache 2
        self.prct = 5 ## Pourcentage de confiance
        self.tabA = [] ## Stockage des valeurs de A
        self.tabS = [] ## Stockage du tableau des temps de séjour
        self.mean_sojourn_time = [] ## Moyenne temps de séjour
        self.conf_high = [] ## Stockage des valeurs de l'intervalle
        self.conf_low = []
        self.estim_ponc = [] ## Stockage de l'estimation ponctuelle
        self.sojourn_time = 0 ## Temps de séjour

    def reset_sojourn(self):
        self.tabS = []
