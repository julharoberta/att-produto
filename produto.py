# Definição da classe Produto
class Produto:
    def __init__(self, nome, codigo, preco, quantidade):
        # Atributos privados
        self._nome = nome
        self._codigo = codigo
        self._preco = preco
        self._quantidade = quantidade

    # Métodos para obter os atributos
    def obtem_nome(self):
        return self._nome

    def obtem_codigo(self):
        return self._codigo

    def obtem_preco(self):
        return self._preco

    # Método para alterar o preço e verificar se houve aumento
    def altera_preco(self, novo_preco):
        preco_anterior = self._preco
        self._preco = novo_preco
        return novo_preco > preco_anterior

    # Método para alterar a quantidade
    def altera_quantidade(self, nova_quantidade):
        self._quantidade = nova_quantidade

    # Método para verificar se há quantidade suficiente para venda
    def verifica_disponibilidade(self, quantidade_requerida):
        return quantidade_requerida <= self._quantidade


# Criação dos objetos p1 e p2
p1 = Produto("Oferta do dia", "P001", 50, 30)  # Produto p1 com preço inicial de 50 e quantidade de 30
p2 = Produto("Oferta da semana", "P002", 60, 50)  # Produto p2 com preço inicial de 60 e quantidade de 50

# Teste para alterar o preço de p1 e verificar se houve redução
preco_reduzido = not p1.altera_preco(40)  # Altera o preço de p1 para 40 e verifica se reduziu

# Resultado da verificação de redução de preço
if preco_reduzido:
    print("O preço da 'Oferta do dia' foi reduzido para 40.")
else:
    print("O preço da 'Oferta do dia' não foi reduzido.")

# Teste para alterar a quantidade de p2 e verificar a disponibilidade para venda
quantidade_requerida = 100
p2.altera_quantidade(quantidade_requerida)  # Altera a quantidade de p2 para 100
disponivel_para_venda = p2.verifica_disponibilidade(quantidade_requerida)

# Verificação da disponibilidade e cálculo do valor total da venda
if disponivel_para_venda:
    valor_total_venda = p2.obtem_preco() * quantidade_requerida
    print(f"Pode ser realizada a venda de {quantidade_requerida} unidades da 'Oferta da semana'.")
    print(f"Valor total da venda: {valor_total_venda}.")
else:
    print("Não há quantidade suficiente da 'Oferta da semana' para a venda.")
