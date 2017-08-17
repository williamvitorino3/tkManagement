from datetime import datetime

def formata_data(data):
    """Formata a data no formato dd/mm/yyy"""
    return "{0:02d}/{1:02d}/{2:04d}".format(*[int(i) for i in data.split('/')])


class Cliente(object):
    def __init__(self, id, nome, last_atendimento, nascimento, tipo_atendimento):
        self.id = id
        self.ultimo_atendimento = formata_data(last_atendimento)
        self.nome = nome
        self.data_nascimento = formata_data(nascimento)
        self.tipo_atendimento = tipo_atendimento

    @property
    def atendido_ha(self):
        tempo = datetime.now() - datetime(*[int(i) for i in self.ultimo_atendimento.split('/')[::-1]])
        return "%d dia%s" %(tempo.days, "" if tempo.days == 1 else "s")

    def get(self):
        return {
            "id": self.id,
            "Nome": self.nome,
            "Último Atendimento": self.ultimo_atendimento,
            "Data Nascimento": self.data_nascimento,
            "Tipo de Atendimento": self.tipo_atendimento,
            "Atendido há": self.atendido_ha
            }
