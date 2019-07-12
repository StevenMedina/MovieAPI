from user.exceptions import UserAlreadyExistError
from user.models import User


class RegisterUser:
    def __init__(self, email, password, first_name, last_name):
        # Set the internal state for the operation
        self._email = email
        self._password = password
        self._first_name = first_name
        self._last_name = last_name

    def execute(self):
        self.valid_data()
        user_account = self._factory_user_account()

        return user_account

    def valid_data(self):
        # It is a public method to allow clients of this object to validate
        # the data even before to execute the use case.
        user_qs = User.objects.find_by_email(self._email)
        if user_qs.exists():
            # Raise a meaningful error to be catched by the client
            raise UserAlreadyExistError('El correo electrónico no esta disponible')
        return True

    def _factory_user_account(self):
        # Factory to create an user account. Ideally, it would be
        # implemented by the UserAccount manager to simplify the
        # API. But it was implemented here for the purpose of this
        # tutorial
        return User.objects.create_user(
            email=self._email,
            password=self._password,
            **{
                'first_name': self._first_name,
                'last_name': self._last_name,
            }
        )
