from pywebio import start_server
from pywebio.input import input, FLOAT
from pywebio.output import put_text
from pywebio.session import *
from pywebio.pin import *
import requests
from sympy import symbols, Eq, pretty
#____________________________________________________
def send_message_to_telegram(message):
    token ='7733635367:AAHtRSVkBm2V_p3DALb9-kkR76ToBr0XovI'
    groupId = "mathematics_py"
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=@{groupId}&text={message}'
    res = requests.get(url)
    if res.status_code == 200:
        put_text("تم إرسال الرسالة بنجاح إلى Telegram.")
    else:
        put_text("حدث خطأ أثناء إرسال الرسالة.")
#__________________________________________________________
def mopasher():
    nam=input("اسمك ال هيظهر في البوت")
    num1 = input("أدخل الرقم الأول:", type=FLOAT)
    num2 = input("أدخل الرقم الثاني:", type=FLOAT)
    
    # حساب المجموع
    dal = num1 * num2
    oss= num2-1
    x=symbols(f"{dal}x")
    osss=x**oss
    # إرسال النتيجة إلى Telegram
    message = (f"""
               welcome:{nam}
حل المعادله هو:
               {(pretty(osss))}
               """)
    send_message_to_telegram(message)
#_____________________________________________________________
def Dala_kosen():
    nam=input("اسمك ال هيظهر في البوت")
    num1 = input("أدخل الرقم الي قبل الاكس:", type=FLOAT)
    num2 = input("أدخل الاس الي فوق الاكس :", type=FLOAT)
    num3 = input("أدخل الرقم الاس الي فوق القوس:", type=FLOAT)
    # حساب المجموع
    nmp3=num3-1
    nmp2=num2*num1
    nmp1=num2-1    
    # إرسال النتيجة إلى Telegram
    message = (f"""
welcome({nam})
الحل
{nmp3}({num1}X{num2})
""")
    send_message_to_telegram(message)
#___________________________________________________________________
def about():
    put_text("""
             

             1(اولا اختيار نوعيه التفاضل المطلوبه


             2(الرقم الي بعدالاكس ف هو الاس 


             3(ازا كان الرقم الاس 0 ف اكتب في خانه الاس1


             4((mathematics_py)الاجابات يرسلها اليوت مباشرتا الي هزا الجروب


             """).style("background-color:black;color:#FF0303;font-weight:bold; padding:18px;")
#_______________________________________________________________________
def gazr_zer():
    # طلب الرقمين من المستخدم
    num1 = input("أدخل الرقم الي قبل الاكس:", type=FLOAT)
    num2 = input("أدخل الرقم الي بعد الاكس:", type=FLOAT)
    # حساب المجموع
    tbset=(f"({num1}X{num2})1.5")
    tfadl=(f"1.5({num1}X{num2}-1.5)({num1*num2}X{num2-1})")
    # إرسال النتيجة إلى Telegram
    message = (f"""
               الحل
               تبسيط المساله:
               {tbset}
               حل المساله:
               {tfadl}
               """)
    send_message_to_telegram(message)
#_______________________________________________________________________
def main():
    # طلب الرقمين من المستخدم
    num1 = input("أدخل الرقم الأول:", type=FLOAT)
    num2 = input("أدخل الرقم الثاني:", type=FLOAT)
    
    # حساب المجموع
    dal = num1 + num2
    
    # إرسال النتيجة إلى Telegram
    message = f"مجموع العددين {num1} و {num2} هو: {dal}"
    send_message_to_telegram(message)
#_____________________________________________________________________________
def main():
    # طلب الرقمين من المستخدم
    num1 = input("أدخل الرقم الأول:", type=FLOAT)
    num2 = input("أدخل الرقم الثاني:", type=FLOAT)
    
    # حساب المجموع
    dal = num1 + num2
    
    # إرسال النتيجة إلى Telegram
    message = f"مجموع العددين {num1} و {num2} هو: {dal}"
    send_message_to_telegram(message)
#____________________________________________________________________________


if __name__ == '__main__':
    start_server([about, mopasher, Dala_kosen, gazr_zer], port=8080)