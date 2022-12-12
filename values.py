class Values:
    def __init__(self):
        self.average_waits_dict = {}
        self.average_waits = []
        self.simtime = 10 ## pour que ça soit pas trop long non plus
        self.nbexecs = 100 ## valeur optimale trouvée avec la tache 2
        self.prct = 5 ## Pourcentage de confiance
        self.tabA = []
        self.tabS = []
        self.sojourn_time = 0

    def reset_sojourn(self):
        self.tabS = []
