#!_*_coding:utf-8_*_
# __author__: "Lightwing Ng"

'''
main program handle module , handle all the user interaction stuff
'''

from core import auth, accounts, logger, transaction, FinacialFormat
import time

# transaction logger
trans_logger = logger.logger('transaction')
# access logger
access_logger = logger.logger('access')

# Temp account data, can only saves the data in memories.
user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}


def account_info(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])
    LatestInfo = '''
    --------- LATEST INFO --------
    Card Number:\t%s
    Expire Date:\t%s
    Credit     :\tHK$ %s
    Balance    :\tHK$ %s
    ''' % (FinacialFormat.formatCardNum(account_data['id']),
           account_data['expire_date'],
           FinacialFormat.formatNum(account_data['credit']),
           FinacialFormat.formatNum(int(account_data['balance'])))
    print(LatestInfo)


def repay(acc_data):
    '''
    print current balance and let user repay the bill
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = '''
    --------- BALANCE INFO --------
        Credit :\tHK$ %s
        Balance:\tHK$ %s
        ''' % (
        FinacialFormat.formatNum(account_data['credit']),
        FinacialFormat.formatNum(int(account_data['balance'])))
    print(current_balance)

    back_flag = False
    while not back_flag:
        repay_amount = input("\033[33;1mPlease input repay amount: \033[0m").strip()
        if len(repay_amount) > 0 and repay_amount.isdigit():
            new_balance = transaction.make_transaction(
                trans_logger, account_data, 'repay', repay_amount)

            if new_balance:
                print('''New Balance:\n\tHK$ %s''' %
                      FinacialFormat.formatNum(int(new_balance['balance'])))

        else:
            print(
                '\033[31;1m%s is not a valid amount, only accept integer!\033[0m' % FinacialFormat.formatNum(repay_amount))

        if repay_amount == 'b':
            back_flag = True


def withdraw(acc_data):
    '''
    print current balance and let user do the withdraw action
    :param acc_data:
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = '''
    --------- BALANCE INFO --------
        Credit :\tHK$ %s
        Balance:\tHK$ %s
        ''' % (
        FinacialFormat.formatNum(account_data['credit']),
        FinacialFormat.formatNum(int(account_data['balance'])))
    print(current_balance)

    back_flag = False
    while not back_flag:
        withdraw_amount = input(
            "\033[33;1mPlease input withdraw amount:\033[0m").strip()

        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(
                trans_logger, account_data, 'withdraw', withdraw_amount)
            if new_balance:
                print('''New Balance:\n\tHK$ %s''' %
                      FinacialFormat.formatNum(int(new_balance['balance'])))

        else:
            print(
                '\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)

        if withdraw_amount == 'b':
            back_flag = True


def transfer(acc_data):
    pass


def pay_check(acc_data):
    pass


def logout(acc_data):
    print('Thanks for coming, HSBC wish you all the best!')
    exit()


def interactive(acc_data):
    '''
    interact with user
    :return:
    '''
    menu = u'''
    * Hong Kong and Shanghai Bank Cooperation *
    \033[32;1m\t\t1\t账户信息
    \t\t2\t还款(*)
    \t\t3\t取款(*)
    \t\t4\t银联转账
    \t\t5\t打印账单
    \t\t6\t退卡\033[0m
    \t\t\t\t ©2018 HSBC All Rights Reserved.
    '''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
    }

    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>> ").strip()

        if user_option in menu_dic:
            menu_dic[user_option](acc_data)
        else:
            print("\033[31;1mSorry!\nption does not exist!\033[0m")


def run():
    '''
    This function will be called right away when the program started, here handles the user interaction stuff
    :return:
    '''

    acc_data = auth.acc_login(user_data, access_logger)

    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)
