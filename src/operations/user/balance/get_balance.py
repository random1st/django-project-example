from db.core.models import UserStorage, UserBalanceStorage


def get_balance(user_id):
    user = UserStorage.get_by_id(user_id)
    balance = UserBalanceStorage.get_user_balance(user)
    return balance
