#!/usr/bin/python
# The Arabic-Python language keywords and their English equivalents
keywords = {'قائمة':'list','صفي':'filter','لامدا':'lambda','اطبع':'print', 'و':'and','مثل':'as',
'تاكد':'assert','توقف':'break','صنف':'class','استمر':'continue', 'و':'and','عرف':'def',
'احذف':'del', 'ولاذا':'elif','والا':'else','سوى':'except','غير_محلي':'nonlocal','اخيرا':'finally','كرر':'for',
'من':'from','عالمي':'global' ,'اذا':'if','استورد':'import','عناصر':'items','داخل':'in','هو':'is','نفي':'not','او':'or','تخطى':'pass',
'ابرز':'raise', 'ارجع':'return','جرب':'try','طالما':'while','خطا':'False','فارغ':'None','صواب':'True',
'مع':'with','احصد':'yield', 'ادخل':'input','افتح':'open','اغلق':'close','اكتب':'write','اقرا':'read','سمي':'rename',
'ازل':'remove','عين':'map', 'نطاق':'range','مطلق':'abs','اسكي':'ascii','ثنائي':'bin','منطقي':'bool','حرف':'chr',
'حقيقي':'float','ستة':'hex', 'صحيح':'int','ثماني':'oct','طول':'len','الاكبر':'max','الاصغر':'min','اس':'pow', 'اساس':'key',
'اعكس':'reversed','اجبر':'round', 'رتب':'sorted','اجمع':'sum','صفوف':'tuple','نوع':'type','كل':'all','اي':'any',
'صف_بايت':'bytearray','بايت':'bytes', 'للاستدعاء':'callable','طريقة_صنف':'classmethod','ترجم':'compile','مركب':'complex',
'احذف_صفة':'delattr','قاموس':'dict','صفات':'dir','باقي':'divmode', 'اسرد':'enumerate','احسب':'eval','نفذ':'exec',
'شكل':'format','جمد':'frozenset','اجلب_صفة':'getattr','عمومي':'globals','يملك_صفة':'hasattr','عنونة':'hash','مساعدة':'help',
'معرف':'id','مثال':'isinstance','صنف_فرعي':'issubclass','بالتوالي':'iter','محلي':'locals','تمثيل_الذاكرة':'memoryview',
'التالي':'next','كائن':'object','رمز':'ord','خاصية':'property','تمثيل':'repr','مجموعة':'set','عين_صفة':'setattr','شرح':'slice',
'ثابتة':'staticmethod','الاعلى':'super','معجم':'vars','اضغط':'zip','ملف':'file','اقرا_سطر':'readline',
'اقرا_اسطر':'readlines', 'افصل':'split','اكتب_اسطر':'writelines','ابحث':'seek','اخبر':'tell','للقراءة':'readable',
'للبحث':'seekable','للكتابة':'writable','جرد':'rstrip', 'اضف':'append','ح_كبير':'upper','ح_صغير':'lower','عد':'count',
'اوجد':'find','استبدل':'replace','ذات':'self', '"ت"':'"w"', '"ق"':'"r"','"ض"':'"a"','ضم':'join'}

# The Arabic-Python language error messages and their English equivalents
errors = {'AssertionError':'جملة التأكيد فشلت','AttributeError':'المتغير لا يدعم الدالة','EOFError':'نهاية غير متوقعة للبرنامج',
'FloatingPointError':'العملية المنفذة على العدد العشري فشلت','GeneratorExit':'تم الخروج من المولد',
'ImportError':'الملف المستورد غير موجود','IndexError':'المؤشر تعدى حدود النطاق','KeyError':'المفتاح غير موجود في القاموس',
'KeyboardInterrupt':'تمت المقاطعة من خلال لوحة المفاتيح','MemoryError':'لا يوجد مكان في الذاكرة','NameError':'المتغير ليس معرف من قبل',
'NotImplementedError':'خطأ غير معرف','OSError':'خطأ من قبل النظام', 'OverflowError':'لا يمكن تمثيل القيمة',
'ReferenceError':'خطأ في المرجع', 'RuntimeError':'خطا في التنفيذ','StopIteration':'تم توقف التكرار',
'SyntaxError':'خطا في بناء الجملة','IndentationError':'استخدام غير صحيح للمسافة البادئة','TabError':'المسافات البادئة غير ثابتة',
'SystemError':'خطا داخلي في النظام','SystemExit':'الخروج من النظام', 'FileNotFoundError':'خطأ الملف لم يمكن إيجاده',
 'TypeError':'النوع المستخدم غير صحيح', 'UnboundLocalError':'خطأ استخدام متغير محلي غير معرف','UnicodeError':'خطأ في تمثيل اليونيكود',
 'UnicodeEncodeError':'خطأ في تشفير اليونيكود', 'UnicodeDecodeError':'خطأ في فك تشفير اليونيكود',
 'UnicodeTranslateError':'خطأ في ترجمة اليونيكود', 'ValueError':'قيمة المتغير غير صحيحة', 'ZeroDivisionError':'خطأ قسمة على الصفر'}

# The Arabic-Python language math library and their English equivalents
math = {'رياضيات':'math', 'سقف':'ceil', 'نسخ_اشارة':'copysign', 'قيمة_مطلقة':'fabs', 'مضروب':'factorial',
 'ارضية':'floor', 'باقي_القسمة':'fmod', 'جمع':'fsum', 'لانهائي':'isinf', 'اس_هـ':'exp',
 'لغ':'log', 'لغ١٠':'log10', 'اس':'pow', 'جذر':'sqrt', 'قجتا':'acos',
 'قجا':'asin', 'قظا':'atan', 'جتا':'cos', 'جا':'sin', 'ظا':'tan',
 'مسافة_اقليدية':'hypot', 'درجة':'degrees', 'راديان':'radians', 'باي':'pi', 'هـ':'e',
 'اختصر':'trunc', '"لانهائي"':'"inf"'}
