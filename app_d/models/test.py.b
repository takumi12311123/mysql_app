"""
ログイン関連の処理をここに書く
"""
from .abstract import AbstractModel
from hashlib import sha256

class TestModel(AbstractModel):
    """
    ログイン，セッションなどの情報はここに書く
    """

    def __init__(self, config):
        super().__init__(config)

    def fetch_user_by_id(self, userid):
        sql = "SELECT * FROM p_users  WHERE id=%s"
        return self.fetch_one(sql, userid)

    def fetch_upper_list(self, userid):
        sql = "SELECT * FROM p_users  WHERE id>=%s"
        return self.fetch_all(sql, userid)

    def signup(self, username, password):
        hashed_password = self.hash_password(password)
        sql = "INSERT INTO p_users (username, password) VALUE (%s, %s);"
        self.execute(sql, username, hashed_password)

    def fetch_user_by_name(self, username):
        sql = "SELECT * FROM p_users  WHERE username=%s"
        return self.fetch_one(sql, username)
    
    def hash_password(self, password: str):
        return sha256(password.encode()).hexdigest()
