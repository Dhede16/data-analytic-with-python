import pandas as pd
import numpy as np 

data = pd.read_csv(r"dirty_cafe_sales.csv")
np.random.seed(42)

# Mengubah UNKNOWN dan ERROR menjadi Nan atau data kosong
for i in ['Item', 'Quantity', 'Price Per Unit', 'Total Spent', 'Payment Method', 'Location', 'Transaction Date' ]:
    data[i] = data[i].replace(['UNKNOWN', 'ERROR'], np.nan)

# Mengisi Nan atau data kosong menjadi nilai acak pada kolom tersebut
for i in ['Item', 'Payment Method', 'Location', 'Transaction Date', 'Quantity'] : 
    unique_vals = data[i].dropna().unique()
    data[i] = data[i].apply(lambda x: np.random.choice(unique_vals) if pd.isna(x) else x)

# Mengubah tipe data kolom Price per Unit ke Float
data['Price Per Unit'] = data['Price Per Unit'].astype(float)

# Isi NaN pada kolom Price Per Unit dengan modus (harga yang paling sering muncul per item)
data['Price Per Unit'] = data.groupby('Item')['Price Per Unit'].transform(
    lambda x: x.fillna(x.mode().iloc[0]) if not x.mode().empty else x
)

# Mengubah tipe data kolom Total Spent ke Float
data['Total Spent'] = data['Total Spent'].astype(float)

# Mengubah tipe data kolom Quantity ke Float
data['Quantity'] = data['Quantity'].astype(float)

# Mengisi Total Spent sesuai dengan perhitungan Quantity x Price Per Unit
data['Total Spent'] = data['Quantity'] * data['Price Per Unit']

print(data.to_string())

output_path = r"C:\Users\NITRO\Desktop\Cafe Sales\data\cleaned_cafe_sales.csv"
data.to_csv(output_path, index=False)

