import os
from homework.pregunta_01 import pregunta_01  # <- aquí está el cambio

def test_01():
    pregunta_01()
    assert os.path.exists("files/plots/news.png"), "No se generó el archivo news.png"
  