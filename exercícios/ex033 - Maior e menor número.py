# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite outro valor: '))
terceiro_valor = (int(input('Digite mais um valor: ')))

#verificando o menor número
menor = primeiro_valor
if segundo_valor < primeiro_valor and segundo_valor < terceiro_valor:
    menor = segundo_valor
if terceiro_valor < primeiro_valor and terceiro_valor < segundo_valor:
    menor = terceiro_valor

#verificando o maior número
maior = primeiro_valor
if segundo_valor > primeiro_valor and segundo_valor > terceiro_valor:
    maior = segundo_valor
if terceiro_valor > primeiro_valor and terceiro_valor > segundo_valor:
    maior = terceiro_valor

print(f'O menor valor digitado foi {menor}.')
print(f'O maior valor digitado foi {maior}.')