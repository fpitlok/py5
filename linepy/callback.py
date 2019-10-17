# -*- coding: utf-8 -*-
class Callback(object):

    def __init__(self, callback):
        self.callback = callback

    def PinVerified(self, pin):
        self.callback("Input this PIN code '" + pin + "' on your LINE for smartphone in 2 minutes")

    def QrUrl(self, url, showQr=True):
        if showQr:
            notice='or scan this QR '
        else:
            notice=''
        self.callback('\nF - ʙᴏᴛʟɪɴᴇ'+ notice +'\n╚=========================================\n\n❋► Coppy ลิ้งภายใน 2 นาทีครับ \n\n🔊 LINK LOGIN BOT : '+ url+ '\n\n\n╔══════════════════════════┓\nF - ʙᴏᴛʟɪɴᴇ\n╚══════════════════════════┛')
        if showQr:
            try:
                import pyqrcode
                url = pyqrcode.create(url)
                self.callback(url.terminal('green', 'white', 1))
            except:
                pass

    def default(self, str):
        self.callback(str)
