class Pagamento:
    """Classe base para todas as modalidades de pagamento."""

    def __init__(self, valor_base: float):
        self._valor_base = valor_base

    def calcular_valor_final(self) -> float:
        # Retorna o valor base sem alterações por padrão
        return self._valor_base


class PagamentoDebito(Pagamento):
    """Pagamento no débito: sem acréscimo de valor."""

    def calcular_valor_final(self) -> float:
        return self._valor_base


class PagamentoPix(Pagamento):
    """Pagamento via Pix: desconto de 5%."""

    def calcular_valor_final(self) -> float:
        return self._valor_base * 0.95


class PagamentoDinheiro(Pagamento):
    """Pagamento em dinheiro: desconto de 3%."""

    def calcular_valor_final(self) -> float:
        return self._valor_base * 0.97


class PagamentoCartao(Pagamento):
    """Pagamento no cartão de crédito: acréscimo de 5%."""

    def calcular_valor_final(self) -> float:
        return self._valor_base * 1.05
