import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror, error
from interface.common.log import log


class Email:
    def __init__(self, server, sender, password, receiver, title, message=None, path=None):
        self.title = title
        self.message = message
        self.files = path
        self.msg = MIMEMultipart('related')

        self.server = server
        self.sender = sender
        self.receiver = receiver
        self.password = password

        def _attach_file(self, att_file):

            att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
            att['Content-Type'] = 'application/octet-stream'
            file_name = re.split(r'[\\|/]', att_file)
            att["Content-Disposition"] = 'attachment; filename="%s"' % file_name[-1]
            self.msg.attach(att)
            logger.info('attach file{}'.format(att_file))

        def send(self):
            self.msg['Subject'] = self.title
            self.msg['From'] = self.sender
            self.msg['To'] = self.receiver

            # 邮件正文
            if self.message:
                self.msg.attach(MIMEText(self.message))

            if self.files:
                if isinstance(self.files, list):
                    for f in self.files:
                        self._attach_file(f)
                elif isinstance(self.files, str):
                    self._attach_file(self.files)

            try:
                smtp_server = smtplib.SMTP(self.server)
            except (gaierror and error) as e:
                logger.exception('发送邮件失败,无法连接到SMTP服务器，检查网络以及SMTP服务器. %s', e)
            else:
                try:
                    smtp_server.login(self.sender, self.password)
                except smtplib.SMTPAuthenticationError as e:
                    logger.exception('用户名密码验证失败！%s', e)
                else:
                    smtp_server.sendmail(self.sender, self.receiver.split(';'), self.as_string())
                finally:
                    smtp_server.quit()
                    logger.info('发送邮件"{0}"成功! 收件人：{1}。如果没有收到邮件，请检查垃圾箱，'
                                '同时检查收件人地址是否正确'.format(self.title, self.receiver))
