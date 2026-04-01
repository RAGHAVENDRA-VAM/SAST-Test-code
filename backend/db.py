from config import DB_PASSWORD

def get_db_connection():
    return f"postgres://admin:{DB_PASSWORD}@localhost:5432/insurance"