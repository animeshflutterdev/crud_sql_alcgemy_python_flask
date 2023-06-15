from main import User, Session, engine
from sqlalchemy import desc

local_session = Session(bind=engine)

## For ordering 
# users = local_session.query(User).order_by(User.userName).all()

## Decending in order
users = local_session.query(User).order_by(desc(User.userName)).all()

for user in users:
    print(f'All users in order {user}')