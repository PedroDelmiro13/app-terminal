from app.main import gritar_texto, inverter_texto


def test_operacoes_do_texto_magico() -> None:
    assert inverter_texto("abc") == "cba"
    assert gritar_texto("oi") == "OI!!!"
