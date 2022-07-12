"""
ログイン関連の処理をここに書く
"""
from .abstract import AbstractModel

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
        sql = "INSERT INTO p_users (username, password) VALUE (%s, %s);"
        self.execute(sql, username, password)

        
    # def login(self, username, password):
    #     """
    #     :param username: ログインするユーザのユーザ名
    #     :param password: ログインするユーザのパスワード
    #     :return bool:ログインが成功したか
    #     """
    #     user = self.find_user_by_name_and_password(username, password)
    #     # 該当するユーザがいなければFalseを返す
    #     if not user:
    #         return False, None
    #     # TODO: セッションに情報を追加
    #     return True, user

    # def create_user(self, username, password):
    #     hashed_password = self.hash_password(password)
    #     sql = "INSERT INTO users(username, password) VALUE (%s, %s);"
    #     self.execute(sql, username, hashed_password)

    
