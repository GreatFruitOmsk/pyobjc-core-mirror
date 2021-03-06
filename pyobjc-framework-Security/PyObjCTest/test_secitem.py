
from PyObjCTools.TestSupport import *

import Security

class TestAuthorizationDB (TestCase):

    @min_os_level('10.7')
    def test_constants_10_6(self):
        self.assertIsInstance(Security.kSecClass, unicode)
        self.assertIsInstance(Security.kSecClassInternetPassword, unicode)
        self.assertIsInstance(Security.kSecAttrCreationDate, unicode)
        self.assertIsInstance(Security.kSecAttrModificationDate, unicode)
        self.assertIsInstance(Security.kSecAttrDescription, unicode)
        self.assertIsInstance(Security.kSecAttrComment, unicode)
        self.assertIsInstance(Security.kSecAttrCreator, unicode)
        self.assertIsInstance(Security.kSecAttrType, unicode)
        self.assertIsInstance(Security.kSecAttrLabel, unicode)
        self.assertIsInstance(Security.kSecAttrIsInvisible, unicode)
        self.assertIsInstance(Security.kSecAttrIsNegative, unicode)
        self.assertIsInstance(Security.kSecAttrAccount, unicode)
        self.assertIsInstance(Security.kSecAttrService, unicode)
        self.assertIsInstance(Security.kSecAttrGeneric, unicode)
        self.assertIsInstance(Security.kSecAttrSecurityDomain, unicode)
        self.assertIsInstance(Security.kSecAttrServer, unicode)
        self.assertIsInstance(Security.kSecAttrProtocol, unicode)
        self.assertIsInstance(Security.kSecAttrAuthenticationType, unicode)
        self.assertIsInstance(Security.kSecAttrPort, unicode)
        self.assertIsInstance(Security.kSecAttrPath, unicode)
        self.assertIsInstance(Security.kSecAttrSubject, unicode)
        self.assertIsInstance(Security.kSecAttrIssuer, unicode)
        self.assertIsInstance(Security.kSecAttrSerialNumber, unicode)
        self.assertIsInstance(Security.kSecAttrSubjectKeyID, unicode)
        self.assertIsInstance(Security.kSecAttrPublicKeyHash, unicode)
        self.assertIsInstance(Security.kSecAttrCertificateType, unicode)
        self.assertIsInstance(Security.kSecAttrCertificateEncoding, unicode)
        self.assertIsInstance(Security.kSecAttrKeyClass, unicode)
        self.assertIsInstance(Security.kSecAttrApplicationLabel, unicode)
        self.assertIsInstance(Security.kSecAttrIsPermanent, unicode)
        self.assertIsInstance(Security.kSecAttrIsSensitive, unicode)
        self.assertIsInstance(Security.kSecAttrIsExtractable, unicode)
        self.assertIsInstance(Security.kSecAttrApplicationTag, unicode)
        self.assertIsInstance(Security.kSecAttrKeyType, unicode)
        self.assertIsInstance(Security.kSecAttrKeySizeInBits, unicode)
        self.assertIsInstance(Security.kSecAttrEffectiveKeySize, unicode)
        self.assertIsInstance(Security.kSecAttrCanEncrypt, unicode)
        self.assertIsInstance(Security.kSecAttrCanDecrypt, unicode)
        self.assertIsInstance(Security.kSecAttrCanDerive, unicode)
        self.assertIsInstance(Security.kSecAttrCanSign, unicode)
        self.assertIsInstance(Security.kSecAttrCanVerify, unicode)
        self.assertIsInstance(Security.kSecAttrCanWrap, unicode)
        self.assertIsInstance(Security.kSecAttrCanUnwrap, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolFTP, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolFTPAccount, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolHTTP, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolIRC, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolNNTP, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolPOP3, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolSMTP, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolSOCKS, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolIMAP, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolLDAP, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolAppleTalk, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolAFP, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolTelnet, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolSSH, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolFTPS, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolHTTPS, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolHTTPProxy, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolHTTPSProxy, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolFTPProxy, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolSMB, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolRTSP, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolRTSPProxy, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolDAAP, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolEPPC, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolIPP, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolNNTPS, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolLDAPS, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolTelnetS, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolIMAPS, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolIRCS, unicode)
        self.assertIsInstance(Security.kSecAttrProtocolPOP3S, unicode)
        self.assertIsInstance(Security.kSecAttrAuthenticationTypeNTLM, unicode)
        self.assertIsInstance(Security.kSecAttrAuthenticationTypeMSN, unicode)
        self.assertIsInstance(Security.kSecAttrAuthenticationTypeDPA, unicode)
        self.assertIsInstance(Security.kSecAttrAuthenticationTypeRPA, unicode)
        self.assertIsInstance(Security.kSecAttrAuthenticationTypeHTTPBasic, unicode)
        self.assertIsInstance(Security.kSecAttrAuthenticationTypeHTTPDigest, unicode)
        self.assertIsInstance(Security.kSecAttrAuthenticationTypeHTMLForm, unicode)
        self.assertIsInstance(Security.kSecAttrAuthenticationTypeDefault, unicode)
        self.assertIsInstance(Security.kSecMatchPolicy, unicode)
        self.assertIsInstance(Security.kSecMatchItemList, unicode)
        self.assertIsInstance(Security.kSecMatchSearchList, unicode)
        self.assertIsInstance(Security.kSecMatchIssuers, unicode)
        self.assertIsInstance(Security.kSecMatchEmailAddressIfPresent, unicode)
        self.assertIsInstance(Security.kSecMatchSubjectContains, unicode)
        self.assertIsInstance(Security.kSecMatchTrustedOnly, unicode)
        self.assertIsInstance(Security.kSecMatchValidOnDate, unicode)
        self.assertIsInstance(Security.kSecMatchLimit, unicode)
        self.assertIsInstance(Security.kSecMatchLimitOne, unicode)
        self.assertIsInstance(Security.kSecMatchLimitAll, unicode)
        self.assertIsInstance(Security.kSecReturnData, unicode)
        self.assertIsInstance(Security.kSecReturnAttributes, unicode)
        self.assertIsInstance(Security.kSecReturnRef, unicode)
        self.assertIsInstance(Security.kSecReturnPersistentRef, unicode)
        self.assertIsInstance(Security.kSecValueData, unicode)
        self.assertIsInstance(Security.kSecValueRef, unicode)
        self.assertIsInstance(Security.kSecValuePersistentRef, unicode)
        self.assertIsInstance(Security.kSecUseItemList, unicode)
        self.assertIsInstance(Security.kSecMatchCaseInsensitive, unicode)

    @min_os_level('10.7')
    def test_constants_10_7(self):
        self.assertIsInstance(Security.kSecClassGenericPassword, unicode)
        self.assertIsInstance(Security.kSecClassCertificate, unicode)
        self.assertIsInstance(Security.kSecClassKey, unicode)
        self.assertIsInstance(Security.kSecClassIdentity, unicode)
        self.assertIsInstance(Security.kSecAttrAccess, unicode)
        self.assertIsInstance(Security.kSecAttrPRF, unicode)
        self.assertIsInstance(Security.kSecAttrSalt, unicode)
        self.assertIsInstance(Security.kSecAttrRounds, unicode)
        self.assertIsInstance(Security.kSecAttrKeyClassPublic, unicode)
        self.assertIsInstance(Security.kSecAttrKeyClassPrivate, unicode)
        self.assertIsInstance(Security.kSecAttrKeyClassSymmetric, unicode)
        self.assertIsInstance(Security.kSecAttrKeyTypeRSA, unicode)
        self.assertIsInstance(Security.kSecAttrKeyTypeDSA, unicode)
        self.assertIsInstance(Security.kSecAttrKeyTypeAES, unicode)
        self.assertIsInstance(Security.kSecAttrKeyTypeDES, unicode)
        self.assertIsInstance(Security.kSecAttrKeyType3DES, unicode)
        self.assertIsInstance(Security.kSecAttrKeyTypeRC4, unicode)
        self.assertIsInstance(Security.kSecAttrKeyTypeRC2, unicode)
        self.assertIsInstance(Security.kSecAttrKeyTypeCAST, unicode)
        self.assertIsInstance(Security.kSecAttrKeyTypeECDSA, unicode)
        self.assertIsInstance(Security.kSecAttrPRFHmacAlgSHA1, unicode)
        self.assertIsInstance(Security.kSecAttrPRFHmacAlgSHA224, unicode)
        self.assertIsInstance(Security.kSecAttrPRFHmacAlgSHA256, unicode)
        self.assertIsInstance(Security.kSecAttrPRFHmacAlgSHA384, unicode)
        self.assertIsInstance(Security.kSecAttrPRFHmacAlgSHA512, unicode)
        self.assertIsInstance(Security.kSecMatchSubjectStartsWith, unicode)
        self.assertIsInstance(Security.kSecMatchSubjectEndsWith, unicode)
        self.assertIsInstance(Security.kSecMatchSubjectWholeString, unicode)
        self.assertIsInstance(Security.kSecMatchDiacriticInsensitive, unicode)
        self.assertIsInstance(Security.kSecMatchWidthInsensitive, unicode)
        self.assertIsInstance(Security.kSecUseKeychain, unicode)

    @min_os_level('10.9')
    def test_constants_10_9(self):
        self.assertIsInstance(Security.kSecAttrAccessible, unicode)
        self.assertIsInstance(Security.kSecAttrAccessGroup, unicode)
        self.assertIsInstance(Security.kSecAttrSynchronizable, unicode)
        self.assertIsInstance(Security.kSecAttrSynchronizableAny, unicode)
        self.assertIsInstance(Security.kSecAttrAccessibleWhenUnlocked, unicode)
        self.assertIsInstance(Security.kSecAttrAccessibleAfterFirstUnlock, unicode)
        self.assertIsInstance(Security.kSecAttrAccessibleAlways, unicode)
        self.assertIsInstance(Security.kSecAttrAccessibleWhenUnlockedThisDeviceOnly, unicode)
        self.assertIsInstance(Security.kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly, unicode)
        self.assertIsInstance(Security.kSecAttrAccessibleAlwaysThisDeviceOnly, unicode)
        self.assertIsInstance(Security.kSecAttrKeyTypeEC, unicode)

    @min_os_level('10.10')
    def test_constants_10_10(self):
        self.assertIsInstance(Security.kSecAttrAccessControl, unicode)
        self.assertIsInstance(Security.kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly, unicode)
        self.assertIsInstance(Security.kSecUseOperationPrompt, unicode)
        self.assertIsInstance(Security.kSecUseNoAuthenticationUI, unicode)

    @min_os_level('10.11')
    def test_constants_10_11(self):
        self.assertIsInstance(Security.kSecAttrSyncViewHint, unicode)
        self.assertIsInstance(Security.kSecUseAuthenticationUI, unicode)
        self.assertIsInstance(Security.kSecUseAuthenticationContext, unicode)
        self.assertIsInstance(Security.kSecUseAuthenticationUIAllow, unicode)
        self.assertIsInstance(Security.kSecUseAuthenticationUIFail, unicode)
        self.assertIsInstance(Security.kSecUseAuthenticationUISkip, unicode)

    @min_os_level('10.12')
    def test_constants_10_12(self):
        self.assertIsInstance(Security.kSecAttrTokenID, unicode)
        self.assertIsInstance(Security.kSecAttrKeyTypeECSECPrimeRandom, unicode)
        self.assertIsInstance(Security.kSecAttrTokenIDSecureEnclave, unicode)
        self.assertIsInstance(Security.kSecAttrAccessGroupToken, unicode)

    @min_os_level('10.13')
    def test_constants_10_13(self):
        self.assertIsInstance(Security.kSecAttrPersistantReference, unicode)
        self.assertIsInstance(Security.kSecAttrPersistentReference, unicode)

    @min_os_level('10.6')
    def test_functions(self):
        self.assertResultHasType(Security.SecItemCopyMatching, objc._C_INT)
        self.assertArgHasType(Security.SecItemCopyMatching, 0, objc._C_ID)
        self.assertArgHasType(Security.SecItemCopyMatching, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecItemCopyMatching, 1)

        self.assertResultHasType(Security.SecItemAdd, objc._C_INT)
        self.assertArgHasType(Security.SecItemAdd, 0, objc._C_ID)
        self.assertArgHasType(Security.SecItemAdd, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecItemAdd, 1)

        self.assertResultHasType(Security.SecItemUpdate, objc._C_INT)
        self.assertArgHasType(Security.SecItemUpdate, 0, objc._C_ID)
        self.assertArgHasType(Security.SecItemUpdate, 1, objc._C_ID)

        self.assertResultHasType(Security.SecItemDelete, objc._C_INT)
        self.assertArgHasType(Security.SecItemDelete, 0, objc._C_ID)

if __name__ == "__main__":
    main()
