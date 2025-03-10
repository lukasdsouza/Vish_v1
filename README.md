# 📌 VISH: Extração de Localização de Imagens

Este projeto permite extrair **coordenadas GPS (latitude e longitude)** de imagens que contenham metadados EXIF e obter o **endereço** correspondente a partir das coordenadas.

## 📂 **Requisitos**
Para rodar este projeto, certifique-se de que tem os seguintes requisitos instalados:

- **Python 3.x**
- **Bibliotecas necessárias** (instalar com `pip`):
  ```bash
  pip install pillow geopy
  ```

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

