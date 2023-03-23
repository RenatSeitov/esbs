from database.database import SessionLocal


class MySuperContextManager:
    def init(self):
        self.db = SessionLocal()

    def enter(self):
        return self.db

    def exit(self, exc_type, exc_value, traceback):
        self.db.close()


async def get_db():
    with MySuperContextManager() as db:
        yield db