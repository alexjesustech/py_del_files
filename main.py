import os


def excluir_arquivos(pasta, extensao):
    """Exclui arquivos XMP na pasta especificada e suas subpastas."""

    print(pasta)
    for item in os.listdir(pasta):
        item_caminho = os.path.join(pasta, item)

        if os.path.isfile(item_caminho) and item_caminho.endswith(extensao):
            print(item_caminho)
            os.remove(item_caminho)
        elif os.path.isdir(item_caminho):
            print(item_caminho)
            excluir_arquivos(item_caminho, extensao)  # Chama a função recursivamente para subpastas


if __name__ == "__main__":
    pasta_imagens = os.path.join(os.path.expanduser("~"), "OneDrive\\Imagens")
    # print(pasta_imagens)
    excluir_arquivos(pasta_imagens, ".xmp")
