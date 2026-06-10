# runtime/company_registry.py

from copy import deepcopy


class CompanyRegistry:

    def __init__(self):
        self.companies = {}

    def add_company(self, name, company_data):
        """
        Registra uma empresa.
        """
        self.companies[name] = deepcopy(company_data)

    def remove_company(self, name):
        if name in self.companies:
            del self.companies[name]

    def get_company(self, name):
        return self.companies.get(name)

    def company_exists(self, name):
        return name in self.companies

    def list_companies(self):
        return list(self.companies.keys())

    def count(self):
        return len(self.companies)

    def clear(self):
        self.companies.clear()

    def load_from_config(self, companies_config):
        """
        Carrega empresas do COMPANIES_CONFIG.
        """
        self.clear()

        for company_name, company_data in companies_config.items():
            self.add_company(company_name, company_data)

    def find_relevant_company(self, domain):
        """
        Procura empresa pelo domínio.
        Ex:
        software
        marketing
        design
        ai
        """

        for company_name, company_data in self.companies.items():

            company_type = company_data.get("type")

            if company_type == domain:
                return company_name, company_data

        return None, None

    def find_company_by_department(self, department_name):

        department_name = department_name.lower()

        for company_name, company_data in self.companies.items():

            for dep in company_data.get("departments", []):

                if dep["name"].lower() == department_name:
                    return company_name, company_data

        return None, None

    def find_company_by_skill(self, skill):

        skill = skill.lower()

        for company_name, company_data in self.companies.items():

            for dep in company_data.get("departments", []):

                manager = dep.get("manager", {})

                for s in manager.get("skills", []):

                    if s.lower() == skill:
                        return company_name, company_data

                for worker in dep.get("workers", []):

                    for s in worker.get("skills", []):

                        if s.lower() == skill:
                            return company_name, company_data

        return None, None

    def summary(self):

        result = []

        for company_name, company_data in self.companies.items():

            result.append({
                "name": company_name,
                "type": company_data.get("type"),
                "departments": len(company_data.get("departments", []))
            })

        return result