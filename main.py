from tinydb import TinyDB, Query
from studentbase import studentbase
# Create or connect to the database
st=TinyDB('student.json')
db = TinyDB('students.json')
for i in studentbase:
    for item in studentbase[i]:
        st.insert(item)
