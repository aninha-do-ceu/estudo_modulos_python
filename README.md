# estudo_modulos_python

## Objetivo
<br>Estudo de disponibilização de funções em módulos, bibliotecas, etc, em formato whl</br>

## Importação e instalação de Módulos
<br>Baixar o wheel file e acessar o diretório usando o comando (no terminal):</br>

~~~shell
cd C:\users\{seu_usuario}\Downloads

pip install Estudo_modulo-0.1-py3-none-any.whl
~~~

<br>Certifique-se que o módulo foi instalado corretamente:</br>

~~~shell
pip list
~~~

<br>A partir, pode-se utilizar o módulo importando-o</br>

~~~python
from pacote_calculadora import Calculadora

calc = Calculadora

print(calc.soma(1,2))
print(calc.subtracao(1,2))
~~~
