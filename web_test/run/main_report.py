import HTMLTestReportCN
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os


# ==============定义发送邮件==========
import now as now



def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf—8')
    msg['Subject'] = Header("自动化测试报告", 'utf—8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login('858042515@qq.com',  "fjvccbnvicxibdcj")
    smtp.sendmail('858042515@qq.com',  '858042515@qq.com', msg.as_string())
    smtp.quit()
    print("邮件发送成功，请注意查收。")

    # ======查找测试目录，找到最新生成的测试报告文件======
def new_report(test_report):
    lsits = os.listdir(test_report)
    lsits.sort(key=lambda fn: os.path.getmtime(test_report + '\\' + fn))
    file_new = os.path.join(test_report, lsits[-1])
    print(file_new)
    return file_new


if __name__=='__main__':
    test_dir = "D:\\kuangjia\\testcase"
    test_report ="D:\\kuangjia\\report"

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + '\\' + now + 'result.html'

    fp = open(filename,'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                             title="舆情系统自动化测试报告",
                                             description="用例执行情况")
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)








