# INTEGRANTES DO GRUPO

**RM 575067:** Gilson Gomes da Silva

**RM 575086:** Igor Alcalde de Jesus Borba

# PROBLEMA IDENTIFICADO

Dentro do tema proposto da Global Solution, é visto que pessoas que necessitam de acessibilidade urbana enfrentam uma enorme defasagem na infraestrutura das cidades, como por exemplo falta de rampas para cadeirantes ou sinalização inclusiva para pessoas com deficiência visual.

# OBJETIVO

Para se ampliar esse suporte, propomos com esse programa uma central de denúncias onde todas as pessoas possam reportar lugares que precisam de um cuidado maior, fazendo com que as melhorias cheguem rapidamente e centralizadas, com base na quantidade de denúncias que são feitas.

# ODS 10

O software se encaixa principalmente na ODS 10 (reduzir as desigualdades), com foco em promover a inclusão social de todos os cidadãos.

# Instruções de execução

O programa necessita apenas do Python instalado, após isso apenas rode o arquivo principal no terminal, dentro da pasta, com:

```python central_denuncias.py``` 

Não é necessário nenhuma biblioteca externa.

# Regras de classificação
 
Cada denúncia recebe uma gravidade de 1 a 5, informada pelo usuário (1 = problema leve, 5 = impede completamente o acesso). Com base nela:
 
| Gravidade | Classificação |
|-----------|---------------|
| 4 ou 5 | Urgente |
| 3 | Moderada |
| 1 ou 2 | Baixa |
 
Recomendação automática (feita com o percentual de denúncias urgentes sobre o total):
 
| Percentual de urgentes | Situação | Recomendação |
|------------------------|----------|--------------|
| 50% ou mais | Crítica | Priorizar intervenção imediata no local com mais denúncias |
| De 25% a menos de 50% | Atenção | Programar melhorias no local com mais denúncias |
| Menos de 25% | Controlada | Manter o monitoramento, com foco no local com mais denúncias |

# Descrição dos resultados 

Ao final, o programa é capaz de nos mostrar:

- Cadastro real de denúncias;
- Tabela organizada com todas as denúncias;
- Indicadores que ajudam na hora da tomada de decisão (total, gravidade média, locais com mais denúncias, porcentagem de urgentes e os tipos mais presentes);
- Recomendação automática de onde e como agir.

# Video Pitch explicativo

https://youtu.be/7Ql55a-BBp4
