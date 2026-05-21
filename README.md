# 🏫 شهادة نتيجة الطلاب — Flask App

## 📁 محتويات المشروع
```
certificate_app/
├── app.py              ← التطبيق الرئيسي
├── requirements.txt    ← المكتبات المطلوبة
├── Procfile            ← إعداد Render
├── students.xlsx       ← ضع ملف الإكسيل هنا  ⬅️
└── templates/
    └── index.html      ← صفحة الشهادة
```

---

## 🚀 خطوات الرفع على الإنترنت (مجاني)

### الخطوة 1 — ضع ملف الإكسيل
- ضع ملف الإكسيل في نفس مجلد `app.py`
- تأكد أن اسمه بالظبط: `students.xlsx`

### الخطوة 2 — GitHub
1. افتح https://github.com وسجل حساب مجاني
2. اضغط **New Repository** → سمّيه `certificate-app`
3. ارفع كل ملفات المشروع (بما فيهم students.xlsx)

### الخطوة 3 — Render (استضافة مجانية)
1. افتح https://render.com وسجل بحساب GitHub
2. اضغط **New → Web Service**
3. اختر الـ Repository اللي عملته
4. اضبط الإعدادات:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. اضغط **Deploy** وانتظر دقيقتين
6. ستحصل على رابط مثل: `https://certificate-app.onrender.com`

---

## 📌 ملاحظات مهمة
- اسم العمود في الإكسيل يجب أن يكون: `الرقم القومى` (بدون همزة)
- الخطة المجانية على Render تنام بعد 15 دقيقة عدم استخدام
  (أول طالب يفتح الرابط ينتظر ~30 ثانية فقط)
- إذا أردت تغيير بيانات الطلاب: ارفع ملف إكسيل جديد على GitHub وسيتحدث تلقائياً

---

**Mr. Mostafa Sabra | 01224061995**
