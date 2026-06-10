# runtime/companies_config.py

COMPANIES_CONFIG = {

    "software_house": {
        "type": "software",
        "ceos": [
            {
                "name": "Alice",
                "persona": "visionary strategist",
                "skills": ["coordination", "decision making"]
            }
        ],
        "departments": [
            {
                "name": "Frontend",
                "manager": {
                    "name": "Carlos",
                    "persona": "frontend lead",
                    "skills": ["react", "typescript"]
                },
                "workers": [
                    {"name": "João", "persona": "react developer", "skills": ["react", "javascript"]},
                    {"name": "Ana", "persona": "ui designer", "skills": ["css", "figma"]}
                ]
            },
            {
                "name": "AI",
                "manager": {
                    "name": "Pedro",
                    "persona": "ai lead",
                    "skills": ["llm", "agents"]
                },
                "workers": [
                    {"name": "Marina", "persona": "prompt engineer", "skills": ["prompts", "reasoning"]}
                ]
            }
        ]
    },

    "marketing_agency": {
        "type": "marketing",
        "ceos": [
            {
                "name": "Beatriz",
                "persona": "marketing visionary",
                "skills": ["strategy", "branding"]
            }
        ],
        "departments": [
            {
                "name": "Copywriting",
                "manager": {
                    "name": "Lucas",
                    "persona": "copy lead",
                    "skills": ["writing", "storytelling"]
                },
                "workers": [
                    {"name": "Marcos", "persona": "copywriter", "skills": ["ads copy", "blogs"]},
                    {"name": "Sofia", "persona": "storyteller", "skills": ["narratives", "scripts"]}
                ]
            },
            {
                "name": "Social Media",
                "manager": {
                    "name": "Fernanda",
                    "persona": "social lead",
                    "skills": ["instagram", "tiktok", "strategy"]
                },
                "workers": [
                    {"name": "Rafael", "persona": "instagram specialist", "skills": ["instagram", "content"]},
                    {"name": "Camila", "persona": "tiktok specialist", "skills": ["tiktok", "trends"]}
                ]
            },
            {
                "name": "Ads",
                "manager": {
                    "name": "Eduardo",
                    "persona": "ads lead",
                    "skills": ["facebook ads", "google ads"]
                },
                "workers": [
                    {"name": "Tiago", "persona": "facebook ads specialist", "skills": ["facebook ads", "analytics"]},
                    {"name": "Patrícia", "persona": "google ads specialist", "skills": ["google ads", "analytics"]}
                ]
            }
        ]
    }
}