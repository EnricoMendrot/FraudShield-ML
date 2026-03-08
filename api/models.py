from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String

from api.database import Base


class User(Base):
    """
    User model for authentication and profiles.
    """

    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, index=True, autoincrement=True)
    username = Column("username", String, unique=True, index=True)
    email = Column("email", String, unique=True, index=True)
    hashed_password = Column("hashed_password", String)
    is_active = Column("is_active", Boolean, default=True)
    is_admin = Column("is_admin", Boolean, default=False)

    def __init__(
        self, username, email, hashed_password, is_active=True, is_admin=False
    ):
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.is_active = is_active
        self.is_admin = is_admin


class Prediction(Base):
    """
    Model for storing fraud detection prediction results.
    """

    __tablename__ = "predictions"

    id = Column("id", Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column("user_id", Integer, ForeignKey("users.id"))
    transaction_id = Column("transaction_id", String, unique=True, index=True)
    amount = Column("amount", Float)
    is_fraud = Column("is_fraud", Boolean)
    created_at = Column("created_at", DateTime, default=datetime.utcnow)

    def __init__(self, user_id, transaction_id, amount, is_fraud, created_at=None):
        self.user_id = user_id
        self.transaction_id = transaction_id
        self.amount = amount
        self.is_fraud = is_fraud
        self.created_at = created_at or datetime.utcnow()
