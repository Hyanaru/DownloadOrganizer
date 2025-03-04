import os
import shutil

# Imposta il percorso della cartella Download
download_folder = os.path.expanduser("~/Downloads")

# Definizione delle estensioni per le immagini
image_extensions = {"jpg", "jpeg", "png", "gif", "bmp", "tiff", "svg","heic","webp"}

# Definizione delle estensioni per gli archivi
archive_extensions = {"zip", "rar", "7z", "tar", "gz", "bz2"}

# Definizione delle estensioni per i file di Office
office_extensions = {
    "excel": {"xls", "xlsx", "xlsm", "csv"},
    "word": {"doc", "docx", "rtf"},
    "powerpoint": {"ppt", "pptx", "pps"},
    "pdf": {"pdf"}
}

def organize_downloads(folder):
    if not os.path.exists(folder):
        print("La cartella specificata non esiste.")
        return
    
    # Scansiona tutti i file nella cartella Download
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        
        # Controlla se è un file
        if os.path.isfile(file_path):
            # Estrai l'estensione del file
            file_extension = file.split('.')[-1].lower() if '.' in file else "sconosciuto"
            
            # Determina la cartella di destinazione
            if file_extension in image_extensions:
                destination_folder = os.path.join(folder, "immagini")
            elif file_extension in archive_extensions:
                destination_folder = os.path.join(folder, "archivi")
            else:
                office_category = None
                for category, extensions in office_extensions.items():
                    if file_extension in extensions:
                        office_category = category
                        break
                
                if office_category:
                    destination_folder = os.path.join(folder, "Office", office_category)
                else:
                    destination_folder = os.path.join(folder, file_extension)
            
            # Crea la cartella di destinazione se non esiste
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            
            # Sposta il file nella cartella corrispondente
            shutil.move(file_path, os.path.join(destination_folder, file))
            print(f"Spostato: {file} -> {destination_folder}")
    
    # Rimuove cartelle vuote
    remove_empty_folders(folder)

def remove_empty_folders(folder):
    for root, dirs, _ in os.walk(folder, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):  # Controlla se la cartella è vuota
                os.rmdir(dir_path)
                print(f"Cartella vuota eliminata: {dir_path}")

if __name__ == "__main__":
    organize_downloads(download_folder)
