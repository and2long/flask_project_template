"""instance/postgresql.py
"""

# TODO: change to your own database credentials
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    'user': 'db-user',
    'password': 'db-password',
    'host': '127.0.0.1',
    'name': 'db-name'
})
