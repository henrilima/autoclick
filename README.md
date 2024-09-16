# Mouse AutoClicker
O **Mouse AutoClicker** é um aplicativo simples feito em Python que simula cliques automáticos no mouse. Ele permite que o usuário defina a frequência dos cliques, o número de cliques por intervalo e o botão do mouse a ser usado (esquerdo ou direito). O projeto foi desenvolvido utilizando bibliotecas como `pyautogui`, `tkinter`, `keyboard` e `pillow`, e pode ser executado tanto em ambientes com Python instalado quanto em executáveis gerados via `cx_Freeze`.

## Releases
Para acessar a versão mais recente do aplicativo, visite a [página de releases](https://github.com/henrilima/autoclick/releases) do projeto. Lá você encontrará os arquivos ZIP para download e as notas de versão associadas.

## Funcionalidades
- Definir o intervalo entre os cliques (em milissegundos).
- Escolher quantos cliques devem ser feitos em cada intervalo.
- Selecionar qual botão do mouse será clicado (esquerdo ou direito).
- Ativar e desativar o autoclick com uma tecla personalizada.
- Interface gráfica simples e intuitiva criada com `tkinter`.

## Como usar
1. **Instalar dependências:**
   Se você estiver rodando o código diretamente em Python, antes de executar o projeto, certifique-se de instalar as dependências listadas no arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```
2. **Definir configurações:**
Você pode definir os intervalos, o número de cliques e o botão do mouse editando manualmente o arquivo `settings.json` ou configurando diretamente pela interface gráfica.

3. **Executar o projeto:**
Execute o arquivo `main.py` para iniciar o aplicativo:
```bash
python main.py
```

## Geração do Executável com `cx_Freeze`
Se você quiser rodar o aplicativo em máquinas que não tenham o Python instalado, pode gerar um executável usando o `cx_Freeze`.

### Como gerar o executável:
1. **Instalar o `cx_Freeze`:**
Certifique-se de que o `cx_Freeze` está instalado no seu ambiente virtual:

```bash
pip install cx_Freeze
```

2. **Rodar o script de build:**
Após configurar o `setup.py`, você pode rodar o comando:

```bash
python setup.py build
```

Isso irá gerar uma pasta `build` contendo o executável.

### Limitações do `cx_Freeze`
Embora o `cx_Freeze` facilite a geração de executáveis para sistemas que não possuem o Python instalado, há algumas limitações:
- **Bibliotecas gráficas:** Bibliotecas que utilizam interfaces gráficas como o `tkinter` podem exigir a configuração correta das variáveis de ambiente `TCL_LIBRARY` e `TK_LIBRARY` para que as dependências de `tkinter` sejam encontradas corretamente.
- **Tamanho do executável:** O executável gerado pode ser grande, uma vez que inclui todos os módulos do Python necessários para rodar o programa de forma independente.

## Contribuição
Se você quiser contribuir com este projeto, fique à vontade para abrir um _pull request_ ou reportar _issues_ na seção de _issues_ do repositório.

## Licença
Este projeto está licenciado sob a licença Apache-2.0. Veja o arquivo `LICENSE` para mais detalhes.
