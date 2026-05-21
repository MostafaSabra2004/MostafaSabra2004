from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# ==============================
# تحميل بيانات الطلاب من الإكسيل
# ==============================
EXCEL_FILE = "students.xlsx"
students_data = {}

def load_students():
    global students_data
    if not os.path.exists(EXCEL_FILE):
        print(f"⚠️  ملف {EXCEL_FILE} غير موجود — ضع الملف في نفس مجلد app.py")
        return

    df = pd.read_excel(EXCEL_FILE, dtype={"الرقم القومى": str})

    for _, row in df.iterrows():
        nid = str(row.get("الرقم القومى", "")).strip()
        if not nid:
            continue
        students_data[nid] = {
            "name":      row.get("اسم الطالب", ""),
            "seat":      row.get("رقم الجلوس", ""),
            "school":    row.get("اسم المدرسة", ""),
            "arabic":    round(float(row.get("لغة عربية الترم الاول", 0) or 0), 2),
            "eng1":      round(float(row.get("لغة اجنبية اولى الترم اول", 0) or 0), 2),
            "studies":   round(float(row.get("دراسات الترم الاول", 0) or 0), 2),
            "math":      round(float(row.get("رياضيات الترم الاول", 0) or 0), 2),
            "science":   round(float(row.get("علوم الترم الاول", 0) or 0), 2),
            "total":     round(float(row.get("المجموع الفعلى الترم الأول", 0) or 0), 2),
            "religion":  round(float(row.get("تربية دينية الترم الاول", 0) or 0), 2),
            "art":       round(float(row.get("رسم الترم الاول", 0) or 0), 2),
            "computer":  round(float(row.get("كمبيوتر الترم الاول", 0) or 0), 2),
            "eng_level": round(float(row.get("لغة اجنبية اولى(مستوى) الترم الاول", 0) or 0), 2),
            "eng2":      round(float(row.get("لغة اجنبية ثانية  الترم الاول", 0) or 0), 2),
        }

    print(f"✅ تم تحميل {len(students_data)} طالب")

load_students()

# ==============================
# Routes
# ==============================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/student/<national_id>")
def get_student(national_id):
    nid = national_id.strip()
    student = students_data.get(nid)
    if student:
        return jsonify({"found": True, "student": student})
    return jsonify({"found": False}), 404

if __name__ == "__main__":
    app.run(debug=True)
