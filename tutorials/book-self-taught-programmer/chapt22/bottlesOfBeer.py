def bottlesOfBeer(bob):
    """
    Печатает текст песенки про 99 бутылок пива.
    :param bob: должно быть целым числом
    """
    if bob < 1:
        print("""Нет бутылок пива на стене. Нет бутылок пива.""")
        return
    tmp = bob
    bob -= 1
    print(f"""{tmp} бутылок пива на стене. {tmp} бутылок пива. 
            Возьми одну, пусти по кругу, {bob} бутылок пива на стене""")
    bottlesOfBeer(bob)

bottlesOfBeer(99)