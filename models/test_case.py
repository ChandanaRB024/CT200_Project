from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


class TestCase(Base):
    __tablename__ = "test_cases"

    id = Column(Integer, primary_key=True, index=True)

    node_id = Column(Integer, ForeignKey("nodes.id"))

    content = Column(Text, nullable=False)

    node = relationship(
        "Node",
        back_populates="test_cases"
    )