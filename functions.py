
def leer_datos(shark_url):
    import pandas as pd

    archivo = pd.read_excel(shark_url)
    print("Hola")
    return archivo
