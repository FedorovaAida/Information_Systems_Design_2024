import psycopg2


class DatabaseConnection:

    _instance = None

    def __new__(cls, db_config):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._initialize(db_config)
        return cls._instance

    def _initialize(self, db_config):
        self.connection = psycopg2.connect(
            database=db_config['dbname'],
            user=db_config['user'],
            password=db_config['password'],
            host=db_config['host'],
            port=db_config['port']
        )
        self.connection.autocommit = True
        self.ensure_table_exists()

    def get_cursor(self):
        return self.connection.cursor()

    def table_exists(self, table_name):
        with self.get_cursor() as cursor:
            cursor.execute("""
                SELECT EXISTS (
                    SELECT 1
                    FROM pg_catalog.pg_tables
                    WHERE tablename = %s
                );
            """, (table_name,))
            result = cursor.fetchone()
        return result[0]

    def ensure_table_exists(self):
        if not self.table_exists("patient"):
            with self.get_cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS patient (
                        id UUID PRIMARY KEY,
                        first_name VARCHAR(50) NOT NULL,
                        last_name VARCHAR(50) NOT NULL, 
                        email VARCHAR(255) UNIQUE,                      
                        gender VARCHAR(1) CHECK (gender IN ('М', 'Ж')),
                        phone VARCHAR(15) NOT NULL,
                        disease VARCHAR(500) NOT NULL
                    );
                """)
                print("Таблица 'patient' успешно создана.")
        else:
            print("Таблица 'patient' уже существует.")
