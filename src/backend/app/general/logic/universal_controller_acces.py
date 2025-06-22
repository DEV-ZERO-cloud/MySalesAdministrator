import pyodbc
import os
import logging
from typing import Any, List

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class UniversalControllerAccess:
    def __init__(self, db_path: str = None):
        """
        Inicializa la conexión a la base de datos Microsoft Access.
        :param db_path: Ruta absoluta al archivo .mdb o .accdb
        """
        try:
            if not db_path:
                db_path = os.getenv("ACCESS_DB_PATH")
            if not db_path or not os.path.isfile(db_path):
                raise FileNotFoundError(f"No se encontró la base de datos Access en la ruta: {db_path}")

            driver = '{Microsoft Access Driver (*.mdb, *.accdb)}'
            conn_str = f"DRIVER={driver};DBQ={db_path};"
            self.conn = pyodbc.connect(conn_str, autocommit=False)
            self.cursor = self.conn.cursor()
        except Exception as e:
            logger.error(f"Error al conectar a la base de datos Access: {e}")
            raise

    def execute_query(self, query: str, params: tuple = None) -> List[dict]:
        """
        Ejecuta una consulta SQL y retorna los resultados como una lista de diccionarios.
        """
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return [
                dict(zip([column[0] for column in self.cursor.description], row))
                for row in rows
            ]
        except pyodbc.Error as e:
            logger.error(f"Error al ejecutar la consulta: {e}")
            raise

    def get_all(self, table: str) -> List[dict]:
        """
        Obtiene todos los registros de una tabla.
        """
        query = f"SELECT * FROM [{table}]"
        return self.execute_query(query)

    def get_by_id(self, table: str, id_field: str, id_value: Any) -> dict | None:
        """
        Obtiene un registro por ID.
        """
        query = f"SELECT * FROM [{table}] WHERE [{id_field}] = ?"
        results = self.execute_query(query, (id_value,))
        return results[0] if results else None

    def get_by_column(self, table: str, column_name: str, value: Any) -> List[dict]:
        """
        Obtiene todos los registros de una tabla donde el valor de una columna coincide con el valor proporcionado.
        """
        query = f"SELECT * FROM [{table}] WHERE [{column_name}] = ?"
        return self.execute_query(query, (value,))

    def add(self, table: str, data: dict) -> None:
        """
        Agrega un registro a la tabla.
        """
        columns = ', '.join([f'[{k}]' for k in data.keys()])
        placeholders = ', '.join(['?' for _ in data])
        query = f"INSERT INTO [{table}] ({columns}) VALUES ({placeholders})"
        try:
            self.cursor.execute(query, tuple(data.values()))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            logger.error(f"Error al agregar registro: {e}")
            raise

    def update(self, table: str, id_field: str, data: dict) -> None:
        """
        Actualiza un registro por ID.
        """
        if id_field not in data:
            raise ValueError("El campo ID debe estar en los datos para actualizar.")
        set_clause = ', '.join([f'[{k}] = ?' for k in data if k != id_field])
        query = f"UPDATE [{table}] SET {set_clause} WHERE [{id_field}] = ?"
        values = [data[k] for k in data if k != id_field] + [data[id_field]]
        try:
            self.cursor.execute(query, tuple(values))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            logger.error(f"Error al actualizar registro: {e}")
            raise

    def delete(self, table: str, id_field: str, id_value: Any) -> None:
        """
        Elimina un registro por ID.
        """
        query = f"DELETE FROM [{table}] WHERE [{id_field}] = ?"
        try:
            self.cursor.execute(query, (id_value,))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            logger.error(f"Error al eliminar registro: {e}")
            raise

    def close(self):
        if self.conn:
            self.conn.close()