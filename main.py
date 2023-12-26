import re

from db import SQLiteWorker
from domains import Project
from collections import Counter


def find_rules(domains):
    """ Поиск паттернов, в задаче не описаны конкретные критерии "плохих" урлов """

    counter = Counter()
    pattern = r'[a-z0-9]+[0-9](-[a-z0-9]+)*'
    for domain in domains:
        if re.match(pattern, domain[0]):
            counter[pattern + '.' + '.'.join(domain[1:])] += 1
    rules = [rule for rule, frequency in counter.items() if frequency > 1]
    return rules


def main():
    with SQLiteWorker('domains.db') as db_conn:
        domains = db_conn.get_domains()
        projects = Project.serialize_projects(domains)
        for project in projects:
            project.rules = find_rules(project.domains)
        db_conn.save_rules(projects)


if __name__ == '__main__':
    main()
