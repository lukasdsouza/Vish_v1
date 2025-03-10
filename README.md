# 📌 VISH: Extração de Localização a partir de Imagens usando Pillow e Geopy

Este projeto permite extrair **coordenadas GPS (latitude e longitude)** de imagens que contenham metadados EXIF e obter o **endereço** correspondente a partir das coordenadas.

## 📂 **Requisitos**
Para rodar este projeto, certifique-se de que tem os seguintes requisitos instalados:

- **Python 3.x**
- **Bibliotecas necessárias** (instalar com `pip`):
  ```bash
  pip install pillow geopy
  ```
### **📌 O que são `Pillow` e `geopy`?**  

No seu projeto, você usa duas bibliotecas essenciais para manipulação de imagens e geolocalização:  

---

## **🖼️ Pillow (PIL Fork) - Manipulação de Imagens**
📌 **Pillow** é uma biblioteca de **processamento de imagens** para Python. Ela permite abrir, editar e manipular imagens em diversos formatos (**JPEG, PNG, BMP, GIF, TIFF**, etc.).  

✔ **No seu código**, Pillow é usada para **abrir a imagem e extrair os metadados EXIF**, que incluem informações da câmera e coordenadas GPS.  

### 🔹 **Principais funções do `Pillow` usadas no seu projeto**:
- `Image.open(image_path)`: Abre a imagem.
- `image._getexif()`: Extrai metadados EXIF da imagem.
- `ExifTags.TAGS`: Permite identificar os metadados EXIF.
- `ExifTags.GPSTAGS`: Converte códigos EXIF para nomes compreensíveis.

### 🔹 **Como instalar `Pillow`**
```bash
pip install pillow
```

📌 **Exemplo simples de uso**
```python
from PIL import Image

# Abrindo uma imagem
image = Image.open("exemplo.jpg")

# Exibindo a imagem
image.show()
```

---

## **🌍 Geopy - Geocodificação e Geolocalização**
📌 **Geopy** é uma biblioteca que permite **converter endereços em coordenadas (geocodificação) e coordenadas em endereços (reverso)** usando serviços como **Nominatim (OpenStreetMap), Google Maps API, Bing Maps**, etc.

✔ **No seu código**, `geopy` é usada para pegar as **coordenadas GPS da imagem** e **transformá-las em um endereço legível**.

### 🔹 **Principais funções do `geopy` usadas no seu projeto**:
- `Nominatim(user_agent="seu_app")`: Define o provedor de geocodificação.
- `geolocator.reverse((lat, lon))`: Converte latitude e longitude em um endereço real.

### 🔹 **Como instalar `geopy`**
```bash
pip install geopy
```

📌 **Exemplo simples de uso**
```python
from geopy.geocoders import Nominatim

# Criando um objeto geolocalizador
geolocator = Nominatim(user_agent="meu_app")

# Pegando o endereço a partir das coordenadas GPS
location = geolocator.reverse("-22.9068, -43.1729")
print(location.address)
```

**Saída esperada**:
```
Praia de Copacabana, Rio de Janeiro, RJ, Brasil
```

---

- **Pillow (`PIL`)** 👉 Manipula imagens e extrai metadados EXIF.
- **Geopy (`Nominatim`)** 👉 Converte coordenadas GPS em endereços legíveis.

## 🚀 **Como Rodar o Projeto**

1. **Clone ou baixe este repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Coloque a imagem na pasta correta** (substitua `sua_imagem.jpg` pelo nome real da imagem no código):
   ```
   C:\Users\SeuUsuario\Documents\teste\sua_imagem.jpg
   ```

3. **Execute o script** no terminal ou no VS Code:
   ```bash
   python nome_do_script.py
   ```

## 📌 **Saída Esperada**
Se a imagem contiver metadados EXIF com GPS, a saída será semelhante a:
```
🗺️ Informações da Imagem
------------------------------
📍 Latitude: -23.0058952
📍 Longitude: -43.3138099
📌 Endereço: IBMEC, 940, Avenida Armando Lombardi, Jardim Oceânico, Barra da Tijuca, Rio de Janeiro, RJ, Brasil
------------------------------
```

Caso a imagem **não contenha dados de GPS**, o script retornará:
```
Nenhuma informação de GPS encontrada.
```

## ❗ **Importante**
- **Fotos enviadas pelo WhatsApp como "Imagem" não contêm metadados EXIF** (use "Documento" para preservar).
- O projeto usa **Nominatim (OpenStreetMap)** para converter coordenadas em endereço, então uma conexão com a Internet é necessária.

## 🛠 **Contribuição**
Se quiser contribuir, faça um fork deste repositório e envie um pull request! 😊

## 📜 **Licença**
Este projeto é de código aberto e está sob a licença MIT.

