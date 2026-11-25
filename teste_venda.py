venda3.adicionar_item(p2, 1)  # Adiciona 1 Teclado (R$ 200,00)
# Total bruto = R$ 200,00

pagamento_dinheiro = PagamentoDinheiro(0)
total_final_dinheiro = venda3.finalizar_venda(pagamento_dinheiro)

print(venda3)
print(f"Valor com Desconto Dinheiro (3%): R$ {total_final_dinheiro:.2f} (Esperado: R$ 194.00)")


# ==========================================
# TESTE EXTRA: Venda paga no DÉBITO (Sem alteração)
# ==========================================
print("\n--- TESTE 4: Pagamento no Débito ---")
venda4 = Venda()
venda4.adicionar_item(p1, 1)  # Adiciona 1 Mouse (R$ 100,00)

pagamento_debito = PagamentoDebito(0)
total_final_debito = venda4.finalizar_venda(pagamento_debito)

print(venda4)
print(f"Valor no Débito (Sem alteração): R$ {total_final_debito:.2f} (Esperado: R$ 100.00)")
