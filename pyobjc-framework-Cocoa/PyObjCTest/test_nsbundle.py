from PyObjCTools.TestSupport import *

from Foundation import *
import Foundation
import AppKit

class TestNSBundle (TestCase):
    def testMethods(self):
        b = NSBundle.mainBundle()
        # Test on an instance because NSBundle has class methods
        # that interfere with this test
        self.assertResultIsBOOL(b.load)
        self.assertResultIsBOOL(b.isLoaded)
        self.assertResultIsBOOL(b.unload)

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertResultIsBOOL(NSBundle.loadNibNamed_owner_topLevelObjects_)
        self.assertArgIsOut(NSBundle.loadNibNamed_owner_topLevelObjects_, 2)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertResultIsBOOL(NSBundle.preflightAndReturnError_)
        self.assertArgIsOut(NSBundle.preflightAndReturnError_, 0)
        self.assertResultIsBOOL(NSBundle.loadAndReturnError_)
        self.assertArgIsOut(NSBundle.loadAndReturnError_, 0)

    def testConstants(self):
        self.assertEqual(NSBundleExecutableArchitectureI386, 0x00000007)
        self.assertEqual(NSBundleExecutableArchitecturePPC, 0x00000012)
        self.assertEqual(NSBundleExecutableArchitectureX86_64, 0x01000007)
        self.assertEqual(NSBundleExecutableArchitecturePPC64, 0x01000012)

        self.assertIsInstance(NSBundleDidLoadNotification, unicode)
        self.assertIsInstance(NSLoadedClasses, unicode)

    def testDefines(self):
        self.assertHasAttr(Foundation, 'NSLocalizedString')
        self.assertHasAttr(Foundation, 'NSLocalizedStringFromTable')
        self.assertHasAttr(Foundation, 'NSLocalizedStringFromTableInBundle')
        self.assertHasAttr(Foundation, 'NSLocalizedStringWithDefaultValue')

if __name__ == "__main__":
    main()
