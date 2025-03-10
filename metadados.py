from geopy.geocoders import Nominatim
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def convert_to_degrees(value):
    """Converte coordenadas EXIF para formato decimal."""
    d, m, s = value
    return d + (m / 60.0) + (s / 3600.0)

def get_address_from_coordinates(lat, lon):
    """Obtém o nome da rua a partir das coordenadas GPS."""
    try:
        geolocator = Nominatim(user_agent="Vish/1.0 (lukascsouza1@gmail.com)")
        location = geolocator.reverse((lat, lon), exactly_one=True)
        return location.address if location else "Endereço não encontrado"
    except Exception as e:
        return f"Erro ao obter endereço: {e}"

def get_gps_location(image_path):
    """Extrai coordenadas GPS de uma imagem se disponíveis e retorna o endereço."""
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
    except Exception as e:
        return f"Erro ao abrir a imagem: {e}"
    
    if not exif_data:
        return "Nenhum dado EXIF encontrado."
    
    gps_info = {}
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        if tag_name == "GPSInfo":
            for gps_tag in value:
                sub_tag = GPSTAGS.get(gps_tag, gps_tag)
                gps_info[sub_tag] = value[gps_tag]
    
    if "GPSLatitude" in gps_info and "GPSLongitude" in gps_info:
        lat = convert_to_degrees(gps_info["GPSLatitude"])
        lon = convert_to_degrees(gps_info["GPSLongitude"])
        
        if gps_info.get("GPSLatitudeRef", "N") != "N":
            lat = -lat
        if gps_info.get("GPSLongitudeRef", "E") != "E":
            lon = -lon
        
        address = get_address_from_coordinates(lat, lon)
        
        # Organizar melhor a saída
        output = (
            f"\n🗺️ **Informações da Imagem**\n"
            f"------------------------------\n"
            f"📍 Latitude: {lat}\n"
            f"📍 Longitude: {lon}\n"
            f"📌 Endereço: {address}\n"
            f"------------------------------\n"
        )
        return output
    else:
        return "Nenhuma informação de GPS encontrada."

# Caminho da imagem enviada (corrigido para evitar erro no Windows)
image_path = r"C:\Users\202309057981\Documents\teste\20250310_085301.jpg"  # Substitua pelo nome real da imagem

# Verificar metadados da imagem
print(get_gps_location(image_path))