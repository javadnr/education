import xmlrpc.client


class OdooClient:

    def __init__(
        self,
        url: str,
        database: str,
        username: str,
        password: str,
    ):
        self.url = url
        self.database = database
        self.username = username
        self.password = password
        
        
        self.common = xmlrpc.client.ServerProxy(
            f"{url}/xmlrpc/2/common",
            allow_none=True
            
        )
        self.models = xmlrpc.client.ServerProxy(
            f"{url}/xmlrpc/2/object",
            allow_none=True
        )

        self.uid = self.common.authenticate(
            database,
            username,
            password,
            {},
        )
        if not self.uid:
            raise Exception(
                "Odoo authentication failed"
            )

    def execute(
        self,
        model: str,
        method: str,
        args=None,
        kwargs=None,
    ):

        return self.models.execute_kw(
            self.database,
            self.uid,
            self.password,
            model,
            method,
            args or [],
            kwargs or {},
        )