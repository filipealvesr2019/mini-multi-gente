import random
from runtime.company_registry import CompanyRegistry
from typing import List, Dict, Any

class AutoCompanyBuilder:
    def __init__(self, registry: CompanyRegistry, analyzer=None):
        """
        analyzer: função que recebe task_description e retorna
        {"domain": str, "departments": [{"name": str, "skills": List[str]}]}
        """
        self.registry = registry
        self.analyzer = analyzer

    def create_or_use_company(self, task_description: str):
        """
        Cria uma nova empresa ou usa uma existente.
        Tudo é gerado dinamicamente com base no prompt.
        """
        # Análise da tarefa
        analysis = self.analyzer(task_description) if self.analyzer else self._default_analyzer(task_description)
        domain = analysis["domain"]
        departments_info = analysis["departments"]

        # Verifica se já existe empresa relevante
        name, company = self.registry.find_relevant_company(domain)
        if company:
            print(f"[AUTO] Usando empresa existente: {name}")
            return name, company

        # Cria empresa dinâmica
        company_name = f"{domain}_auto_{random.randint(1000,9999)}"
        new_company = self._build_company_structure(domain, departments_info)
        self.registry.add_company(company_name, new_company)
        print(f"[AUTO] Criada nova empresa: {company_name}")
        return company_name, new_company

    def _build_company_structure(self, domain: str, departments_info: List[Dict[str, Any]]):
        """
        Cria CEO, departamentos e workers dinamicamente com base nas skills.
        """
        # CEO único
        ceos = [{
            "name": f"CEO_{domain}_{random.randint(1,999)}",
            "persona": f"{domain} visionary",
            "skills": ["coordination", "decision making"]
        }]

        # Criação dinâmica de departamentos e workers
        departments = []
        for i, dept_info in enumerate(departments_info, start=1):
            dept_name = dept_info.get("name", f"Dept{i}")
            skills = dept_info.get("skills", ["general"])
            manager_name = f"Manager_{dept_name}_{random.randint(1,999)}"

            dept = {
                "name": dept_name,
                "manager": {
                    "name": manager_name,
                    "persona": f"{dept_name} lead",
                    "skills": skills
                },
                "workers": [
                    {"name": f"{skill}_Worker_{j}", "persona": f"{skill} specialist", "skills": [skill]}
                    for j, skill in enumerate(skills, start=1)
                ]
            }
            departments.append(dept)

        return {
            "type": domain,
            "ceos": ceos,
            "departments": departments
        }

    def _default_analyzer(self, task_description: str):
        """
        Fallback simples se não houver analisador externo.
        Cria 1 departamento por palavra-chave e uma skill por departamento.
        """
        words = [w.strip().lower() for w in task_description.split() if len(w) > 3]
        departments = [{"name": w.capitalize(), "skills": [w]} for w in words[:5]]
        return {"domain": "general", "departments": departments}