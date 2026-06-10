import random
from runtime.company_registry import CompanyRegistry
from typing import List, Dict, Any

class AutoCompanyBuilder:
    # Lista de nomes fixos (reais)
    NAMES = [
        "Ana", "João", "Maria", "Pedro", "Cláudia", "Lucas",
        "Carla", "Rafael", "Fernanda", "Bruno", "Beatriz",
        "Gustavo", "Juliana", "Carlos", "Patrícia", "Ricardo"
    ]

    def __init__(self, registry: CompanyRegistry, analyzer=None):
        self.registry = registry
        self.analyzer = analyzer

    def create_or_use_company(self, task_description: str):
        analysis = (
            self.analyzer(task_description)
            if self.analyzer
            else self._default_analyzer(task_description)
        )

        domain = analysis["domain"]
        departments_info = analysis["departments"]

        name, company = self.registry.find_relevant_company(domain)
        if company:
            print(f"[AUTO] Usando empresa existente: {name}")
            return name, company

        company_name = f"{domain}_auto_{random.randint(1000,9999)}"
        new_company = self._build_company_structure(domain, departments_info, task_description)
        self.registry.add_company(company_name, new_company)

        print(f"[AUTO] Criada nova empresa: {company_name}")
        return company_name, new_company

    # ---------------------------------------------------
    # Gera nomes a partir da lista fixa
    # ---------------------------------------------------
    def _pick_name(self):
        return random.choice(self.NAMES)

    # ---------------------------------------------------
    # Gera cargo dinamicamente a partir do prompt/skill
    # ---------------------------------------------------
    def _make_identity(self, role: str, skill: str = ""):
        name = self._pick_name()
        if skill:
            position = f"{role} especializado em {skill}"
        else:
            position = f"{role} geral"
        return name, position

    # ---------------------------------------------------
    def _build_company_structure(self, domain: str, departments_info: List[Dict[str, Any]], task_description: str):

        ceo_name, ceo_position = self._make_identity("CEO")
        ceos = [{
            "name": ceo_name,
            "persona": f"{domain} visionary",
            "skills": ["coordination", "decision making"],
            "position": ceo_position
        }]

        departments = []

        for i, dept_info in enumerate(departments_info, start=1):
            dept_name = dept_info.get("name", f"Dept{i}")
            skills = dept_info.get("skills", ["general"])

            manager_name, manager_position = self._make_identity("Gerente")
            manager = {
                "name": manager_name,
                "persona": f"{dept_name} lead",
                "skills": skills,
                "position": manager_position
            }

            workers = []
            for skill in skills:
                worker_name, worker_position = self._make_identity("Profissional", skill)
                workers.append({
                    "name": worker_name,
                    "persona": f"{skill} specialist",
                    "skills": [skill],
                    "position": worker_position
                })

            departments.append({
                "name": dept_name,
                "manager": manager,
                "workers": workers
            })

        return {
            "type": domain,
            "ceos": ceos,
            "departments": departments
        }

    def _default_analyzer(self, task_description: str):
        words = [w.strip().lower() for w in task_description.split() if len(w) > 3]
        departments = [{"name": w.capitalize(), "skills": [w]} for w in words[:5]]
        return {"domain": "general", "departments": departments}