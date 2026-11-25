# sisvenda/venda.py
from datetime import datetime
from item_venda import Item_Venda
from produto import Produto
from pagamento import Pagamento  # Importação da classe pai de pagamento


class Venda:
    # Atributo de classe para controlar o total de vendas existentes no sistema
    _total_vendas = 0

    def __init__(self, data_venda: datetime = datetime.now()):
        self._valor_total = 0.0
        self._data_venda = data_venda
        self._itens: list[Item_Venda] = []
        
        # Incrementa o atributo de classe a cada nova venda criada
        Venda._total_vendas += 1

    @property
    def itens(self):
        return self._itens

    def adicionar_item(self, produto: Produto, quantidade: int):
        if produto.decrementar_estoque(quantidade):
            novo_item = Item_Venda(produto, quantidade)
            self._itens.append(novo_item)
            self._valor_total += novo_item.valor
            return True
        else:
            return False

    def remover_item(self, produto: Produto):
        for item in self._itens:
            if item.produto == produto:
                self._itens.remove(item)
                self._valor_total -= item.valor
                produto.incrementar_estoque(item.quantidade)
                return True
        return False

    def calcular_valor_total(self):
        return self._valor_total

    def finalizar_venda(self, forma_pagamento: Pagamento):
        """Método que aplica o polimorfismo, recebendo qualquer objeto que herde de Pagamento

        e calculando o valor final com base na regra específica daquela modalidade.
        """
        # Define o valor base do pagamento com o total acumulado da venda
        forma_pagamento._valor_base = self.calcular_valor_total()

        # Retorna o valor final com descontos ou acréscimos aplicados
        return forma_pagamento.calcular_valor_final()

    def __str__(self):
        string = "\n========== COMPROVANTE =========="
        string += f"\nVenda: {self._data_venda.strftime('%d/%m/%Y %H:%M:%S')}"
        string += "\n---------------------------------"

        for item in self._itens:
            string += (
                f"\n{item.produto.descricao} | "
                f"{item.quantidade}x | "
                f"R$ {item.produto.preco_unitario:.2f} | "
                f"Subtotal: R$ {item.valor:.2f}"
            )
        string += "\n---------------------------------"
        string += f"\nValor total: R$ {self.calcular_valor_total():.2f}"
        string += "\n================================="
        return string
