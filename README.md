# Projeto de Busca de Endereços com ViaCEP

Este projeto consiste em uma aplicação Python para buscar informações de endereços e CEPs utilizando a API do ViaCEP. A aplicação é organizada em classes que facilitam a busca e validação de dados de CEPs e logradouros (ruas, avenidas, etc.) em qualquer cidade do Brasil.

## Funcionalidades

- **Busca de CEP**: A partir de um CEP fornecido, a aplicação consulta a API do ViaCEP e retorna os dados associados ao CEP, como logradouro, bairro, cidade e estado.
- **Busca de Logradouro**: A partir de uma combinação de estado (UF), cidade e logradouro, a aplicação consulta a API do ViaCEP e retorna uma lista de endereços que correspondem aos critérios fornecidos.
- **Validação de Requisições**: Verifica se as requisições HTTP foram bem-sucedidas e levanta exceções em caso de erros.
- **Formatação e Validação de Dados**: Formata os CEPs e verifica se os dados fornecidos são válidos antes de realizar as consultas.

## Estrutura do Projeto

- `Requisicao`: Classe que valida o resultado das requisições HTTP.
- `CEP`: Classe que realiza a formatação, validação e busca de informações de um CEP específico.
- `Endereco`: Classe que realiza a busca de logradouros a partir de UF, cidade e logradouro.

## Como Usar

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/OtavMacedo/busca_enderecos.git
    ```

2. **Instale as dependências:**

    Certifique-se de ter o Python instalado em sua máquina e instale a biblioteca `requests`:

    ```bash
    pip install requests
    ```

3. **Execute a aplicação:**

    Você pode usar as classes diretamente em seu script Python:

    ```python
    from busca_enderecos import CEP, Endereco

    # Exemplo de busca por CEP
    cep = CEP('01001000')
    print(cep.dados)

    # Exemplo de busca por Endereço
    endereco = Endereco('SP', 'Sao Paulo', 'Avenida Paulista')
    endereco.imprime_dados_enderecos()
    ```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Para dúvidas ou sugestões, entre em contato pelo e-mail: otavmacedo04@gmail.com
