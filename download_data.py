import os
import requests

# Carpeta donde está ubicado este script
DATA_DIR = os.path.dirname(os.path.abspath(__file__))

FILES = {
    "train.csv": "1ov4BQJcmSidP_YO5gaszsbfkmQgcRj1F",
    "test.csv": "1p6qAIGmpPgbfYpm7Clh6cIPm3768RHL0",
    "sample_submission.csv": "1ryBfQlw55rv2CsLXjLIb9BUwQKwzZQ06",
}

def download_file(file_id, destination):
    url = "https://drive.google.com/uc"

    session = requests.Session()
    response = session.get(
        url,
        params={"export": "download", "id": file_id},
        stream=True
    )

    # Confirmación para archivos grandes
    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            response = session.get(
                url,
                params={
                    "export": "download",
                    "id": file_id,
                    "confirm": value
                },
                stream=True
            )
            break

    response.raise_for_status()

    with open(destination, "wb") as f:
        for chunk in response.iter_content(1024 * 1024):
            if chunk:
                f.write(chunk)

    print(f"Descargado: {destination}")

def main():
    print(f"Guardando archivos en: {DATA_DIR}\n")

    for filename, file_id in FILES.items():
        destination = os.path.join(DATA_DIR, filename)

        print(f"Descargando {filename}...")
        download_file(file_id, destination)

    print("\n¡Descargas finalizadas!")

if __name__ == "__main__":
    main()
