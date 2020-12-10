
import pyodbc
import time
from datetime import date

class SL:

    def __init__(self, server, database):
        print('SL init')
        self.cnx = pyodbc.connect('Driver={SQL Server};'+
        'Server='+server+';'+
        'Database='+database+';'+
        'Trusted_Connection=yes;')
        
        self.crs = self.cnx.cursor()

    def new_session(self, name, characters, alphabet):
        now = date.today() 
        nowdt = now.strftime('%Y-%m-%d %H:%M:%S')
        self.crs.execute("""
                        INSERT INTO name_generator.dbo.session (name, launched, characters, alphabet)
                        VALUES ('"""+name+"""','"""+time.strftime('%Y-%m-%d %H:%M:%S')+"""','"""+characters+"""','"""+alphabet+"""')
                        """)
        
    def new_name(self, value, occurences, points, policy, session):
        self.crs.execute("""
                        INSERT INTO name_generator.dbo.name (value, occurences, points, policy, session)
                        VALUES ('"""+value+"""',"""+str(occurences)+""","""+str(points)+""",'"""+policy+"""','"""+session+"""')
                        """)
            
    def new_policy(self, name):
        self.crs.execute("""
                        IF NOT EXISTS (SELECT * FROM name_generator.dbo.policy
                                        WHERE name = '"""+name+"""')
                        BEGIN
                            INSERT INTO name_generator.dbo.policy (name)
                            VALUES ('"""+name+"""')
                        END
                        """)
            
    def validate_changes(self):
        self.cnx.commit()