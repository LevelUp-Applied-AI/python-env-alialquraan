import pathlib
import pandas as pd

# تحديد مسار ملف البيانات بشكل ذكي ومضمون
# السطر التالي يعني: اذهب لموقع هذا الملف الحالي، ثم ارجع لمجلد الخلف، ثم ادخل مجلد data
data_path = pathlib.Path(__file__).parent.parent / "data" / "sample.csv"

# تحميل البيانات
df = pd.read_csv(data_path)

# عرض النتائج في التيرمينال
print("--- Output from Python Script ---")
print("Shape:", df.shape)
print("\nFirst Few Rows:")
print(df.head())
print("\nStatistical Summary:")
print(df.describe())