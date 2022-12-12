import ciw

class NetworkValues:
    def __init__(self):
        self.I = 0.001
        self.Y = 0.0001
        self.R = 10000
        self.S = 1500
        self.A = 30 #entre 10 et 40
        self.C = 707
        self.B = 16
        self.F = 42.2
        self.SR = 1/(self.Y+self.B/self.R)
        self.N = self.network_creation()

    def set_A(self, A):
        self.A = A

    def reset_A(self):
        self.A = 30

    def set_R(self, R):
        self.R = R
        self.reset_SR()

    def reset_R(self):
        self.R = 10000
        self.reset_SR()

    def set_S(self, S):
        self.S = S

    def reset_S(self):
        self.S = 1500

    def set_SR(self, SR):
        self.SR = SR

    def reset_SR(self):
        self.SR = 1/(self.Y+self.B/self.R)

    def reset_network(self):
        self.N = self.network_creation()
        return self.N

    def network_creation(self):

        N = ciw.create_network(

            arrival_distributions=[
                ciw.dists.Exponential(rate=self.A),#SI
                ciw.dists.NoArrivals(),#SR
                ciw.dists.NoArrivals(),#SS
                ciw.dists.NoArrivals()],#SC

            service_distributions=[
                ciw.dists.Deterministic(value=self.I),#SI
                ciw.dists.Exponential(rate=self.SR),#SR
                ciw.dists.Deterministic(value=self.B/self.S),#SS
                ciw.dists.Deterministic(value=self.B/self.C)],#SC

            routing=[
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [0, self.B/self.F, 0, 0]],

            number_of_servers=[1, 1, 1, 1]
        )

        return N
