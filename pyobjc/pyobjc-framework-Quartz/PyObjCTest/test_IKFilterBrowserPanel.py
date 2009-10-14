
from PyObjCTools.TestSupport import *
from Quartz import *

class TestIKFilterBrowserPanel (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.failUnlessArgIsSEL(IKFilterBrowserPanel.beginWithOptions_modelessDelegate_didEndSelector_contextInfo_, 2, "v@:@i^v")
        self.failUnlessArgIsSEL(IKFilterBrowserPanel.beginSheetWithOptions_modalForWindow_modalDelegate_didEndSelector_contextInfo_, 3, "v@:@i^v")

    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(IKFilterBrowserFilterSelectedNotification, unicode)
        self.failUnlessIsInstance(IKFilterBrowserFilterDoubleClickNotification, unicode)
        self.failUnlessIsInstance(IKFilterBrowserWillPreviewFilterNotification, unicode)
        self.failUnlessIsInstance(IKFilterBrowserShowCategories, unicode)
        self.failUnlessIsInstance(IKFilterBrowserShowPreview, unicode)
        self.failUnlessIsInstance(IKFilterBrowserExcludeCategories, unicode)
        self.failUnlessIsInstance(IKFilterBrowserExcludeFilters, unicode)
        self.failUnlessIsInstance(IKFilterBrowserDefaultInputImage, unicode)

if __name__ == "__main__":
    main()
