class Restaurant:
    """Model de restaurante simples."""

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
        if not self.open:
            # BUG: atributo que indica quando restaurante está aberto estava inicializando com False
            self.open = True
            # BUG: number_served estava inicializado com -2 quando deveria estar zero quando abrir restaurante
            self.number_served = 0
            # REFACTORY: removido print para adicionar retorno a função
            return f"{self.restaurant_name} agora está aberto!"

        # REFACTORY: retirado "else" porque é a única instrução a ser executada
        # REFACTORY: removido print para adicionar retorno da função
        return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """
         Retorna uma mensagem indicando que o restaurante está fechado para negócios.
         """
        if self.open:
            self.open = False
            self.number_served = 0
            # REFACTORY: removido print para adicionar retorno a função
            return f"{self.restaurant_name} agora está fechado!"

        # REFACTORY: retirado "else" porque é a única instrução a ser executada
        # REFACTORY: removido print para adicionar retorno a função
        return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """
        Defina o número total de pessoas atendidas por este restaurante até o momento.
        """
        if self.open:
            self.number_served = total_customers
            # REFACTORY: adicionado return a função
            return f"Agora são {self.number_served} pessoas atendidas por {self.restaurant_name} até o momento!"

        # REFACTORY: retirado "else" porque é a única instrução a ser executada
        # REFACTORY: removido print para adicionar retorno a função
        return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            # BUG: number_served estava sendo alterado e não incrementado com o parâmetro da função
            self.number_served += more_customers
            # REFACTORY: adicionado return a função
            return f"Agora são {self.number_served} pessoas atendidas por {self.restaurant_name} até o momento!"

        # REFACTORY: retirado "else" porque é a única instrução a ser executada
        # REFACTORY: removido print para adicionar retorno a função
        return f"{self.restaurant_name} está fechado!"
