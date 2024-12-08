class Funcionario:
    def __init__(self, id, nome, cargo, valor_vt, valor_va):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.valor_vt = valor_vt
        self.valor_va = valor_va

    def __repr__(self):
        return f"Funcionario({self.nome}, {self.cargo}, VT: {self.valor_vt}, VA: {self.valor_va})"
