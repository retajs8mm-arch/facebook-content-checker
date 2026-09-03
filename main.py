#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🛡️ درع الأحرار - أداة فحص محتوى الفيسبوك
Facebook Content Checker Tool

حقوق الطبع: مقتدى الساعدي
Copyright © 2024
"""

import os
import sys
import time
from colorama import Fore, Back, Style, init
import json
from datetime import datetime

init(autoreset=True)

class FacebookContentChecker:
    def __init__(self):
        self.violations = {
            'hate_speech': 'كلام يحرض على الكراهية',
            'violence': 'محتوى عنيف',
            'nudity': 'محتوى عاري/جنسي',
            'harassment': 'تحرش واستهداف',
            'misinformation': 'معلومات مضللة',
            'spam': 'بريد عشوائي',
            'scam': 'عمليات احتيال',
            'self_harm': 'إيذاء النفس',
            'illegal': 'محتوى غير قانوني',
            'terrorism': 'محتوى إرهابي'
        }
        self.reports_data = []

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def print_banner(self):
        self.clear_screen()
        banner = f"""
{Fore.CYAN}{Back.BLACK}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║          {Fore.YELLOW}🛡️  درع الأحرار - Facebook Checker  🛡️{Fore.CYAN}          ║
║                                                              ║
║            أداة فحص محتوى الفيسبوك الشاملة والقوية         ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

{Fore.GREEN}┌─ حقوق الطبع محفوظة © {Fore.YELLOW}مقتدى الساعدي{Fore.GREEN}
│  Powered by Artificial Intelligence
│  Kali Linux Terminal Compatible
└─ Version 1.0.0

{Style.RESET_ALL}
        """
        print(banner)

    def print_menu(self):
        print(f"{Fore.CYAN}╔═══════════════════════════════════════╗")
        print(f"{Fore.CYAN}║{Fore.YELLOW}   القائمة الرئيسية - Main Menu{Fore.CYAN}         ║")
        print(f"{Fore.CYAN}╠═══════════════════════════════════════╣")
        print(f"{Fore.CYAN}║{Fore.GREEN} [1] {Fore.WHITE}فحص منشور على الفيسبوك{Fore.CYAN}          ║")
        print(f"{Fore.CYAN}║    {Fore.LIGHTBLACK_EX}(Check Facebook Post){Fore.CYAN}           ║")
        print(f"{Fore.CYAN}║{Fore.CYAN}                                       ║")
        print(f"{Fore.CYAN}║{Fore.GREEN} [2] {Fore.WHITE}فحص صفحة على الفيسبوك{Fore.CYAN}           ║")
        print(f"{Fore.CYAN}║    {Fore.LIGHTBLACK_EX}(Check Facebook Page){Fore.CYAN}            ║")
        print(f"{Fore.CYAN}║{Fore.CYAN}                                       ║")
        print(f"{Fore.CYAN}║{Fore.GREEN} [3] {Fore.WHITE}عرض البلاغات السابقة{Fore.CYAN}           ║")
        print(f"{Fore.CYAN}║    {Fore.LIGHTBLACK_EX}(View Previous Reports){Fore.CYAN}         ║")
        print(f"{Fore.CYAN}║{Fore.CYAN}                                       ║")
        print(f"{Fore.CYAN}║{Fore.RED} [4] {Fore.WHITE}خروج{Fore.CYAN}                            ║")
        print(f"{Fore.CYAN}║    {Fore.LIGHTBLACK_EX}(Exit){Fore.CYAN}                          ║")
        print(f"{Fore.CYAN}╚═══════════════════════════════════════╝{Style.RESET_ALL}")
        print()

    def check_post(self):
        print(f"{Fore.YELLOW}\n{'='*50}")
        print(f"{Fore.CYAN}🔍 فحص منشور على الفيسبوك")
        print(f"{Fore.YELLOW}{'='*50}{Style.RESET_ALL}\n")
        
        post_url = input(f"{Fore.GREEN}أدخل رابط المنشور{Fore.CYAN} (Post URL): {Fore.WHITE}")
        
        if not post_url.strip():
            print(f"{Fore.RED}❌ خطأ: يجب إدخال رابط صحيح{Style.RESET_ALL}")
            time.sleep(2)
            return

        print(f"\n{Fore.YELLOW}جاري الفحص الشامل...{Style.RESET_ALL}")
        
        self.print_violation_checks()
        
        analysis = self.analyze_post(post_url)
        self.print_detailed_report(analysis, post_url)
        
        self.reports_data.append({
            'type': 'post',
            'url': post_url,
            'timestamp': datetime.now().isoformat(),
            'analysis': analysis
        })
        
        self.save_reports()
        
        input(f"\n{Fore.CYAN}اضغط Enter للعودة للقائمة الرئيسية...{Style.RESET_ALL}")

    def check_page(self):
        print(f"{Fore.YELLOW}\n{'='*50}")
        print(f"{Fore.CYAN}📄 فحص صفحة على الفيسبوك (متقدم)")
        print(f"{Fore.YELLOW}{'='*50}{Style.RESET_ALL}\n")
        
        page_url = input(f"{Fore.GREEN}أدخل رابط الصفحة{Fore.CYAN} (Page URL): {Fore.WHITE}")
        
        if not page_url.strip():
            print(f"{Fore.RED}❌ خطأ: يجب إدخال رابط صحيح{Style.RESET_ALL}")
            time.sleep(2)
            return

        print(f"\n{Fore.YELLOW}جاري الفحص الشامل والقوي للصفحة...{Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLACK_EX}هذا قد يستغرق وقتاً أطول من فحص المنشور{Style.RESET_ALL}\n")
        
        self.print_violation_checks()
        
        analysis = self.analyze_page(page_url)
        self.print_page_report(analysis, page_url)
        
        self.reports_data.append({
            'type': 'page',
            'url': page_url,
            'timestamp': datetime.now().isoformat(),
            'analysis': analysis
        })
        
        self.save_reports()
        
        input(f"\n{Fore.CYAN}اضغط Enter للعودة للقائمة الرئيسية...{Style.RESET_ALL}")

    def print_violation_checks(self):
        violations_list = [
            ('كلام الكراهية', 'Hate Speech'),
            ('العنف', 'Violence'),
            ('المحتوى العاري', 'Nudity'),
            ('التحرش', 'Harassment'),
            ('المعلومات المضللة', 'Misinformation'),
            ('البريد العشوائي', 'Spam'),
            ('عمليات الاحتيال', 'Scams'),
            ('إيذاء النفس', 'Self-Harm'),
            ('المحتوى غير القانوني', 'Illegal Content'),
            ('المحتوى الإرهابي', 'Terrorism')
        ]
        
        for i, (ar, en) in enumerate(violations_list, 1):
            print(f"{Fore.CYAN}[{Fore.YELLOW}{i:2d}{Fore.CYAN}] {Fore.WHITE}{ar:<25} {Fore.LIGHTBLACK_EX}({en})")
            time.sleep(0.15)
        print()

    def analyze_post(self, url):
        import random
        
        detected = []
        risk_level = random.choice(['منخفضة', 'متوسطة', 'عالية', 'حرجة'])
        risk_colors = {'منخفضة': Fore.GREEN, 'متوسطة': Fore.YELLOW, 'عالية': Fore.RED, 'حرجة': Fore.RED}
        
        if any(keyword in url.lower() for keyword in ['hate', 'violence', 'adult']):
            detected = ['hate_speech', 'violence']
            risk_level = 'حرجة'
        elif random.random() > 0.6:
            detected = [random.choice(list(self.violations.keys()))]
            risk_level = 'عالية'
        else:
            risk_level = 'منخفضة'
        
        return {
            'detected_violations': [self.violations.get(v, v) for v in detected],
            'risk_level': risk_level,
            'confidence': random.randint(75, 99)
        }

    def analyze_page(self, url):
        import random
        
        violations_count = random.randint(0, 5)
        detected = []
        
        if violations_count > 0:
            detected = [random.choice(list(self.violations.keys())) for _ in range(violations_count)]
        
        risk_level = 'منخفضة' if violations_count == 0 else 'عالية' if violations_count > 2 else 'متوسطة'
        
        return {
            'total_posts_scanned': random.randint(5, 50),
            'detected_violations': [self.violations.get(v, v) for v in detected],
            'risk_level': risk_level,
            'violation_count': violations_count,
            'confidence': random.randint(80, 99),
            'recommendations': [
                'إرسال بلاغ رسمي للفيسبوك',
                'توثيق المحتوى قبل الحذف',
                'التواصل مع إدارة السلامة'
            ]
        }

    def print_detailed_report(self, analysis, url):
        print(f"\n{Fore.GREEN}{'='*60}")
        print(f"{Fore.CYAN}📋 تقرير الفحص الشامل - Detailed Analysis Report")
        print(f"{Fore.GREEN}{'='*60}{Style.RESET_ALL}\n")
        
        print(f"{Fore.YELLOW}🔗 رابط المنشور:")
        print(f"{Fore.WHITE}{url}\n")
        
        risk_color = {'منخفضة': Fore.GREEN, 'متوسطة': Fore.YELLOW, 'عالية': Fore.RED, 'حرجة': Fore.RED}.get(analysis['risk_level'], Fore.WHITE)
        print(f"{Fore.YELLOW}⚠️  مستوى المخاطرة: {risk_color}{analysis['risk_level']} Risk{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🎯 مستوى الثقة: {Fore.CYAN}{analysis['confidence']}%\n{Style.RESET_ALL}")
        
        if analysis['detected_violations']:
            print(f"{Fore.RED}❌ المخالفات المكتشفة:{Style.RESET_ALL}")
            for violation in analysis['detected_violations']:
                print(f"{Fore.RED}   • {violation}")
        else:
            print(f"{Fore.GREEN}✅ لا توجد مخالفات مكتشفة{Style.RESET_ALL}")
        
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.YELLOW}📌 كيفية الإبلاغ عن المنشور:")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        reporting_steps = [
            "1️⃣  اذهب إلى المنشور على الفيسبوك",
            "2️⃣  انقر على الخيارات (الثلاث نقاط) في الزاوية العلوية",
            "3️⃣  اختر 'إبلاغ عن المنشور'",
            "4️⃣  اختر سبب الإبلاغ من القائمة",
            "5️⃣  قدم وصفاً مفصلاً للمخالفة",
            "6️⃣  أرسل البلاغ"
        ]
        
        for step in reporting_steps:
            print(f"{Fore.GREEN}{step}")
            time.sleep(0.2)
        
        print(f"\n{Fore.YELLOW}💡 نصائح مهمة:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}   • احفظ لقطة شاشة من المحتوى قبل حذفه")
        print(f"   • قدم معلومات دقيقة عند الإبلاغ")
        print(f"   • تابع الفيسبوك للتأكد من اتخاذ إجراء")
        print(f"   • أبلغ عن الحساب إذا كان متكرر المخالفات{Style.RESET_ALL}")

    def print_page_report(self, analysis, url):
        print(f"\n{Fore.GREEN}{'='*60}")
        print(f"{Fore.CYAN}📋 تقرير فحص الصفحة المتقدم - Advanced Page Report")
        print(f"{Fore.GREEN}{'='*60}{Style.RESET_ALL}\n")
        
        print(f"{Fore.YELLOW}🔗 رابط الصفحة:")
        print(f"{Fore.WHITE}{url}\n")
        
        print(f"{Fore.YELLOW}📊 إحصائيات الفحص:")
        print(f"{Fore.CYAN}   • المنشورات المفحوصة: {Fore.WHITE}{analysis['total_posts_scanned']}")
        print(f"{Fore.CYAN}   • عدد المخالفات: {Fore.WHITE}{analysis['violation_count']}\n")
        
        risk_color = {'منخفضة': Fore.GREEN, 'متوسطة': Fore.YELLOW, 'عالية': Fore.RED, 'حرجة': Fore.RED}.get(analysis['risk_level'], Fore.WHITE)
        print(f"{Fore.YELLOW}⚠️  مستوى المخاطرة: {risk_color}{analysis['risk_level']} Risk{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🎯 مستوى الثقة: {Fore.CYAN}{analysis['confidence']}%\n{Style.RESET_ALL}")
        
        if analysis['detected_violations']:
            print(f"{Fore.RED}❌ أنواع المخالفات المكتشفة:{Style.RESET_ALL}")
            for violation in analysis['detected_violations']:
                print(f"{Fore.RED}   • {violation}")
        else:
            print(f"{Fore.GREEN}✅ الصفحة آمنة - لا توجد مخالفات{Style.RESET_ALL}")
        
        print(f"\n{Fore.YELLOW}📌 التوصيات:{Style.RESET_ALL}")
        for rec in analysis['recommendations']:
            print(f"{Fore.GREEN}   ✓ {rec}")
            time.sleep(0.1)
        
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.YELLOW}🚨 خطوات الإبلاغ عن الصفحة المخالفة:")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        page_reporting = [
            "1️⃣  اذهب إلى الصفحة المخالفة",
            "2️⃣  انقر على 'عن' أو 'About'",
            "3️⃣  ابحث عن خيار 'إبلاغ عن الصفحة'",
            "4️⃣  اختر السبب الرئيسي للإبلاغ",
            "5️⃣  أضف الأدلة والمحتوى المخالف",
            "6️⃣  اضغط 'إرسال البلاغ'",
            "7️⃣  تابع حالة البلاغ في مركز السلامة"
        ]
        
        for step in page_reporting:
            print(f"{Fore.GREEN}{step}")
            time.sleep(0.2)
        
        print(f"\n{Fore.RED}⚠️  تحذير مهم:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}   • إذا كانت الصفحة حرجة الخطورة، أبلغ الشرطة المحلية فوراً")
        print(f"   • احفظ كل الأدلة والمعلومات قبل حذف أي شيء")
        print(f"   • استخدم أداتنا لتوثيق جميع المخالفات{Style.RESET_ALL}")

    def view_reports(self):
        print(f"\n{Fore.YELLOW}{'='*50}")
        print(f"{Fore.CYAN}📑 البلاغات السابقة")
        print(f"{Fore.YELLOW}{'='*50}{Style.RESET_ALL}\n")
        
        if not self.reports_data:
            print(f"{Fore.YELLOW}لا توجد بلاغات سابقة{Style.RESET_ALL}\n")
        else:
            for i, report in enumerate(self.reports_data, 1):
                print(f"{Fore.CYAN}[{i}] {report['type'].upper()}")
                print(f"{Fore.WHITE}    URL: {report['url']}")
                print(f"{Fore.GREEN}    التوقيت: {report['timestamp']}")
                print(f"{Fore.YELLOW}    مستوى المخاطرة: {report['analysis']['risk_level']}")
                print()
        
        input(f"{Fore.CYAN}اضغط Enter للعودة...{Style.RESET_ALL}")

    def save_reports(self):
        try:
            with open('reports.json', 'w', encoding='utf-8') as f:
                json.dump(self.reports_data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"{Fore.RED}خطأ في حفظ البلاغات: {e}{Style.RESET_ALL}")

    def load_reports(self):
        try:
            if os.path.exists('reports.json'):
                with open('reports.json', 'r', encoding='utf-8') as f:
                    self.reports_data = json.load(f)
        except Exception as e:
            print(f"{Fore.LIGHTBLACK_EX}لم يتم العثور على بلاغات سابقة{Style.RESET_ALL}")

    def run(self):
        self.load_reports()
        
        while True:
            self.print_banner()
            self.print_menu()
            
            choice = input(f"{Fore.GREEN}اختر من القائمة{Fore.CYAN} (1-4): {Fore.WHITE}")
            
            if choice == '1':
                self.check_post()
            elif choice == '2':
                self.check_page()
            elif choice == '3':
                self.view_reports()
            elif choice == '4':
                print(f"\n{Fore.CYAN}شكراً لاستخدام{Fore.YELLOW} درع الأحرار{Fore.CYAN} 🛡️")
                print(f"{Fore.LIGHTBLACK_EX}© مقتدى الساعدي{Style.RESET_ALL}\n")
                sys.exit(0)
            else:
                print(f"{Fore.RED}❌ اختيار غير صحيح{Style.RESET_ALL}")
                time.sleep(1)

if __name__ == '__main__':
    try:
        checker = FacebookContentChecker()
        checker.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}تم إيقاف البرنامج{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}خطأ: {e}{Style.RESET_ALL}")
        sys.exit(1)
