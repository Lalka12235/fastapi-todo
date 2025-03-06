from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class TasksOrm(Base):
    __tablename__ = 'tasks'

    username: Mapped[str]
    task_id: Mapped[int] = mapped_column(autoincrement=True,primary_key=True)
    task: Mapped[str]
    description: Mapped[str]
    is_completed: Mapped[bool]