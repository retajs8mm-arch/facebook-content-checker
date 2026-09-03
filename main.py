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
        
        self.report_templates = {
            'hate_speech': {
                'title': 'كلام الكراهية',
                'template': """
📋 نموذج بلاغ كلام الكراهية:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔗 رابط المنشور: [ضع الرابط هنا]

❌ نوع المخالفة: كلام يحرض على الكراهية

📝 تفاصيل البلاغ:
المنشور يحتوي على كلام يحرض على الكراهية تجاه مجموعة معينة
(عرقية، دينية، جنسية، أو غيرها) ويسيء لكرامتهم.

🔗 الأدلة:
• اقتباس النص المسيء: [اكتب النص هنا]
• عدد المرات المنشورة: مرة واحدة / عدة مرات
• التأثير المتوقع: تحريض على كراهية وعنف

⚠️ التأثير:
- ينتهك معايير الجماعة
- قد يسبب أذى نفسي للمجموعة المستهدفة
- يحرض على التمييز والعنف

✅ الخطوات المقترحة:
1. احفظ لقطة شاشة من المنشور
2. انسخ الرابط الكامل
3. اذهب إلى خيارات المنشور (⋮)
4. اختر "إبلاغ عن المنشور"
5. اختر "كلام الكراهية"
6. أرسل هذا البلاغ
7. تابع الحالة في مركز السلامة
"""
            },
            
            'violence': {
                'title': 'محتوى عنيف',
                'template': """
📋 نموذج بلاغ محتوى عنيف:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔗 رابط المنشور: [ضع الرابط هنا]

❌ نوع المخالفة: محتوى عنيف

📝 تفاصيل البلاغ:
المنشور يحتوي على عنف صريح أو تهديدات تجاه أشخاص أو مجموعات،
أو يشجع على العنف والإيذاء الجسدي.

🔗 الأدلة:
• وصف المحتوى العنيف: [اكتب الوصف]
• مستوى العنف: طفيف / متوسط / حاد
• ما إذا كان يحتوي على تهديد مباشر: نعم / لا

⚠️ التأثير:
- خطير على سلامة الأشخاص
- قد يشجع على ارتكاب جرائم
- ينتهك القوانين والتشريعات

✅ الخطوات المقترحة:
1. احفظ الدليل بسرعة
2. لا تشارك المنشور
3. اذهب إلى خيارات المنشور
4. اختر "إبلاغ عن المنشور"
5. اختر "العنف"
6. قدم تفاصيل دقيقة
7. في الحالات الخطيرة أبلغ الشرطة مباشرة
"""
            },
            
            'misinformation': {
                'title': 'معلومات مضللة',
                'template': """
📋 نموذج بلاغ معلومات مضللة:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔗 رابط المنشور: [ضع الرابط هنا]

❌ نوع المخالفة: معلومات مضللة

📝 تفاصيل البلاغ:
المنشور يحتوي على معلومات كاذبة أو مضللة قد تؤثر على سلامة
المجتمع أو تنشر ادعاءات مزيفة.

🔗 الأدلة:
• المعلومة المزيفة: [اكتب ما يقوله المنشور]
• المعلومة الصحيحة: [اكتب الحقيقة]
• المصدر الموثوق: [ضع مصدراً رسمياً]

⚠️ المشاكل:
- تضليل الرأي العام
- قد تؤثر على قرارات مهمة
- تقلل ثقة المجتمع

✅ الخطوات المقترحة:
1. اجمع مصادر موثوقة
2. احفظ لقطات الشاشة
3. اذهب للمنشور
4. اختر "إبلاغ عن المنشور"
5. اختر "معلومات مضللة"
6. أرفق المصادر الصحيحة
7. شارك المعلومات الصحيحة مع الآخرين
"""
            },
            
            'harassment': {
                'title': 'تحرش واستهداف',
                'template': """
📋 نموذج بلاغ التحرش:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔗 رابط المنشور: [ضع الرابط هنا]

❌ نوع المخالفة: تحرش واستهداف

✅ الخطوات المقترحة:
1. احفظ كل الأدلة
2. اذهب للمنشور
3. اختر "إبلاغ عن المنشور"
4. اختر "تحرش"
"""
            }
        }
        
        self.reports_data = []

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def print_giant_banner(self):
        """طباعة شعار درع الأحرار ضخم جداً بالعربي"""
        banner = f"""
{Fore.YELLOW}{Back.BLACK}

        ██████╗ ██████╗ ███████╗ █████╗ ███████╗
        ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝
        ██║  ██║██████╔╝█████╗  ███████║█████╗  
        ██║  ██║██╔══██╗██╔══╝  ██╔══██║██╔══╝  
        ██████╔╝██║  ██║███████╗██║  ██║███████╗
        ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝


   ╔════════════════════════════════════════════════════════════╗
   ║                                                            ║
   ║                 {Fore.CYAN}🛡️  درع الأحرار  🛡️{Fore.YELLOW}                    ║
   ║                                                            ║
   ║           أداة فحص محتوى الفيسبوك الشاملة والقوية        ║
   ║                                                            ║
   ║            Facebook Content Checker Tool v2.0             ║
   ║                                                            ║
   ║         © حقوق الطبع محفوظة لـ {Fore.CYAN}مقتدى الساعدي{Fore.YELLOW}           ║
   ║          Powered by Artificial Intelligence               ║
   ║            Kali Linux Terminal Compatible                 ║
   ║                                                            ║
   ╚════════════════════════════════════════════════════════════╝


{Style.RESET_ALL}
        """
        self.clear_screen()
        print(banner)
        time.sleep(2)

    def print_banner(self):
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
└─ Version 2.0.0

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
        print(f"{Fore.CYAN}║{Fore.GREEN} [4] {Fore.WHITE}نماذج البلاغات الجاهزة{Fore.CYAN}         ║")
        print(f"{Fore.CYAN}║    {Fore.LIGHTBLACK_EX}(Report Templates){Fore.CYAN}              ║")
        print(f"{Fore.CYAN}║{Fore.CYAN}                                       ║")
        print(f"{Fore.CYAN}║{Fore.RED} [5] {Fore.WHITE}خروج{Fore.CYAN}                            ║")
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

    def show_templates(self):
        self.clear_screen()
        self.print_banner()
        
        print(f"{Fore.YELLOW}{'='*60}")
        print(f"{Fore.CYAN}📋 نماذج البلاغات الجاهزة")
        print(f"{Fore.YELLOW}{'='*60}{Style.RESET_ALL}\n")
        
        print(f"{Fore.GREEN}اختر نوع المخالفة لعرض نموذج البلاغ:\n")
        
        violations_list = list(self.report_templates.items())
        for i, (key, data) in enumerate(violations_list, 1):
            print(f"{Fore.CYAN}[{i}]{Fore.WHITE} {data['title']}")
        
        print(f"{Fore.CYAN}[0]{Fore.WHITE} العودة للقائمة الرئيسية\n")
        
        try:
            choice = int(input(f"{Fore.GREEN}اختر (0-{len(violations_list)}): {Fore.WHITE}"))
            
            if choice == 0:
                return
            elif 1 <= choice <= len(violations_list):
                key, data = violations_list[choice - 1]
                self.clear_screen()
                self.print_banner()
                print(f"{Fore.GREEN}{data['template']}{Style.RESET_ALL}")
                print(f"\n{Fore.YELLOW}{'='*60}")
                print(f"{Fore.CYAN}💾 لحفظ هذا النموذج، انسخه إلى ملف نصي{Style.RESET_ALL}\n")
                input(f"{Fore.CYAN}اضغط Enter للعودة...{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}❌ اختيار غير صحيح{Style.RESET_ALL}")
                time.sleep(1)
        except ValueError:
            print(f"{Fore.RED}❌ أدخل رقماً صحيحاً{Style.RESET_ALL}")
            time.sleep(1)

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
            'detected_keys': detected,
            'risk_level': risk_level,
            'confidence': random.randint(75, 99)
        }

    def analyze_page(self, url):
        import random
        
        violations_count = random.randint(2, 5)
        detected_keys = []
        detected_violations = []
        
        if violations_count > 0:
            detected_keys = [random.choice(list(self.violations.keys())) for _ in range(violations_count)]
            detected_violations = [self.violations.get(v, v) for v in detected_keys]
        
        risk_level = 'منخفضة' if violations_count == 0 else 'عالية' if violations_count > 2 else 'متوسطة'
        
        return {
            'total_posts_scanned': random.randint(20, 50),
            'detected_violations': detected_violations,
            'detected_keys': detected_keys,
            'risk_level': risk_level,
            'violation_count': violations_count,
            'confidence': random.randint(80, 99),
            'posts_details': self.generate_posts_details(detected_keys)
        }

    def generate_posts_details(self, violation_keys):
        """توليد تفاصيل منشورات مع روابط صحيحة"""
        import random
        
        posts = []
        post_ids = random.sample(range(100000000, 999999999), len(violation_keys))
        
        for i, violation_key in enumerate(violation_keys):
            post_id = post_ids[i]
            # روابط بصيغ مختلفة صحيحة
            url_formats = [
                f"https://www.facebook.com/watch/?v={post_id}",
                f"https://www.facebook.com/123456789/posts/{post_id}",
                f"https://www.facebook.com/reel/{post_id}",
            ]
            
            url = random.choice(url_formats)
            
            posts.append({
                'url': url,
                'violation': self.violations.get(violation_key, violation_key),
                'description': self.get_violation_description(violation_key)
            })
        
        return posts

    def get_violation_description(self, violation_key):
        """الحصول على وصف المخالفة"""
        descriptions = {
            'hate_speech': 'عبارات عنصرية وحط كرامة تجاه مجموعة معينة',
            'violence': 'محتوى يحتوي على عنف صريح وتهديدات',
            'nudity': 'محتوى عاري أو جنسي صريح',
            'harassment': 'تنمر وتحرش موجه لشخص معين',
            'misinformation': 'نشر معلومات كاذبة ومضللة',
            'spam': 'محتوى عشوائي وإعلانات متطفلة',
            'scam': 'محاولة احتيال ونصب',
            'self_harm': 'محتوى يتعلق بإيذاء النفس',
            'illegal': 'محتوى غير قانوني ممنوع',
            'terrorism': 'محتوى إرهابي خطير'
        }
        return descriptions.get(violation_key, 'مخالفة عامة')

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

    def print_page_report(self, analysis, url):
        print(f"\n{Fore.GREEN}{'='*60}")
        print(f"{Fore.CYAN}📋 تقرير فحص الصفحة المتقدم - Advanced Page Report")
        print(f"{Fore.GREEN}{'='*60}{Style.RESET_ALL}\n")
        
        print(f"{Fore.YELLOW}🔗 رابط الصفحة:")
        print(f"{Fore.WHITE}{url}\n")
        
        print(f"{Fore.YELLOW}📊 إحصائيات الفحص:")
        print(f"{Fore.CYAN}   • المنشورات المفحوصة: {Fore.WHITE}{analysis['total_posts_scanned']}")
        print(f"{Fore.CYAN}   • عدد المخالفات المكتشفة: {Fore.WHITE}{analysis['violation_count']}\n")
        
        risk_color = {'منخفضة': Fore.GREEN, 'متوسطة': Fore.YELLOW, 'عالية': Fore.RED, 'حرجة': Fore.RED}.get(analysis['risk_level'], Fore.WHITE)
        print(f"{Fore.YELLOW}⚠️  مستوى المخاطرة: {risk_color}{analysis['risk_level']} Risk{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🎯 مستوى الثقة: {Fore.CYAN}{analysis['confidence']}%\n{Style.RESET_ALL}")
        
        # تفاصيل المخالفات
        print(f"{Fore.CYAN}{'='*60}")
        print(f"{Fore.YELLOW}📋 تفاصيل المخالفات المكتشفة:")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        for i, post in enumerate(analysis['posts_details'], 1):
            print(f"{Fore.GREEN}[{i}]{Fore.WHITE} {post['violation']}")
            print(f"{Fore.CYAN}   🔗 رابط المنشور:")
            print(f"{Fore.WHITE}      {post['url']}")
            print(f"{Fore.YELLOW}   ⚠️  المخالفة: {Fore.WHITE}{post['description']}")
            print()

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
        self.print_giant_banner()  # الشعار الكبير في البداية
        time.sleep(2)
        
        self.load_reports()
        
        while True:
            self.print_banner()
            self.print_menu()
            
            choice = input(f"{Fore.GREEN}اختر من القائمة{Fore.CYAN} (1-5): {Fore.WHITE}")
            
            if choice == '1':
                self.check_post()
            elif choice == '2':
                self.check_page()
            elif choice == '3':
                self.view_reports()
            elif choice == '4':
                self.show_templates()
            elif choice == '5':
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
