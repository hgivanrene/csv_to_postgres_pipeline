def run():
    import pandas as pd
    from sqlalchemy import create_engine, text
    import os
    from dotenv import load_dotenv

    load_dotenv()

    # Configuración de conexión a la base de datos
    DB_NAME = os.getenv('DB_NAME')
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')

    # Nombre del archivo CSV y de la tabla en la base de datos
    csv_file_path = 'scripts/jobs.csv'
    schema_name = 'celerix'
    table_name = 'jobs'

    # Conexión a la base de datos usando SQLAlchemy
    engine = create_engine(f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}')

    create_table_sql = f'''
        CREATE TABLE IF NOT EXISTS {DB_NAME}.{schema_name}.{table_name} (
            job_id INT PRIMARY KEY,
            job_name VARCHAR(100)
        );
        '''
    
    # Crear DDL de la tabla
    try:
        with engine.connect() as connection:
            connection.execute(text(create_table_sql))
        print(f"Tabla '{table_name}' creada o reemplazada en el esquema '{schema_name}'")
    except Exception as e:
        print("Error al crear la tabla:", e)

    # Leer el archivo CSV
    try:
        data = pd.read_csv(csv_file_path)
        print(f'Datos extraidos desde {csv_file_path}')
    except FileNotFoundError:
        print('Archivo CSV no encontrado.')
        exit()

    # Cargar los datos en la tabla de postgresql
    try:
        data.to_sql(table_name, engine, if_exists='replace', index=False, schema=schema_name)
        print(f"Datos cargados exitosamente en la tabla '{table_name}' del esquema '{schema_name}' de la base de datos '{DB_NAME}'")
    except Exception as e:
        print('Error al cargar los datos:', e)


if __name__ == '__main__':
    run()