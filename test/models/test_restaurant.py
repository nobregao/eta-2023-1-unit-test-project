from src.models.restaurant import Restaurant


class TestRestaurant:

    restaurant_name = "Ristorante Renatao"
    cuisine_type = "cozinha italiana"

    def test_describe_restaurant(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)

        expected_result = f"Esse restaurante chama {self.restaurant_name} serve {self.cuisine_type} e está servindo 0 consumidores desde que está aberto."

        result = restaurant.describe_restaurant()

        assert result == expected_result

    def test_open_restaurant_fechado(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)

        expected_result = f"{self.restaurant_name} agora está aberto!"

        assert restaurant.open_restaurant() == expected_result
        assert restaurant.open
        assert restaurant.number_served == 0

    def test_open_restaurant_aberto(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        restaurant.open_restaurant()

        expected_result = f"{self.restaurant_name} já está aberto!"

        assert restaurant.open_restaurant() == expected_result
        assert restaurant.open

    def test_close_restaurant_fechado(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        restaurant.open_restaurant()

        expected_result = f"{self.restaurant_name} agora está fechado!"

        assert restaurant.close_restaurant() == expected_result
        assert restaurant.open is False
        assert restaurant.number_served == 0

    def test_close_restaurant_aberto(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        restaurant.close_restaurant()

        expected_result = f"{self.restaurant_name} já está fechado!"

        assert restaurant.close_restaurant() == expected_result
        assert restaurant.open is False
        assert restaurant.number_served == 0

    def test_set_number_served_restaurante_aberto(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        restaurant.open_restaurant()

        PESSOAS_ATENDIDAS = 2

        expected_result = f"Agora são {PESSOAS_ATENDIDAS} pessoas atendidas por {self.restaurant_name} até o momento!"

        assert restaurant.set_number_served(PESSOAS_ATENDIDAS) == expected_result
        assert restaurant.number_served == PESSOAS_ATENDIDAS

    def test_set_number_served_restaurante_fechado(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)

        PESSOAS_ATENDIDAS = 0

        expected_result = f"{self.restaurant_name} está fechado!"

        assert restaurant.set_number_served(PESSOAS_ATENDIDAS) == expected_result
        assert restaurant.number_served == PESSOAS_ATENDIDAS

    def test_increment_number_served_restaurante_aberto(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        restaurant.open_restaurant()

        PESSOAS_ATENDIDAS = 2
        restaurant.set_number_served(PESSOAS_ATENDIDAS)

        PESSOAS_ESPERADAS_ATENDIDAS = 4

        expected_result = f"Agora são {PESSOAS_ESPERADAS_ATENDIDAS} pessoas atendidas por {self.restaurant_name} até o momento!"

        assert restaurant.increment_number_served(PESSOAS_ATENDIDAS) == expected_result
        assert restaurant.number_served == PESSOAS_ESPERADAS_ATENDIDAS

    def test_increment_number_served_restaurante_fechado(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)

        PESSOAS_ATENDIDAS = 2

        expected_result = f"{self.restaurant_name} está fechado!"

        assert restaurant.increment_number_served(PESSOAS_ATENDIDAS) == expected_result

    def test_increment_number_served_valor_negativo(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        restaurant.open_restaurant()

        PESSOAS_ATENDIDAS = 2
        restaurant.set_number_served(PESSOAS_ATENDIDAS)

        expected_result = "Não pode incrementar valores negativos"

        VALOR_INVALIDO = -2
        assert restaurant.increment_number_served(VALOR_INVALIDO) == expected_result
        assert restaurant.number_served == PESSOAS_ATENDIDAS
