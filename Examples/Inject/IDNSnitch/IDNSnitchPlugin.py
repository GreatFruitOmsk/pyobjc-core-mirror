from Foundation import *
from AppKit import *
import sys
import encodings.idna
import objc

MESSAGE = u"""An URL using an IDN host has been detected.  URLs of this type may be misleading as there are many characters that look the same.

Display Host
  %s

Unicode Host
  %s

URL
  %s"""

class IDNSnitch(NSObject):
    def init(self):
        super(IDNSnitch, self).init()
        self.HOSTS = {}
        return self

    def runDialog_(self, (res, dialog)):
        res.append(NSRunAlertPanel(*dialog))
        return

    def startIDNSnitch_(self, sender):
        print u'startIDNSnitch:'
        global NSURLRequest
        SEL = 'initWithURL:cachePolicy:timeoutInterval:'
        oldIMP = NSURLRequest.instanceMethodForSelector_(SEL)
        class NSURLRequest(objc.Category(NSURLRequest)):
            def initWithURL_cachePolicy_timeoutInterval_(self, theURL, cachePolicy, timeoutInterval):
                print 'checking', theURL, cachePolicy, timeoutInterval
                try:
                    theURL = idnSnitch.checkURL_(theURL)
                except Exception, e:
                    import traceback
                    traceback.print_exc()
                    NSLog(u"%s: %s" % (e.__class__.__name__, e))
                print 'checked'
                self.retain()
                res = oldIMP(self, theURL, cachePolicy, timeoutInterval)
                print 'got res'
                return res

    def checkURL_(self, anURL):
        print 'checkURL', self, anURL
        if anURL is None:
            return anURL
        host = anURL.host()
        if host is None:
            return anURL
        if encodings.idna.uace_prefix in host:
            uni = u'.'.join([encodings.idna.ToUnicode(part) for part in host.split(u'.')])
            shouldDeny = self.HOSTS.get(uni)
            if shouldDeny is None:
                res = []
                self.performSelectorOnMainThread_withObject_waitUntilDone_(
                    'runDialog:',
                    (
                        res,
                        (
                            u'IDN URL Detected',
                            MESSAGE % (uni, uni.encode('unicode_escape'), anURL),
                            u'Allow',
                            u'Deny',
                            None,
                        ),
                    ),
                    True,
                )
                shouldDeny = res.pop() != NSAlertDefaultReturn
                self.HOSTS[uni] = shouldDeny
            if shouldDeny:
                return NSURL.URLWithString_(u'about:blank')
        return anURL


#from PyObjCTools import Debugging
#Debugging.installVerboseExceptionHandler()
idnSnitch = IDNSnitch.alloc().init()
idnSnitch.performSelectorOnMainThread_withObject_waitUntilDone_('startIDNSnitch:', None, False)
