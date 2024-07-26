import xml.etree.ElementTree as ET
import random

def process_random_element(random_element):
    # Mengambil semua elemen <li> dalam elemen <random>
    options = random_element.findall('li')

    if options:
        # Memilih jawaban secara acak dari opsi yang tersedia
        selected_option = random.choice(options)
        return selected_option.text.strip()

    return "Tidak ada pilihan yang tersedia."

def get_aiml_response(user_input, root):
    for category in root.findall(".//category"):
        pattern = category.find('pattern').text
        if user_input.lower() == pattern.lower():
            template = category.find('template')

            # Memeriksa apakah terdapat elemen <random> dalam template
            random_element = template.find('random')
            if random_element is not None:
                return process_random_element(random_element)

            # Jika tidak ada elemen <random>, kembalikan template biasa
            return template.text.strip()

    return "Saya tidak mengerti pertanyaan Anda."

def main():
    tree = ET.parse('storage/app/public/chatbot.xml')
    root = tree.getroot()

    while True:
        user_input = input("Pertanyaan (atau ketik 'exit' untuk keluar): ")

        if user_input.lower() == 'exit':
            break  # Keluar dari loop jika pengguna mengetik 'exit'

        response = get_aiml_response(user_input, root)
        print("Jawaban:", response)

if __name__ == "__main__":
    main()
