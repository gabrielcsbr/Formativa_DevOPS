import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from calculadora import Calculadora


import pytest
from calculadora import Calculadora

@pytest.fixture
def calc():
    return Calculadora()

def test_soma_inteiros(calc):
    assert calc.soma(2, 3) == 5

def test_subtracao_inteiros(calc):
    assert calc.subtracao(10, 6) == 4

def test_multiplicacao_inteiros(calc):
    assert calc.multiplicacao(7, 5) == 35

def test_divisao_inteiros(calc):
    assert calc.divisao(20, 4) == 5

def test_divisao_por_zero_gera_erro(calc):
    with pytest.raises(ValueError):
        calc.divisao(10, 0)

# Extra: checagem com decimais (tolerância de ponto flutuante)
def test_operacoes_decimais(calc):
    assert calc.soma(0.1, 0.2) == pytest.approx(0.3, rel=1e-9, abs=1e-12)
    assert calc.multiplicacao(0.1, 0.2) == pytest.approx(0.02, rel=1e-9, abs=1e-12)

# Extra: valores negativos
def test_operacoes_com_negativos(calc):
    assert calc.subtracao(-5, -2) == -3
    assert calc.multiplicacao(-3, 4) == -12
    assert calc.divisao(-9, 3) == -3
