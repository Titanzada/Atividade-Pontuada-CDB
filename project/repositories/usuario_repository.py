from project.models.usuario_model import Usuario
from sqlalchemy.orm import Session

class UsuarioRepository:
    def __init__(self, session: Session):
        self.session = session

    def salvar_usuario(self, usuario: Usuario):

        try:
            self.session.add(usuario)
            self.session.commit()
        except Exception as erro:
            self.session.rollback()
            print(f"Erro ao salvar usuário: {erro}")
            raise erro

    def listar_usuarios(self):
        try:
            return self.session.query(Usuario).all()
        except Exception as erro:
            print(f"Erro ao listar usuários: {erro}")
            raise erro

    def pesquisar_usuario_por_email(self, email: str):
        try:
            return self.session.query(Usuario).filter_by(email=email).first()
        except Exception as erro:
            print(f"Erro ao pesquisar usuário: {erro}")
            raise erro

    def excluir_usuario(self, usuario: Usuario):
        try:
            self.session.delete(usuario)
            self.session.commit()
        except Exception as erro:
            self.session.rollback()
            print(f"Erro ao excluir usuário: {erro}")
            raise erro

    def atualizar_usuario(self, usuario: Usuario, novos_dados: dict):
        try:
            for key, value in novos_dados.items():
                if hasattr(usuario, key):
                    setattr(usuario, key, value)
            self.session.commit()
        except Exception as erro:
            self.session.rollback()
            print(f"Erro ao atualizar usuário: {erro}")
            raise erro
