# SCRIPT para manipular hojas de cálculo de Google Sheets

import gspread
import pandas as pd

class GoogleSheet:
    def __init__(self, credentials, document, sheet_name):
        self.gc = gspread.service_account_from_dict(credentials)    # autenticarnos
        #self.gc = gspread.service_account(credentials)
        self.sh = self.gc.open(document)
        self.sheet = self.sh.worksheet(sheet_name)
    
    def read_data(self,range):  # range = "A1:E1" Data devolverá un array de la fila 1 desde la columna A hasta la E
        data = self.sheet.get(range)
        return data
    
    def read_data_by_uid(self, uid):
        data = self.sheet.get_all_records()
        df = pd.DataFrame(data)
        print(df)
        filtered_data = df[df['id-usuario'] == uid]
        return filtered_data    # devuelve un data frame de una tabla de dos filas siendo la primera las cabeceras y la segunda los datas del uid dado
    
    def write_data(self, range, values):    # range ej "A1:V1". values debe ser una lista de lista
        self.sheet.update(range, values)
    
    def write_data_by_uid(self, uid, values):
        # Busca la fila correspondiente al uid dado
        cell = self.sheet.find(uid)
        row_index = cell.row
        # modifica la fila con los values dados
        self.sheet.update(f"A{row_index}:E{row_index}", [values])
    
    def get_last_row_range(self):
        last_row = len(self.sheet.get_all_values()) + 1
        data = self.sheet.get_values()
        range_start = f"A{last_row}"
        range_end = f"{chr(ord('A') + len(data[0]) - 1)}{last_row}"
        return f"{range_start}:{range_end}"

    def get_all_values(self):
        #self.sheet.get_all_values() # esto devuelve una lista de listas. get_all_record es mas sencillo ya que obtiene valores filtrados
        return self.sheet.get_all_records()   # esto devuelve una lista de diccionarios, por lo que la clave es la columna de nombre y el valor es el valor de esa columna en particular

        