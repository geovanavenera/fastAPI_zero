from sqlalchemy import select

from fastapi_zero.models import User


def test_create_user(session):
    new_user = User(username="geovana", password="secret", email="teste@test")
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == "geovana"))

    assert user.username == "geovana"
