from src.models.user import User, UserIdentify
from src.models.verifier import Verifier
from src.services.auth import AuthService

def router(app):
    @app.post("/sign-in")
    def sign_in(user: User):

        """
        login no firebase
        """

        return AuthService().sign_in(user)

    @app.post("/sign-up")
    def sign_up(user: User):

        """
        cadastro de usuario
        """

        return AuthService().sign_up(user)

    @app.post("/verification")
    def verifier(token: Verifier):

        """
        verifica o email
        """

        return AuthService().verifier(token)
   
    @app.post("/reset-password")
    def resetPassword(user: UserIdentify):

        """
        verifica o email
        """

        return AuthService().changePassword(user)