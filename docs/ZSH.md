# Instalando o terminal Oh My ZSH

> Caso você esteja utilizando Windows, lamento informar que não possuímos instruções para instalar esse terminal nele, nós recomendamos que você utilize para todo o curso um sistema operacional Linux ou MacOS
{.is-warning}

## Instalando o ZSH

### Linux
- Rode o comando 
	```
  sudo apt install zsh
  ```
- Confirme a instalação 
	```
  zsh --version
  ```
- Torne ele seu terminal padrão 
	```
  chsh -s $(which zsh)
  ```
- Será necessário reiniciar ou deslogar da sessão para ser aplicado.
- Após, abra o terminal e verifique que ele mudou :D
> Caso ainda tenha problemas, confira alguns links de ajuda no Google [clicando aqui](https://www.google.com/search?q=zsh+default+without+chsh)
{.is-info}


### MacOS
- Rode o comando 
	```
  brew install zsh
  ```
- Confirme a instalação 
	```
	zsh --version
  ```
- Torne ele seu terminal padrão 
	```
  sudo sh -c "echo $(which zsh) >> /etc/shells"` depois `chsh -s $(which zsh)
  ```
- Feche o terminal e abra novamente, deverá aparecer algumas instruções para configurar
	- **Digite `1`** - Continue to the main menu.
		- **Digite `0`** - para finalizar

## Instalando o Oh My ZSH
- Execute o comando
  ```sh
  sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
  ```
> Caso dê um erro informando que você não possui `curl`, basta instalar e rodar o comando novamente. **Linux:** `sudo apt install curl` **MacOS:** `brew install curl`
{.is-info}
- Abra o terminal e veja que ele mudou :D
> No terminal antigo, utilizávamos o `~/.bash_profile` ou `~/.profile` para as configurações do terminal, agora com o ZSH, utilizaremos sempre o `~/.bashrc`
{.is-warning}

## (Opcional) Tema Dracula

### Linux
- Para instalar, basta acessar o site https://draculatheme.com/gnome-terminal e seguir as instruções
> Aqui é considerado que você já possui o `git` instalado, caso não possua rode `sudo apt install git`
{.is-info}

### MacOS
- Baixe o terminal [clicando aqui](https://github.com/dracula/terminal-app/archive/master.zip)
- Descompacte
- No terminal clique em `Preferências` --> `Temas` --> Seleciona `Dracula` caso já exista.
- Caso não, clique em `+` --> Vá na pasta descompactada --> Selecione o arquivo `Dracula.terminal` --> Selecione o tema `Dracula`

## Tema Spaceship
Esse tema modificará as informações que são exibidas no terminal, permitindo a gente visualizar várias informações a depender da pasta em que estamos.

### Fonte FiraCode

- Esse tema utiliza a fonte `Fira Code`, vamos instala-la baixando o zip [clicando aqui](https://github.com/tonsky/FiraCode/releases/download/6.2/Fira_Code_v6.2.zip)
- Descompacte o zip --> entre na pasta de `TTF` --> clique duas vezes no arquivo `Retina` --> Aparecerá um botão para instalar
- Agora no terminal --> vá em preferências --> Texto -> Fonte -> Trocar fonte -> Escolha `Retina` e o tamanho que melhor lhe agradar, normalmente utilizo `14`

### Instalando
- Primeiro vamos clonar o repositório do Spaceship 
	```
  git clone https://github.com/denysdovhan/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt"
  ```
- Agora vamos criar um "atalho" na pasta de temas do **Oh My ZSH** 
	```
  ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"
  ```
- Vamos no arquivo de configuração do ZSH e modificar o tema
	- `code ~/.zshrc`
	- Procuro por `ZSH_THEME` e deixe assim `ZSH_THEME="spaceship"`
- Feche o terminal e abra novamente, verá que ele mudou :D

### Configurando
- Vamos abrir o `code ~/.zshrc`
- No final do arquivo, cole
  ```sh
  SPACESHIP_PROMPT_ORDER=(
    user          # Username section
    dir           # Current directory section
    host          # Hostname section
    git           # Git section (git_branch + git_status)
    hg            # Mercurial section (hg_branch  + hg_status)
    exec_time     # Execution time
    line_sep      # Line break
    vi_mode       # Vi-mode indicator
    jobs          # Background jobs indicator
    exit_code     # Exit code section
    char          # Prompt character
  )
  SPACESHIP_USER_SHOW=always
  SPACESHIP_PROMPT_ADD_NEWLINE=false
  SPACESHIP_CHAR_SYMBOL="❯"
  SPACESHIP_CHAR_SUFFIX=" "
  ```
- Feche o terminal e abra novamente, verá que mudou :D

## Adicionando alguns plugins

### Instalando o ZI
- Cole no terminal 
	```
  sh -c "$(curl -fsSL https://git.io/get-zi)" -- -i skip -b v1.0.0
  ```
- Cole no terminal
  ```sh
  # Will add minimal configuration
  sh -c "$(curl -fsSL https://git.io/get-zi)" --
  # Non interactive. Just clone or update repository.
  sh -c "$(curl -fsSL https://git.io/get-zi)" -- -i skip
  # Minimal configuration + annexes.
  sh -c "$(curl -fsSL https://git.io/get-zi)" -- -a annex
  # Minimal configuration + annexes + zunit.
  sh -c "$(curl -fsSL https://git.io/get-zi)" -- -a zunit
  # Minimal configuration with loader
  sh -c "$(curl -fsSL https://git.io/get-zi)" -- -a loader
  # Suggest your .zshrc configuration to:
  # https://github.com/z-shell/playground
  sh -c "$(curl -fsSL https://git.io/get-zi)" -- -a ???
  ```
- Feche e abra o terminal
- Execute `zi self-update`

### Adicionando os plugins

#### Adicionando zdharma/fast-syntax-highlighting
Adiciona syntax highlighting na hora da escrita de comandos que facilita principalmente em reconhecer comandos que foram digitados de forma incorreta;

#### Adicionando zsh-users/zsh-autosuggestions
Sugere comandos baseados no histórico de execução conforme você vai digitando;

#### Adicionando zsh-users/zsh-completions
Adiciona milhares de completitions para ferramentas comuns como Yarn, Homebrew, NVM, Node, etc, para você precisar apenas apertar TAB para completar comandos;

- Abra o arquivo de configuração do terminal `code ~/.zshrc` e no final cole as seguintes linhas
  ```sh
  # ZI Control
  zi light zdharma/fast-syntax-highlighting
  zi light zsh-users/zsh-autosuggestions
  zi light zsh-users/zsh-completions
  ```

## Configurando o VSCode
Vamos configurar o VSCode para utilizar o zsh por padrão

### Linux
- No VSCode, digite `ctrl + shift + p`
- Escreva **settings** e clique `ENTER`
- No final do arquivo cole `"terminal.integrated.defaultProfile.linux": "/bin/zsh"`

### MacOS
- No VSCode, digite `cmd + shift + p`
- Escreva **settings** e clique `ENTER`
- No final do arquivo cole `"terminal.integrated.defaultProfile.osx": "zsh"`
  