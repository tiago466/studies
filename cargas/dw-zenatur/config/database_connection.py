from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from decouple import config

class DatabaseConnection:
    def __init__(self):
        self.connection_string = config("DB_CONNECTION_STRING")
        self.engine = self.create_engine()
        self.session = self.create_session()

    def create_engine(self):
        engine = create_engine(self.connection_string)
        return engine

    def create_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def execute_query(self, query):
        stmt = text(query)
        result = self.session.execute(stmt)
        return result

    def execute_multiple_queries(self, queries):
        results = []
        for query in queries:
            result = self.execute_query(query)
            results.append(result)
        return results

    def commit_changes(self):
        self.session.commit()

    def rollback_changes(self):
        self.session.rollback()

    def close_connection(self):
        self.session.close()
        self.engine.dispose()