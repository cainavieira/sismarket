from dotenv import load_dotenv
import pathlib
import os
import psycopg2

env_path = pathlib.Path(__file__).parent.parent/ ".github" / pathlib.Path("credentials.env") 
load_dotenv(dotenv_path= env_path)

"Dados para entrar no data base credential.env"

DATABASE = os.getenv("PGDATABASE")
HOST = os.getenv("PGHOST")
USER = os.getenv("PGUSER")
PASSWORD = os.getenv("PGPASSWORD")
SSLMODE = os.getenv("PGSSLMODE")
CHANNEL_BINDING = os.getenv("PGCHANNELBINDING")

def get_conn():
    return psycopg2.connect  (
        dbname=DATABASE,
        user=USER,
        password=PASSWORD,
        host=HOST,
        sslmode=SSLMODE,
        channel_binding=CHANNEL_BINDING
    )

def ler_estoque_db():
    storage = []
    try:
        with get_conn() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM sismarket.estoque;")
                rows = cursor.fetchall()
                for row in rows:
                    id_prod,nome,qtd,price = row
                    storage.append([id_prod,nome,qtd,float(price)])
    except Exception as error:
                print(error)
                exit()
    return storage

def gravar_estoque_db(caixa_infos):
    try:
        with get_conn() as conn:
            with conn.cursor() as cursor:
                for info_row in caixa_infos:
                    cursor.execute('''
                            INSERT INTO sismarket.estoque (id_product,product,stock_count,price) VALUES (%s,%s,%s,%s) ON CONFLICT (id_product) DO NOTHING
                            ''', (info_row)
                            )
        conn.commit()
        print("Data base was updated")
    except Exception as error:
        print("Error: ", error)
        exit()

