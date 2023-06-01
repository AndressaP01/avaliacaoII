import select
from neo4j.graph import Graph

from database import Database
from school_database import SchoolDatabase


db = Database("bolt://35.172.231.11:7687", "neo4j", "machine-ponds-diary")
db.drop_all()


school_db = SchoolDatabase(db)

# Criando professores
school_db.create_professor("Aline","1998","123.456.789-10")
school_db.create_professor("Marisa","1950","012.345.678-91")
school_db.create_professor("Elza","1987","901.234.567-89")
school_db.create_professor("Marcelo","1978","890.123.456-78")
school_db.create_professor("Renzo","1956","789.012.345-67")
school_db.create_professor("Justino","1995","678.901.234-56")

school_db.create_school("Sanico Teles","R. OlÃ¡vo MarquÃªs",181)
school_db.create_school("Sinhã Moreira","Av. Dr. Delfim Moreira",509)
school_db.create_school("Zenaide","Conj. Hab. Gilberto Rossetti",332)
school_db.create_school("Luis Machado Filho","R. LuÃ­s Machado",100)

school_db.create_city("Santa Rita do Sapucaí","37540-000",43753)
school_db.create_city("Serra da Saudade","35617-000",776)
school_db.create_city("Cidadezinha","13737-635",68980)

school_db.create_state("Minas Gerais","Brasil")


school_db.create_escola_professor_trabalha("Renzo","Luis Machado Filho")
school_db.create_escola_professor_trabalha("Justino","Zenaide")
school_db.create_escola_professor_trabalha("Aline","SinhÃ Moreira")
school_db.create_escola_professor_trabalha("Marcelo","Sanico Teles")
school_db.create_escola_professor_trabalha("Elza","SinhÃ¡ Moreira")
school_db.create_escola_professor_trabalha("Marisa","Sanico Teles")

school_db.create_localidade_da_escola("SinhÃ Moreira ","Santa Rita do Sapucaí")
school_db.create_localidade_da_escola("Sanico Teles","Santa Rita do Sapucaí")
school_db.create_localidade_da_escola("Luis Machado Filho","Serra da Saudade")
school_db.create_localidade_da_escola("Zenaide","Cidadezinha")

school_db.create_state_city("Santa Rita do Sapucaí","Minas Gerais")
school_db.create_state_city("Serra da Saudade","Minas Gerais")
school_db.create_state_city("Cidadezinha","Minas Gerais")



db.close()