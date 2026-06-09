from runtime.pipeline import MultiOrgSystem

system = MultiOrgSystem()

output = system.run("criar editor de texto")
print("Resultado final:", output)