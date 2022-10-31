from CSV.CSVHandler import *
from Settings import TEAMS_PATH

# Define a classe Team para facilitar a utilização no código
class Team:
    def __init__(self, id, group_id, name):
        self.id = id
        self.group_id = group_id
        self.name = name
    def __str__(self):
        return f'Team[id: {self.id}, group_id: {self.group_id}, name: {self.name}]'


# Converte dicionario em rating
def to_team(team_dict):
    return Team(
        int(team_dict['id']),
        int(team_dict['group_id']),
        team_dict['name']
    )

# Cria e armazena um novo Time com o nome fornecido
def create_team (name:str, group:int):
    return add_unique_csv_autoid(TEAMS_PATH, [group, name])

# Verifica se um Time com o id forneido existe armazenado no banco de dados
def exists_team (id:int):
    if id is None:
        return True
    return find_data_by_id_csv(TEAMS_PATH, id) is not None 

# retorna o Time que corresponde ao id especificado 
def get_team (id:int):
    return to_team(find_data_by_id_csv(TEAMS_PATH, int(id)))



