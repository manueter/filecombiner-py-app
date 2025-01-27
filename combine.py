import os

def combine_files(input_folder, output_file):
    """
    Combining text files (with UTF-8 encoding) from a selected folder into a single output file
    Combina el contenido de los archivos de texto con encoding utf-8 en un unico archivo.

    Parameters:
        input_folder (str): Path to folder with files to combine / La ruta a la carpeta que tiene los archivos a combinar.
        output_file (str): Path and name for output file / La ruta y nombre del archivo (incluye extension) destino.
    """
    try:
        # Se asegura que la input_folder no esté vacía.
        if not os.listdir(input_folder):
            raise ValueError("Input folder is empty / Carpeta de entrada no tiene ningun archivo.")

        with open(output_file, 'w', encoding='utf-8') as outfile:
            for filename in os.listdir(input_folder):
                file_path = os.path.join(input_folder, filename)

                # Solo procesa archivos (omite los directorios)
                if os.path.isfile(file_path):
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
        print(f"Output file at {output_file} / Contenidos combinados en  {output_file}")
    except Exception as e:
        print(f"Error trying to combine files / Error mientras se combinaban los archivos: {e}")
