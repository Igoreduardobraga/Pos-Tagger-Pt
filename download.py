import os
import urllib.request
import tarfile

corpus_url = "http://nilc.icmc.usp.br/macmorpho/macmorpho-v3.tgz"
corpus_path = "macmorpho-v3.tgz"

if not os.path.exists(corpus_path):
    print("Baixando o corpus Mac-Morpho...")
    urllib.request.urlretrieve(corpus_url, corpus_path)
    print("Download concluído.")
else:
    print("Arquivo do corpus já existe.")

if not os.path.exists("macmorpho-v3"):
    print("Extraindo o corpus...")
    with tarfile.open(corpus_path, "r:gz") as tar:
        tar.extractall()
    print("Extração concluída.")
else:
    print("Corpus já extraído.")