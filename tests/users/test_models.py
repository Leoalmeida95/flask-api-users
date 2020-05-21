# Third

from mongoengine import (
    BooleanField,
    StringField
)

# Apps

from apps.users.models import User


class TestUser:

    def setup_method(self):
        self.car = {
            'color': 'red', 'value': 10000,
            'mileage': 0, 'number_ports': 2
        }

        self.data = {
            'email': 'teste1@teste.com', 'password': 'teste123',
            'active': True, 'full_name': 'Teste',
            'cpf_cnpj': '11111111111',
        }

        # Crio uma instancia do modelo User
        self.user = User(**self.data)

    def test_email_field_exists(self):
        """
        Verifico se o campo email existe
        """
        assert 'email' in self.user._fields

    def test_email_field_is_required(self):
        """
        Verifico se o campo email é requirido
        """
        assert self.user._fields['email'].required is True

    def test_email_field_is_unique(self):
        """
        Verifico se o campo email é unico
        """
        assert self.user._fields['email'].unique is True

    def test_email_field_is_str(self):
        """
        Verifico se o campo email é do tipo string
        """
        assert isinstance(self.user._fields['email'], StringField)

    def test_active_field_exists(self):
        assert 'active' in self.user._fields

    def test_active_field_is_default_true(self):
        assert self.user._fields['active'].default is False

    def test_active_field_is_bool(self):
        """
        Verifico se o campo active é booleano
        """
        assert isinstance(self.user._fields['active'], BooleanField)

    def test_full_name_field_exists(self):
        """
        Verifico se o campo full_name existe
        """
        assert 'full_name' in self.user._fields

    def test_full_name_field_is_str(self):
        assert isinstance(self.user._fields['full_name'], StringField)

    def test_all_fields_in_user(self):
        """
        Verifico se todos os campos estão de fato no meu modelo
        """
        fields = [
            'active', 'cpf_cnpj', 'created', 'email',
            'full_name', 'id', 'password', 'roles'
        ]

        user_keys = [i for i in self.user._fields.keys()]

        fields.sort()
        user_keys.sort()

        assert fields == user_keys
