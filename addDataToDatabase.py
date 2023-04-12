import firebase_admin
from firebase_admin import credentials, db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':""
})

ref = db.reference('Students')

data = {
    "123456":
    {
        "name": "Abdullah Jirjees",
        "major": "AI",
        "starting_year": 2014,
        "total_attendance": 6, 
        "standing":"G",
        "year": 4,
        "last_attendance_time":"2023-04-10 14:25:00"
    },

     "234567":
    {
        "name": "Elon Mask",
        "major": "Rocket Science",
        "starting_year": 2017,
        "total_attendance": 8, 
        "standing":"VG",
        "year": 3,
        "last_attendance_time":"2023-04-08 08:25:00"
    },

     "345678":
    {
        "name": "Jesse Cook",
        "major": "Music",
        "starting_year": 2020,
        "total_attendance": 1, 
        "standing":"G",
        "year": 1,
        "last_attendance_time":"2023-04-11 12:44:30"
    }
}

for key, value in data.items():
    ref.child(key).set(value)