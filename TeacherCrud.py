class TeacherCrud:
    def __init__(self, database):
        self.db = database

    def create_professor(self, name,ano_nasc,cpf):
        query = "CREATE (:Professor {name: $name,ano_nasc:$ano_nasc,cpf:$cpf})"
        parameters = {"name": name,"ano_nasc":ano_nasc,"cpf":cpf}
        self.db.execute_query(query, parameters)

    def update_professor(self, old_cpf, new_cpf):
        query = "MATCH (p:Professor {name: $old_cpf}) SET p.cpf = $new_cpf"
        parameters = {"old_cpf": old_cpf, "new_cpf": new_cpf}
        self.db.execute_query(query, parameters)

    def delete_professor(self, name):
        query = "MATCH (p:Professor {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def read_professor(self):
        query = "MATCH (p:Professor) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]