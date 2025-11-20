from sqlalchemy.orm import Mapped, registry, mapped_column
from datetime import datetime
from sqlalchemy import func, String

table_registry = registry()

@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(String(150), unique=True)
    password: Mapped[str] = mapped_column(String(150))
    email: Mapped[str] = mapped_column(String(150), unique=True)
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())

    # init=False significa que não deve ser passado o atributo quando o objeto for instanciado
    # func serve pra usar as funções SQL nativas