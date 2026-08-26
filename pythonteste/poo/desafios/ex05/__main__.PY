from rich import inspect
from cx05 import Aluno, Professor, Funcionario
a1 = Aluno("Jose", "17", "informatica", "T01")
a1.fazer_aniversario()
a1.fazer_matricula()
inspect(a1, methods=True)

p1 = Professor("samuel", 37, "Biologia", "mestrado")
p1.fazer_aniversario()
p1.dar_aula()


f1 = Funcionario("Claudia", 27, "Secretaria", "Secretaria")
f1.fazer_aniversario()
f1.bater_ponto()
inspect(f1,methods=True)