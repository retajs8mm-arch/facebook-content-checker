#!/bin/bash

# 🛡️ درع الأحرار - تثبيت الأداة
# Facebook Content Checker - Installation Script

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                                                              ║"
echo "║          🛡️  درع الأحرار - Facebook Checker  🛡️             ║"
echo "║              أداة الفحص الشاملة للفيسبوك                    ║"
echo "║                                                              ║"
echo "║                 © مقتدى الساعدي - 2024                      ║"
echo "║                                                              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

echo "[*] جاري التثبيت..."
echo ""

# تحديث النظام
echo "[+] تحديث قائمة الحزم..."
sudo apt-get update

echo "[+] تثبيت Python وأدوات البناء..."
sudo apt-get install -y python3 python3-pip python3-venv build-essential

# إنشاء بيئة افتراضية
echo "[+] إنشاء بيئة Python افتراضية..."
python3 -m venv venv

# تفعيل البيئة الافتراضية
echo "[+] تفعيل البيئة الافتراضية..."
source venv/bin/activate

# تثبيت المتطلبات
echo "[+] تثبيت المكتبات المطلوبة..."
pip install -r requirements.txt

# جعل البرنامج قابل للتنفيذ
echo "[+] تعديل صلاحيات الملفات..."
chmod +x main.py
chmod +x install.sh

echo ""
echo "✅ تم التثبيت بنجاح!"
echo ""
echo "للتشغيل استخدم:"
echo "  ./main.py"
echo "أو"
echo "  python3 main.py"
echo ""
echo "شكراً لاستخدام درع الأحرار 🛡️"
echo ""
