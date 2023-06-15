from jira import JIRA

# API-ключ пользователя
api_token = "API Key из Jira"

# Ключ вашего проекта
PROJECT_KEY = 'YOUR_PROJECT_KEY'

# Инициализация клиента Jira с использованием API-ключа
jira = JIRA(server='Server', basic_auth=('email', api_token))

def get_fix_version_issues(fix_version):

    # Формируем JQL-запрос для поиска задач по фиксированной версии
    jql_query = f"project = {PROJECT_KEY} AND fixVersion = '{fix_version}'"

    # Получаем список задач
    issues = jira.search_issues(jql_query, maxResults=1000)

    # Выводим ID задачи и ее статус
    print("Задачи, которые вошли в релиз:")
    for issue in issues:
        issue_key = issue.key
        issue_status = issue.fields.status.name
        print(f"Issue: {issue_key} | Status: {issue_status}")

    # Формируем JQL-запрос для поиска задач, не находящихся в статусе "Done"
    jql_query_not_done = f"project = CMT1 AND fixVersion = '{fix_version}' AND status != Done"

    # Получаем список задач, не находящихся в статусе "Done"
    not_done_issues = jira.search_issues(jql_query_not_done, maxResults=1000)

    # Выводим ID задачи и ее статус для задач, не находящихся в статусе "Done"
    print("Задачи, не находящиеся в статусе 'Done':")
    for issue in not_done_issues:
        issue_key = issue.key
        issue_status = issue.fields.status.name
        print(f"Issue: {issue_key} | Status: {issue_status}")

# Fix Version
get_fix_version_issues('1.0.0')
