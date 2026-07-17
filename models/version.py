from sqlalchemy import Column, Integer, String
from database.database import Base


class Version(Base):
    __tablename__ = "versions"

    id = Column(Integer, primary_key=True, index=True)

    version_number = Column(Integer)

    document_name = Column(String)