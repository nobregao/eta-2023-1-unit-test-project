from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    CAMPO_VAZIO = SEM_ESTOQUE = 0

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    # REFACTORY: criada função para formatação da lista de sabores
    def flavors_formated_list(self):
        flavor_concatenado = ""
        for index, flavor in enumerate(self.flavors):
            if index == len(self.flavors) - 1:
                flavor_concatenado += f" - {flavor}"
            else:
                flavor_concatenado += f" - {flavor},\n"

        return flavor_concatenado

    def flavors_available(self):
        """
        Percorra a lista de sabores disponíveis e retorne.
        """
        # REFACTORY: retirado "else" porque é a última instrução a ser executada
        # REFACTORY: removido print para adicionar retorno a função
        # REFACTORY: alterado lugar do retorno que seria do último else para ter feedback rápido (fail first)
        if len(self.flavors) == self.SEM_ESTOQUE:
            return "Estamos sem estoque atualmente!"

        # REFACTORY: alterado local de formatação da lista para uma função
        flavor_concatenado = self.flavors_formated_list()

        # REFACTORY: removido print para adicionar retorno a função
        return f"No momento temos os seguintes sabores de sorvete disponíveis: \n{flavor_concatenado}"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        # REFACTORY: retirado último "else" porque é a última instrução a ser executada
        # REFACTORY: removido print para adicionar retorno a função
        # REFACTORY: alterado lugar do retorno que seria do último else para ter feedback rápido (fail first)
        if len(self.flavors) == self.SEM_ESTOQUE:
            return "Estamos sem estoque atualmente!"

        if flavor in self.flavors:
            # BUG: está retornando todos os sabores. deveria retornar o flavor do parâmetro
            # REFACTORY: removido print para adicionar retorno a função
            return f"Temos no momento {flavor}!"
        else:
            # BUG: está retornando todos os sabores. deveria retornar o flavor do parâmetro
            # REFACTORY: removido print para adicionar retorno a função
            return f"Não temos no momento {flavor}!"

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        # REFACTORY: removida validação inicial de estoque para ser posssível adicionar,
        # caso não tenha nenhum estoque de sabores

        # MELHORIA: validação para caso sabor adicionado seja inválido
        if len(flavor) == self.CAMPO_VAZIO:
            return "Sabor inválido!"

        if flavor in self.flavors:
            # REFACTORY: removido print para adicionar retorno a função
            return f"Sabor já disponível!"
        else:
            self.flavors.append(flavor)
            # REFACTORY: removido print para adicionar retorno a função
            return f"{flavor} adicionado ao estoque!"

