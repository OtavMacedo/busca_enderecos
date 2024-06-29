import requests


class Requisicao:

    @staticmethod
    def valida_requisicao(requisicao: requests.Response,
                          tipo_busca: str
    ) -> None:
        """
        Valida o resultado da requisição HTTP.

        Args:
            requisicao (requests.Response): A resposta da requisição HTTP.
            tipo_busca (str): O tipo de busca realizado (por exemplo, 'CEP' ou 
            'endereço').

        Raises:
            ValueError: Se o status da requisição for 400, indicando formato 
            inválido.
            Exception: Se ocorrer um erro desconhecido.
        """
        if requisicao.status_code == 200:
            print(f'Busca de {tipo_busca} realizada')
        elif requisicao.status_code == 400:
            raise ValueError(f'Formato de {tipo_busca} inválido')
        else:
            raise Exception('Erro desconhecido')
        

class CEP:
    def __init__(self, cep: int | str):
        """
        Inicializa a instância com um CEP formatado.

        Args:
            cep (int | str): O CEP a ser buscado.
        """
        self._cep = self._formata_cep(cep)
        self.dados = self._busca_cep()
    
    def _busca_cep(self) -> dict:
        """
        Realiza a busca do CEP e retorna os dados.

        Returns:
            dict: Os dados referentes ao CEP buscado.

        Raises:
            Exception: Se ocorrer um erro na requisição.
        """
        URL_REQUISICAO = f'https://viacep.com.br/ws/{self._cep}/json/'
        try:
            requisicao = requests.get(URL_REQUISICAO)
        except requests.RequestException as error:
            raise Exception(f'Erro na requisição: {error}')
        Requisicao.valida_requisicao(requisicao, 'CEP')
        dados = requisicao.json()
        self._valida_dados_cep(dados)
        return dados
    
    def _formata_cep(self, cep: int | str) -> str:
        """
        Formata o CEP removendo espaços e hífens e convertendo para string.

        Args:
            cep (int | str): O CEP a ser formatado.

        Returns:
            str: O CEP formatado.
        """
        if not isinstance(cep, str):
            cep = str(cep)
        cep = cep.replace(' ', '').replace('-', '')
        self._valida_cep_entrada(cep)
        return cep
    
    def _valida_cep_entrada(self, cep):
        """
        Valida se o CEP não está vazio e se possui o formato correto.

        Args:
            cep (str): O CEP a ser validado.

        Raises:
            ValueError: Se o CEP for vazio ou inválido.
        """
        if len(cep) == 0:
            raise ValueError('Campo vazio')
        if len(cep) != 8 or not cep.isdigit():
            raise ValueError('CEP inválido')
        
    def _valida_dados_cep(self, dados: dict):
        """
        Verifica se o CEP fornecido existe.

        Args:
            dados (dict): Os dados retornados pela requisição do CEP.

        Raises:
            ValueError: Se o CEP não for encontrado.
        """
        if 'erro' in dados:
            raise ValueError('CEP não encontrado')
        

class Endereco:
    def __init__(self, uf: str, cidade: str, logradouro: str):
        """
        Inicializa a instância com UF, cidade e logradouro.

        Args:
            uf (str): A unidade federativa (estado) do endereço - Exemplo: MG.
            cidade (str): A cidade do endereço.
            logradouro (str): O logradouro (rua, avenida, etc.) do endereço.
        """
        self._uf = uf
        self._cidade = cidade
        self._logradouro = logradouro
        self.dados = self._busca_logradouro()
        
    def _busca_logradouro(self) -> list:
        """
        Realiza a busca pelo logradouro e retorna os dados.

        Returns:
            list: Os dados dos endereços correspondentes ao logradouro buscado.

        Raises:
            Exception: Se ocorrer um erro na requisição.
        """
        URL_REQUISICAO = f'https://viacep.com.br/ws/{self._uf}/{self._cidade}/'\
            f'{self._logradouro}/json/'
        try:
            requisicao = requests.get(URL_REQUISICAO)
        except requests.RequestException as error:
            raise Exception(f'Erro na requisição: {error}')
        Requisicao.valida_requisicao(requisicao, 'endereço')
        dados = requisicao.json()
        self._valida_dados_endereco(dados)
        return dados
    
    def _valida_dados_endereco(self, dados: list):
        """
        Verifica se o endereço fornecido existe.

        Args:
            dados (list): Os dados retornados pela requisição do logradouro.

        Raises:
            ValueError: Se nenhum endereço for encontrado.
        """
        quantidade_enderecos = len(dados)
        if quantidade_enderecos == 0:
            raise ValueError('Endereço não encontrado')
        
    def imprime_dados_enderecos(self):
        """
        Imprime os dados dos endereços encontrados.
        """
        quantidade_enderecos = len(self.dados)
        palavra_endereco = \
            'endereço' if quantidade_enderecos == 1 else 'endereços'
        
        print(f'{quantidade_enderecos} {palavra_endereco} encontrado(s)')
        for indice, dict_endereco in enumerate(self.dados, 1):
                print(f'Endereço {indice}: {dict_endereco}')
