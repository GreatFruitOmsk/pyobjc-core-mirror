
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
from Foundation import NSData

import sys, os

if sys.version_info[0] != 2:
    def buffer(value):
        if isinstance(value, bytes):
            return value
        return value.encode('latin1')

    long = int

class TestCGDataProvider (TestCase):
    def testTypes(self):
        self.assertIsCFType(CGDataProviderRef)

    def testFunctions(self):
        self.assertIsInstance(CGDataProviderGetTypeID(), (int, long))

        provider = CGDataProviderCreateWithCFData(buffer("data"))
        self.assertIsInstance(provider, CGDataProviderRef)

        fn = "/Library/Documentation/Acknowledgements.rtf"
        if not os.path.exists(fn):
            fn = "/Library/Documentation/Airport Acknowledgements.rtf"
        if not os.path.exists(fn):
            fn = "/Library/Documentation//MacOSXServer/Server Acknowledgments.pdf"

        if not os.path.exists(fn):
            self.fail("Cannot find test file")
           
        url = CFURLCreateWithFileSystemPath(None,
                fn, kCFURLPOSIXPathStyle, False)

        provider = CGDataProviderCreateWithURL(url)
        self.assertIsInstance(provider, CGDataProviderRef)

        provider = CGDataProviderCreateWithFilename(fn.encode('ascii'))
        self.assertIsInstance(provider, CGDataProviderRef)

        v = CGDataProviderRetain(provider)
        self.assertTrue(v is provider)
        CGDataProviderRelease(provider)

        data = CGDataProviderCopyData(provider)
        self.assertIsInstance(data, CFDataRef)

        info = [b"hello world", False]
        def release(info):
            info[-1] = True
        provider = CGDataProviderCreateWithData(info, info[0], len(info[0]), release)
        self.assertIsInstance(provider, CGDataProviderRef)
        del provider

        self.assertTrue(info[-1])



    @expectedFailure
    def testMissing(self):
        self.fail("CGDataProviderCreateSequential") # + callbacks
        self.fail("CGDataProviderCreateDirect") # + callbacks
        self.fail("CGDataProviderCreate") # + callbacks
        self.fail("CGDataProviderCreateDirectAccess") # + callbacks

    @min_os_level('10.13')
    def testFunctions10_13(self):
        CGDataProviderGetInfo

if __name__ == "__main__":
    main()
