# Creo una nuova classe Rifugio
class Rifugio:
    def __init__(self, id, nome, localita):
        self.id = id
        self.nome = nome
        self.localita = localita

    def __str__(self):
        return f"{self.nome} ({self.localita})"

    def __repr__(self):
        return self.__str__()

    # Rendo l'oggetto hashable perchè serve per il grafo
    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        # Dico che due rifugi devono essere considerati uguali se hanno lo stesso id
        return isinstance(other, Rifugio) and self.id == other.id