# Otimiza
Repositório do projeto desenvolvido durante a segunda verificação de aprendizagem da disciplina Tópicos em Otimização 2019.2 do Bacharelado em Sistemas de Informação da Universidade Federal Rural de Pernambuco.

## Instalação e configuração do projeto

### Criando um ambiente no Windows
Se não tiver um ambiente virtual instalado, continue no método VENV, caso contrário utilize o que você tiver disponível e passe para o passo de instalação. Se você preferir por não utilizar o ambiente virtual, então siga para a instalação.

#### Método VENV
Instalando o virtualenv

    pip install virtualenv

iniciando o virtualenv

    virtualenv venv

Ativando o ambiente virtual

    venv\Scripts\activate

Para desativar o ambiente virtual

    deactivate

### Criando um ambiente no Linux
Se não tiver um ambiente virtual instalado, continue no método VENV, caso contrário utilize o que você tiver disponível e passe para o passo de instalação. Se você preferir por não utilizar o ambiente virtual, então siga para a instalação.

#### Método VENV
Instalando o virtualenv

    pip install virtualenv

iniciando o virtualenv

    virtualenv venv

Ativando o ambiente virtual

    source venv/bin/activate

Para desativar o ambiente virtual

    deactivate

### Instalação
Utilize o seguinte comando para instalar no ambiente virtual os pacotes necessários para rodar o projeto.

    pip install -r requirements.txt

### Iniciando o projeto

    python run.py