from app.database.database import Base, engine, SessionLocal
from app.models.user import User
from app.routers.users import get_all_users


Base.metadata.create_all(engine)


def main():

    session = SessionLocal()

    try:
        users = get_all_users(session)

        print("Fetched Users:")

        for user in users:
            print(
                f"ID: {user.id}, "
                f"Name: {user.name}, "
                f"Email: {user.email}"
            )

    finally:
        session.close()


if __name__ == "__main__":
    main()