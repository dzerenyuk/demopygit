class BankAccount:
    start_sum = 2000
    def __init__(self, client_id, name, user_sum):
        self.client_id = client_id
        self.name = name
        self.user_sum = user_sum
    def account_replenishment(self, sum_to_replenish):
        self.user_sum += sum_to_replenish
        return self.user_sum

first_user = BankAccount(1, 'Dmytro', 250)

first_user.account_replenishment(250)
print(first_user.user_sum)