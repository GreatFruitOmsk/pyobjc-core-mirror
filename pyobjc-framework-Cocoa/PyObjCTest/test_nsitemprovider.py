from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSItemProvider (TestCase):
    def testConstants(self):
        self.assertEqual(NSItemProviderRepresentationVisibilityAll, 0)
        self.assertEqual(NSItemProviderRepresentationVisibilityGroup, 2)
        self.assertEqual(NSItemProviderRepresentationVisibilityOwnProcess, 3)
        self.assertEqual(NSItemProviderFileOptionOpenInPlace, 1)

    @min_os_level('10.10')
    @onlyOn64Bit
    def testConstants10_10(self):
        self.assertIsInstance(NSTypeIdentifierDateText, unicode)
        self.assertIsInstance(NSTypeIdentifierAddressText, unicode)
        self.assertIsInstance(NSTypeIdentifierPhoneNumberText, unicode)
        self.assertIsInstance(NSTypeIdentifierTransitInformationText, unicode)

        self.assertIsInstance(NSItemProviderPreferredImageSizeKey, unicode)
        self.assertIsInstance(NSExtensionJavaScriptPreprocessingResultsKey, unicode)
        self.assertIsInstance(NSItemProviderErrorDomain, unicode)

        self.assertEqual(NSItemProviderUnknownError, -1)
        self.assertEqual(NSItemProviderItemUnavailableError, -1000)
        self.assertEqual(NSItemProviderUnexpectedValueClassError, -1100)

    @min_os_level('10.11')
    @onlyOn64Bit
    def testConstants10_11(self):
        self.assertEqual(NSItemProviderUnavailableCoercionError, -1200)

    @min_os_level('10.10')
    @onlyOn64Bit
    def testMethods10_10(self):
        NSItemProviderCompletionHandler = b'v@@'
        NSItemProviderLoadHandler = b'v@?#@'

        self.assertResultIsBOOL(NSItemProvider.hasItemConformingToTypeIdentifier_)
        self.assertArgIsBlock(NSItemProvider.loadItemForTypeIdentifier_options_completionHandler_, 2, NSItemProviderCompletionHandler)
        self.assertArgIsBlock(NSItemProvider.registerItemForTypeIdentifier_loadHandler_, 1, NSItemProviderLoadHandler)

        self.assertResultIsBlock(NSItemProvider.previewImageHandler, NSItemProviderLoadHandler)
        self.assertArgIsBlock(NSItemProvider.setPreviewImageHandler_, 0, NSItemProviderLoadHandler)
        self.assertArgIsBlock(NSItemProvider.loadPreviewImageWithOptions_completionHandler_, 1, NSItemProviderCompletionHandler)

        # XXX:
        #self.fail("NSItemProviderLoadHandler metadata test")

    @min_os_level('10.13')
    @onlyOn64Bit
    def testMethods10_13(self):
        # XXX: Cannot properly test right now...
        self.assertArgIsBlock(NSItemProvider.registerDataRepresentationForTypeIdentifier_visibility_loadHandler_, 2, b'@@?')
        self.assertArgIsBlock(NSItemProvider.registerFileRepresentationForTypeIdentifier_fileOptions_visibility_loadHandler_, 2, b'@@?')
        self.assertArgIsBlock(NSItemProvider.registerObjectOfClass_visibility_loadHandler_, 2, b'@@?')

        self.assertResultIsBOOL(NSItemProvider.hasRepresentationConformingToTypeIdentifier_fileOptions_)

        self.assertArgIsBlock(NSItemProvider.loadDataRepresentationForTypeIdentifier_completionHandler_, 1, b'v@@')
        self.assertArgIsBlock(NSItemProvider.loadFileRepresentationForTypeIdentifier_completionHandler_, 1, b'v@@')
        self.assertArgIsBlock(NSItemProvider.loadInPlaceFileRepresentationForTypeIdentifier_completionHandler_, 1, b'v@Z@')
        self.assertArgIsBlock(NSItemProvider.loadObjectOfClass_completionHandler_, 1, b'v@@')
        self.assertResultIsBOOL(NSItemProvider.canLoadObjectOfClass_)

        # XXX: Cannot properly test right now...
        self.assertArgIsBlock(NSItemProvider.registerItemForTypeIdentifier_loadHandler_, 2, b'@@?')
        self.assertArgIsBlock(NSItemProvider.loadItemForTypeIdentifier_options_completionHandler_, 2, NSItemProviderCompletionHandler)

if __name__ == "__main__":
    main()
