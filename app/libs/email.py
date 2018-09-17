from threading import Thread

from app import mail
from flask_mail import Message
from flask import current_app, render_template


def send_async_mail(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            raise e


def send_mail(to, subject, template, **kwargs):
    # msg = Message('测试邮件', sender='283618142@qq.com', body='Test',
    #               recipients=['283618142@qq.com'])
    msg = Message(current_app.config['MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()  # 拿到真实flask核心对象
    thr = Thread(target=send_async_mail, args=[app, msg])
    thr.start()

