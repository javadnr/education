import xmlrpc.client
from typing import Any


class OdooClient:
    def __init__(self, url: str, db: str, username: str, password: str):
        self.url = url
        self.db = db
        self.username = username
        self.password = password
        self._common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
        self._models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
        self._uid = self._common.authenticate(db, username, password, {})

    def search_read(self, model: str, domain: list, fields: list,
                     offset: int = 0, limit: int = 100) -> list[dict[str, Any]]:
        return self._models.execute_kw(
            self.db, self._uid, self.password,
            model, "search_read",
            [domain, fields],
            {"offset": offset, "limit": limit},
        )