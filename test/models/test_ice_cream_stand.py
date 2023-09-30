from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:
    restaurant_name = "Gelatos do Nordeste"
    cuisine_type = "sorvete de sabores nordestinos"
    flavors_list = [
        "Açaí",
        "Manga Rosa",
        "Pitanga",
        "Goiaba Vermelha",
        "Seriguela",
        "Rapadura",
        "Tapioca",
        "Bolo de Rolo",
        "Pamonha",
        "Beiju de Tapioca"
    ]

    def test_flavors_formated_list(self):
        ice_cream_stand = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavors_list)

        expected_result = \
            f""" - Açaí,
 - Manga Rosa,
 - Pitanga,
 - Goiaba Vermelha,
 - Seriguela,
 - Rapadura,
 - Tapioca,
 - Bolo de Rolo,
 - Pamonha,
 - Beiju de Tapioca"""

        assert ice_cream_stand.flavors_formated_list() == expected_result

    def test_flavors_available_com_estoque(self):
        ice_cream_stand = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavors_list)

        expected_result = \
            f"""No momento temos os seguintes sabores de sorvete disponíveis: 
 - Açaí,
 - Manga Rosa,
 - Pitanga,
 - Goiaba Vermelha,
 - Seriguela,
 - Rapadura,
 - Tapioca,
 - Bolo de Rolo,
 - Pamonha,
 - Beiju de Tapioca"""

        assert ice_cream_stand.flavors_available() == expected_result

    def test_flavors_available_sem_estoque(self):
        ice_cream_stand = IceCreamStand(self.restaurant_name, self.cuisine_type, [])

        expected_result = "Estamos sem estoque atualmente!"

        assert ice_cream_stand.flavors_available() == expected_result

    def test_find_flavor_com_estoque_tem_sabor(self):
        ice_cream_stand = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavors_list)

        assert ice_cream_stand.find_flavor("Manga Rosa") == "Temos no momento Manga Rosa!"

    def test_find_flavor_com_estoque_nao_tem_sabor(self):
        ice_cream_stand = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavors_list)

        assert ice_cream_stand.find_flavor("Milho Verde") == "Não temos no momento Milho Verde!"

    def test_find_flavor_sem_estoque(self):
        ice_cream_stand = IceCreamStand(self.restaurant_name, self.cuisine_type, [])

        assert ice_cream_stand.find_flavor("Pamonha") == "Estamos sem estoque atualmente!"

    def test_add_flavor_invalido(self):
        ice_cream_stand = IceCreamStand(self.restaurant_name, self.cuisine_type, [])

        assert ice_cream_stand.add_flavor("") == "Sabor inválido!"

    def test_add_flavor_valido(self):
        ice_cream_stand = IceCreamStand(self.restaurant_name, self.cuisine_type, [])

        assert ice_cream_stand.add_flavor("Pamonha") == "Pamonha adicionado ao estoque!"

    def test_add_flavor_ja_existe(self):
        ice_cream_stand = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavors_list)

        assert ice_cream_stand.add_flavor("Manga Rosa") == "Sabor já disponível!"