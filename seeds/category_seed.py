from db import *

category1 = Category(name = "Soccer")
db_session.add(category1)

category2 = Category(name = "Basketball")
db_session.add(category2)

category3 = Category(name = "Baseball")
db_session.add(category3)

category4 = Category(name = "Frisbee")
db_session.add(category4)

category5 = Category(name = "Snowboarding")
db_session.add(category5)

category6 = Category(name = "rock Climbing")
db_session.add(category6)

category7 = Category(name = "foosball")
db_session.add(category7)

category8 = Category(name = "skating")
db_session.add(category8)

category9 = Category(name = "hockey")
db_session.add(category9)

db_session.commit()
