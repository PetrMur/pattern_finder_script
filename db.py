import sqlite3


class SQLiteWorker:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.conn = sqlite3.connect(self.filename)
        self.cur = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cur.close()
        self.conn.close()

    def get_domains(self) -> list:
        """ Получить список доменов из базы данных """
        self.cur.execute('SELECT * FROM domains')
        result = self.cur.fetchall()
        return result

    def save_rules(self, projects: list):
        """ Сохранить правила в базу данных """
        sql = f'INSERT INTO rules(project_id, regexp) VALUES'
        values = []
        for project in projects:
            for rule in project.rules:
                values.append(f'({project.project_id}, "{rule}")')
        if len(values) == 0:
            print('Нет правил для сохранения')
            return
        sql = sql + ', '.join(values)
        self.cur.execute(sql)
        self.conn.commit()
