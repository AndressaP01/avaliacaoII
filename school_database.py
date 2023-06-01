class SchoolDatabase:
    def __init__(self, database):
        self.db = database

    def create_professor(self, name,ano_nasc,cpf):
        query = "CREATE (:Professor {name: $name,ano_nasc:$ano_nasc,cpf:$cpf})"
        parameters = {"name": name,"ano_nasc":ano_nasc,"cpf":cpf}
        self.db.execute_query(query, parameters)

    def create_school(self, name,address,number):
        query = "CREATE (:School {name: $name,address:$address,number:$number})"
        parameters = {"name": name,"address":address,"number":number}
        self.db.execute_query(query, parameters)

    def create_city(self, name,cep,population):
        query = "CREATE (:City {name: $name,cep:$cep,population:$population})"
        parameters = {"name": name,"cep":cep,"population":population}
        self.db.execute_query(query, parameters)

    def create_state(self, name,country):
        query = "CREATE (:State {name: $name,country:$country})"
        parameters = {"name": name,"country":country}
        self.db.execute_query(query, parameters)


    def create_escola_professor_trabalha(self, professor_name,name):
        query = "MATCH (p:Professor {name: $professor_name}) CREATE (:School {name: $name})<-[:WORKS]-(p)"
        parameters = {"professor_name": professor_name,"name": name,}
        self.db.execute_query(query, parameters)

    def create_localidade_da_escola(self, school_name,name):
        query = "MATCH (p:School {name: $school_name}) CREATE (:City {name: $name})<-[:Locates]-(c)"
        parameters = {"school_name": school_name, "name":name}
        self.db.execute_query(query, parameters)

    def create_state_city(self, city_name,name):
        query = "MATCH (p:City {name: $city_name}) CREATE (:State {name: $name})<-[:Belongs]-(st)"
        parameters = {"city_name": city_name, "name":name}
        self.db.execute_query(query, parameters)

    def get_school(self):
        query = "MATCH (p:school) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name","address"] for result in results]

    def get_city(self):
        query = "MATCH (a:city) RETURN a.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_professor(self):
        query = "MATCH (a:Professor)<-[:WORKS]-(p:Professor) RETURN a.name AS name, p.name AS professor_name"
        results = self.db.execute_query(query)
        return [(result["name"], result["professor_name"]) for result in results]

  



