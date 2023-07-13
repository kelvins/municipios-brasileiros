import requests
import pandas as pd
import os
import pytest

class BaixaBiomas:
    def baixar_arquivo(self, url, destino):
        try:
            response = requests.get(url)
            response.raise_for_status()

            with open(destino, "wb") as file:
                file.write(response.content)

            print("Download concluído com sucesso.")

            # Carrega o arquivo XLS como um DataFrame
            dataframe = pd.read_excel(destino)

            return dataframe

        except requests.exceptions.RequestException as err:
            print(f"Falha ao baixar o arquivo: {err}")
            return None


def processar_municipios():
    # Leitura do arquivo "municipios.csv" e criação do DataFrame
    municipios_df = pd.read_csv("/Users/lucasrodrigues/Documents/projetos/Municipios-Brasileiros/csv/municipios.csv")

    # Chamar a função baixar_arquivo para obter o DataFrame com os biomas
    url = "https://geoftp.ibge.gov.br/informacoes_ambientais/estudos_ambientais/biomas/documentos/Lista_Municipio_Bioma_250mil.xls"
    destino = "biomas.xls"

    downloader = BaixaBiomas()
    biomas_df = downloader.baixar_arquivo(url, destino)

    # Verificar se o DataFrame dos biomas foi criado com sucesso
    if biomas_df is not None:
        # Remover duplicatas da coluna "NM_MUNICIP" no DataFrame dos biomas
        biomas_df.drop_duplicates(subset="NM_MUNICIP", inplace=True)

        # Comparar as colunas "nome" e "NM_MUNICIP" para adicionar a coluna "BIOMA"
        municipios_df["BIOMA"] = municipios_df["codigo_ibge"].map(biomas_df.set_index("CD_GEOCMU")["BIOMA"])

    # Sobrescrever o arquivo municipios.csv com o DataFrame atualizado
    municipios_df.to_csv("/Users/lucasrodrigues/Documents/projetos/Municipios-Brasileiros/csv/municipios.csv", index=False)

    print(municipios_df['BIOMA'])

    # Remove o arquivo após processar os biomas
    os.remove(destino)

    return municipios_df


class TestDownloadArquivo:
    def test_baixar_arquivo(self):
        url = "https://geoftp.ibge.gov.br/informacoes_ambientais/estudos_ambientais/biomas/documentos/Lista_Municipio_Bioma_250mil.xls"
        destino = "biomas.xls"

        downloader = BaixaBiomas()

        # Realiza o download do arquivo
        resultado = downloader.baixar_arquivo(url, destino)

        # Verifica se o arquivo foi baixado com sucesso
        assert resultado is not None

        # Verifica se o arquivo existe no local de destino
        assert os.path.exists(destino) == True

        # Verifica se o arquivo não está vazio
        assert os.path.getsize(destino) > 0

        # Remove o arquivo após o teste
        os.remove(destino)

    def test_baixar_arquivo_retorna_dataframe(self):
        url = "https://geoftp.ibge.gov.br/informacoes_ambientais/estudos_ambientais/biomas/documentos/Lista_Municipio_Bioma_250mil.xls"
        destino = "biomas.xls"

        downloader = BaixaBiomas()
        dataframe = downloader.baixar_arquivo(url, destino)

        assert isinstance(dataframe, pd.DataFrame)

        # Remove o arquivo após o teste
        if dataframe is not None:
            os.remove(destino)

def test_municipios_csv_coluna_bioma():
    # Obter o diretório do script atual
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    # Montar o caminho relativo do arquivo municipios.csv
    caminho_csv = os.path.join(diretorio_atual, "..", "csv", "municipios.csv")

    # Verificar se o arquivo municipios.csv existe
    assert os.path.exists(caminho_csv)

    # Ler o arquivo municipios.csv como DataFrame
    municipios_df = pd.read_csv(caminho_csv)

    # Verificar se a coluna "BIOMA" está presente no DataFrame
    assert 'BIOMA' in municipios_df.columns

#Para executar o metodo principal

#processar_municipios()

# Executar o testes

pytest.main(["-v"])