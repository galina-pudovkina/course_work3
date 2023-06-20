from datetime import datetime
import json


def load_operations(path):
    """Загружает словарь JSON"""
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
    return data


def select_data(data):
    """Возвращает список успешно проведенных операций"""
    selected_data = []

    for row in data:
        if 'state' in row and row['state'] == 'EXECUTED':
            selected_data.append(row)

    return selected_data


def sort_data(data):
    """Возвращает список 5 последних операций"""
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:5]


def changes_format_account(account):
    """Получает список с счетом отправителя/получателя и выводит его замаскированным"""
    if len(account[-1]) == 20:
        account_masc = " ".join(account[:-1]) + ' ' + f'**{account[-1][-4:]}'
    elif len(account[-1]) == 16:
        account_masc = " ".join(
            account[:-1]) + ' ' + f'{account[-1][:4]} {account[-1][4:6]}** **** {account[-1][-4:]}'
    else:
        print("Некорректный формат")

    return account_masc


def create_operations(data):
    """Форматирует словарь data и выводит список транзакции в нужном формате"""
    operations = []

    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = row['description']
        recipient = changes_format_account(row['to'].split())

        if 'from' in row:
            sender = changes_format_account(row['from'].split())
        else:
            sender = ''
        amount = row['operationAmount']['amount'] + ' ' + row['operationAmount']['currency']['name']

        operations.append(f"""
{date} {description}
{sender} -> {recipient}
{amount} \n""")

    return operations
