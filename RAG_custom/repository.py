import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from configuration import Configuration
import os 

class RepositoryManager:
    def __init__(self):
        self._config = Configuration()
        self.dbname = self._config["DB_dbname"] 
        self.user = self._config["DB_user"] 
        self.password = self._config["DB_password"] 
        self.host = self._config["DB_host"] 
        self.port = self._config["DB_port"] 
        self.connection = None
        self.cursor = None
        
    def _get_script(self, file_path):
        path = os.path.abspath(file_path)
        print(path)
        with open(path, 'r', encoding='utf-8') as file:
            sql_script = file.read()
            return sql_script
        
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error during connection to PostgreSQL: {e}")

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def _execute_script_from_file(self, file_path):

        if not self.connection or not self.cursor:
            print("Error: Connection to database not established. Call connect() first.")
            return False

        try:
            sql_script = self._get_script(file_path)
            self.cursor.execute(sql_script)
            self.connection.commit()
            return True

        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
            return False
        except Error as e:
            print(f"Error during execution of SQL script: {e}")
            if self.connection:
                self.connection.rollback()
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False
        
    def init_DB(self):
        try:
            conn_default = psycopg2.connect(dbname="postgres", user=self.user, password=self.password, host=self.host, port=self.port)

            conn_default.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor_default = conn_default.cursor()
            
            cursor_default.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{self.dbname}'")
            exists = cursor_default.fetchone()
            
            if not exists:
                cursor_default.execute(f"CREATE DATABASE {self.dbname}")
                print(f"Database '{self.dbname}' has been created.")
            else:
                print(f"Database '{self.dbname}' just existed.")

        except Error as e:
            print(f"Error on creating the database: {e}")
            return
        finally:
            if 'cursor_default' in locals() and cursor_default: cursor_default.close()
            if 'conn_default' in locals() and conn_default: conn_default.close()
        
        try:
            self.connect()
            self._execute_script_from_file('RAG_custom/Scripts/Create_Tables.txt')
            print("Tables created correctly")
            print("Setup compleated!")
        except Error as e:
            print(f"Error on creationing tables: {e}")
            if self.connection: self.connection.rollback()
        finally:
            self.disconnect()
        
        
            
        
