#aumento de 15% no salario de 750

x = 750
porcentagem_aumento = 15
porcentagem_diminuicao = 15

aumento = (porcentagem_aumento / 100) * x
diminuicao = (porcentagem_diminuicao / 100) * x

novo_valor_apos_aumento = x + aumento
novo_valor_apos_diminuicao = x - diminuicao

print(f"Após um aumento de {porcentagem_aumento}%, o valor é {novo_valor_apos_aumento}.")
print(f"Após uma diminuição de {porcentagem_diminuicao}%, o valor é {novo_valor_apos_diminuicao}.")
