# Запуск
pip install -r requirements.txt
python app.py

# Генерация exe-файла
pip install PyInstaller
pyinstaller --windowed -n "Password Generator" --add-data "words_alpha.txt;." .\app.py

Сам бинарник будет находиться в папке dist