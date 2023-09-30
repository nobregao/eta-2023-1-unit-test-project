class Restaurant:
    """Model de restaurante simples."""

    QUANTIDADE_INVALIDA = 0

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """
        Retorna uma descrição simples da instância do restaurante.
        """
        # BUG: o nome do restaurante estava errado
        # BUG: na mensagem havia "restaturante" quando deveria ser "restaurante"
        # BUG: na mensagem havia "and" quando deveria ser "e"
        # REFACTORY: compiladas mensagens dos prints para removê-las e adicionar a mensagem ao retorno da função
        return f"Esse restaurante chama {self.restaurant_name} serve {self.cuisine_type} e está servindo {self.number_served} consumidores desde que está aberto."

    def open_restaurant(self):
        """
        Retorna uma mensagem indicando que o restaurante está aberto para negócios.
        """
        # REFACTORY: retirado "else" porque é a última instrução a ser executada
        # REFACTORY: removido print para adicionar retorno da função
        # REFACTORY: alterado lugar de validação para quando estiver aberto, feedback rápido (logo no início da função)
        if self.open:
            return f"{self.restaurant_name} já está aberto!"

        # BUG: atributo que indica quando restaurante está aberto estava inicializando com False
        self.open = True
        # BUG: number_served estava inicializado com -2 quando deveria estar 0 quando abrir restaurante
        self.number_served = 0
        # REFACTORY: removido print para adicionar retorno a função
        return f"{self.restaurant_name} agora está aberto!"

    def close_restaurant(self):
        """
         Retorna uma mensagem indicando que o restaurante está fechado para negócios.
         """
        # REFACTORY: retirado "else" porque é a última instrução a ser executada
        # REFACTORY: removido print para adicionar retorno a função
        # REFACTORY: alterado lugar de validação para quando estiver fechado, feedback rápido (logo no início da função)
        if not self.open:
            return f"{self.restaurant_name} já está fechado!"

        self.open = False
        self.number_served = 0
        # REFACTORY: removido print para adicionar retorno a função
        return f"{self.restaurant_name} agora está fechado!"

    def set_number_served(self, total_customers):
        """
        Defina o número total de pessoas atendidas por este restaurante até o momento.
        """
        # REFACTORY: retirado "else" porque é a última instrução a ser executada
        # REFACTORY: removido print para adicionar retorno a função
        # REFACTORY: alterado lugar de validação para quando estiver fechado, feedback rápido (logo no início da função)
        if not self.open:
            return f"{self.restaurant_name} está fechado!"

        # MELHORIA: validação para números negativos
        if total_customers < self.QUANTIDADE_INVALIDA:
            return "Não pode alterar para valor negativo"

        self.number_served = total_customers
        # REFACTORY: adicionado return a função
        return f"Agora são {self.number_served} pessoas atendidas por {self.restaurant_name} até o momento!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        # REFACTORY: retirado "else" porque é a última instrução a ser executada
        # REFACTORY: removido print para adicionar retorno a função
        # REFACTORY: alterado lugar de validação para quando estiver fechado, feedback rápido (logo no início da função)
        if not self.open:
            return f"{self.restaurant_name} está fechado!"

        # MELHORIA: validação para números negativos
        if more_customers < self.QUANTIDADE_INVALIDA:
            return "Não pode incrementar valores negativos"

        # BUG: number_served não estava sendo incrementado. estava apenas alterando para valor do parâmetro
        self.number_served += more_customers
        # REFACTORY: adicionado return a função
        return f"Agora são {self.number_served} pessoas atendidas por {self.restaurant_name} até o momento!"
