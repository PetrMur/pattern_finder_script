class Project:
    """ Модель для связки проекта с доменами и правилами """

    def __init__(self, project_id: str, domains: list):
        self.project_id = project_id
        self.domains = list(map(lambda x: x.split('.'), domains))
        self.rules = []

    @classmethod
    def serialize_projects(cls, domains_list: list) -> list:
        """ Сериализовать данные и сгруппировать доменные имена по проектам """

        projects_with_domains = {}
        for domain in domains_list:
            if domain[0] in projects_with_domains.keys():
                projects_with_domains[domain[0]].append(domain[1])
            else:
                projects_with_domains[domain[0]] = [domain[1]]

        projects = []
        for project, domains in projects_with_domains.items():
            projects.append(cls(project, domains))
        return projects
