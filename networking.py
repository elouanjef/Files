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
        self.N = self.network_creation(self.A)

    def set_A(self, A):
        self.A = A
        return A

    def reset_network(self):
        self.N = self.network_creation(self.A)
        return self.N

    def network_creation(self, A):

        N = ciw.create_network(

            arrival_distributions=[
                ciw.dists.Exponential(rate=self.A),#SI
                ciw.dists.NoArrivals(),#SR
                ciw.dists.NoArrivals(),#SS
                ciw.dists.NoArrivals()],#SC

            service_distributions=[
                ciw.dists.Deterministic(value=self.I),#SI
                ciw.dists.Exponential(rate=1/(self.Y+self.B/self.R)),#SR
                ciw.dists.Deterministic(value=self.B/self.S),#SS
                ciw.dists.Deterministic(value=self.B/self.C)],#SC

            routing=[
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [0, self.B/self.F, 0, 0]],

            number_of_servers=[1, 1, 1, 1]
        )

        self.N = N
        return N
