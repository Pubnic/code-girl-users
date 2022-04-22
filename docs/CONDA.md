# Instalando o Conda

Aqui veremos como instalar o gerenciador de ambientes python Conda.

## Motivação

Hoje temos várias versões do python e cada projeto nasce utilizando alguma versão em específico, sendo que algumas bibliotecas não terão compatibilidade com versões anteriores ou superiores.

Além disso, cada projeto também possui versões específicas de cada biblioteca, o que torna uma chateação quando trabalhamos com muito projetos em paralelo.

O Conda é uma das ferramentas que nos possibilidade isolar nosso ambiente para cada projeto, sendo esse ambiente com uma versão de Python específica e suas bibliotecas instaladas, de modo isolado à não afetar outros projetos com versões diferentes.

## Instalando
O conda, no momento somente tem disponibilizado seu instalador para versões do python `3.7`, `3.8` e `3.9`. Caso tenha uma versão maior do que essa, pode consultar a página de instalação do miniconda e verificar se já foi disponibilizado para uma versão maior: https://docs.conda.io/en/latest/miniconda.html

### Linux
- Verifique a versão do python no terminal `python --version` 
- Escolha um dos instaladores adequados a sua versão
	- [Python 3.9](https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-x86_64.sh)
	- [Python 3.8](https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-Linux-x86_64.sh)
	-	[Python 3.7](https://repo.anaconda.com/miniconda/Miniconda3-py37_4.11.0-Linux-x86_64.sh)
- Após baixar, rode um dos comando a depender da versão baixada
	- Python 3.9: `bash Miniconda3-py39_4.11.0-Linux-x86_64.sh`
	- Python 3.8: `bash Miniconda3-py38_4.11.0-Linux-x86_64.sh`
	- Python 3.7: `bash Miniconda3-py37_4.11.0-Linux-x86_64.sh`
- Aperter enter até aparecer o pedido de confirmação e digite `yes`
- Caso peça para iniciar automaticamente, digite `yes`
- Após instalado, feche seu terminal e abra novamente, aparecerá no início do seu terminal a palavra `(base)` entre parênteses, isso significa que foi instalado e agora ele está no ambiente padrão.

### MacOS
- Verifique a versão do python no terminal `python --version` 
- Escolha um dos instaladores adequados a sua versão
	- [Python 3.9](https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-MacOSX-x86_64.sh)
	- [Python 3.8](https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-MacOSX-x86_64.sh)
	-	[Python 3.7](https://repo.anaconda.com/miniconda/Miniconda3-py37_4.11.0-MacOSX-x86_64.sh)
- Após baixar, rode um dos comando a depender da versão baixada
	- Python 3.9: `bash Miniconda3-py39_4.11.0-MacOSX-x86_64.sh`
	- Python 3.8: `bash Miniconda3-py38_4.11.0-MacOSX-x86_64.sh`
	- Python 3.7: `bash Miniconda3-py37_4.11.0-MacOSX-x86_64.sh`
- Aperter enter até aparecer o pedido de confirmação e digite `yes`
- Caso peça para iniciar automaticamente, digite `yes`
- Após instalado, feche seu terminal e abra novamente, aparecerá no início do seu terminal a palavra `(base)` entre parênteses, isso significa que foi instalado e agora ele está no ambiente padrão.
