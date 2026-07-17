from sqlalchemy import Column, Integer, String, ForeignKey
from database.database import Base


class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key=True, index=True)

    heading = Column(String, nullable=False)

    body = Column(String)

    level = Column(Integer)

    content_hash = Column(String)

    parent_id = Column(Integer, nullable=True)

    document_id = Column(Integer, ForeignKey("documents.id"))