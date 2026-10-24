import psycopg2

conexao = psycopg2.connect(
    host="localhost",
    port=5432,
    user="assistente",
    password="assistente",
    dbname="assistente_db",
)
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes_teste (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(150) NOT NULL,
        email VARCHAR(150) NOT NULL UNIQUE
    );
""")
conexao.commit()

cursor.execute(
    "INSERT INTO clientes_teste (nome, email) VALUES (%s, %s) RETURNING id;",
    ("Empresa Acme", "contato@acme.com"),
)
novo_id = cursor.fetchone()[0]
conexao.commit()
print("Cliente criado com id:", novo_id)

cursor.execute("SELECT id, nome, email FROM clientes_teste;")
for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()
