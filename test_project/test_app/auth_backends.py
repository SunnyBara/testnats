from test_app.models import Dummy


class DummyBackend:
    def authenticate(self, request, username=None, password=None):
        """
        Authentifie un Dummy par username et password.
        """
        try:
            dummy = Dummy.objects.get(name=username)
        except Dummy.DoesNotExist:
            return None

        if dummy.password == password:
            return dummy
        return None

    def get_user(self, user_id):
        try:
            return Dummy.objects.get(pk=user_id)
        except Dummy.DoesNotExist:
            return None
