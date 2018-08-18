from PyObjCTools.TestSupport import *

import CoreServices

class TestMacMemory (TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(not hasattr(CoreServices, name), "%r exposed in bindings"%(name,))

    def test_not_wrapped(self):
        self.assert_not_wrapped('kMacMemoryMaximumMemoryManagerBlockSize')
        self.assert_not_wrapped('maxSize')
        self.assert_not_wrapped('defaultPhysicalEntryCount')
        self.assert_not_wrapped('kPageInMemory')
        self.assert_not_wrapped('kPageOnDisk')
        self.assert_not_wrapped('kNotPaged')
        self.assert_not_wrapped('k32BitHeap')
        self.assert_not_wrapped('kNewStyleHeap')
        self.assert_not_wrapped('kNewDebugHeap')
        self.assert_not_wrapped('kHandleIsResourceBit')
        self.assert_not_wrapped('kHandlePurgeableBit')
        self.assert_not_wrapped('kHandleLockedBit')
        self.assert_not_wrapped('kHandleIsResourceMask')
        self.assert_not_wrapped('kHandlePurgeableMask')
        self.assert_not_wrapped('kHandleLockedMask')
        self.assert_not_wrapped('Zone')
        self.assert_not_wrapped('MemoryBlock')
        self.assert_not_wrapped('LogicalToPhysicalTable')
        self.assert_not_wrapped('kVolumeVirtualMemoryInfoVersion1')
        self.assert_not_wrapped('VolumeVirtualMemoryInfo')
        self.assert_not_wrapped('NewGrowZoneUPP')
        self.assert_not_wrapped('NewPurgeUPP')
        self.assert_not_wrapped('NewUserFnUPP')
        self.assert_not_wrapped('DisposeGrowZoneUPP')
        self.assert_not_wrapped('DisposePurgeUPP')
        self.assert_not_wrapped('DisposeUserFnUPP')
        self.assert_not_wrapped('InvokeGrowZoneUPP')
        self.assert_not_wrapped('InvokePurgeUPP')
        self.assert_not_wrapped('InvokeUserFnUPP')
        self.assert_not_wrapped('NewGrowZoneUPP')
        self.assert_not_wrapped('NewPurgeUPP')
        self.assert_not_wrapped('NewUserFnUPP')
        self.assert_not_wrapped('DisposeGrowZoneUPP')
        self.assert_not_wrapped('DisposePurgeUPP')
        self.assert_not_wrapped('DisposeUserFnUPP')
        self.assert_not_wrapped('InvokeGrowZoneUPP')
        self.assert_not_wrapped('InvokePurgeUPP')
        self.assert_not_wrapped('InvokeUserFnUPP')
        self.assert_not_wrapped('MemError')
        self.assert_not_wrapped('LMGetMemErr')
        self.assert_not_wrapped('LMSetMemErr')
        self.assert_not_wrapped('NewHandle')
        self.assert_not_wrapped('NewHandleClear')
        self.assert_not_wrapped('RecoverHandle')
        self.assert_not_wrapped('NewPtr')
        self.assert_not_wrapped('NewPtrClear')
        self.assert_not_wrapped('MaxBlock')
        self.assert_not_wrapped('StackSpace')
        self.assert_not_wrapped('NewEmptyHandle')
        self.assert_not_wrapped('HLock')
        self.assert_not_wrapped('HLockHi')
        self.assert_not_wrapped('HUnlock')
        self.assert_not_wrapped('HPurge')
        self.assert_not_wrapped('HNoPurge')
        self.assert_not_wrapped('TempNewHandle')
        self.assert_not_wrapped('TempMaxMem')
        self.assert_not_wrapped('TempFreeMem')
        self.assert_not_wrapped('CompactMem')
        self.assert_not_wrapped('PurgeMem')
        self.assert_not_wrapped('FreeMem')
        self.assert_not_wrapped('MaxMem')
        self.assert_not_wrapped('SetGrowZone')
        self.assert_not_wrapped('GetGrowZone')
        self.assert_not_wrapped('MoveHHi')
        self.assert_not_wrapped('DisposePtr')
        self.assert_not_wrapped('GetPtrSize')
        self.assert_not_wrapped('SetPtrSize')
        self.assert_not_wrapped('DisposeHandle')
        self.assert_not_wrapped('SetHandleSize')
        self.assert_not_wrapped('GetHandleSize')
        self.assert_not_wrapped('ReallocateHandle')
        self.assert_not_wrapped('EmptyHandle')
        self.assert_not_wrapped('HSetRBit')
        self.assert_not_wrapped('HClrRBit')
        self.assert_not_wrapped('HGetState')
        self.assert_not_wrapped('HSetState')
        self.assert_not_wrapped('BlockMove')
        self.assert_not_wrapped('BlockMoveData')
        self.assert_not_wrapped('BlockMoveUncached')
        self.assert_not_wrapped('BlockMoveDataUncached')
        self.assert_not_wrapped('BlockZero')
        self.assert_not_wrapped('BlockZeroUncached')
        self.assert_not_wrapped('HandToHand')
        self.assert_not_wrapped('PtrToXHand')
        self.assert_not_wrapped('PtrToHand')
        self.assert_not_wrapped('HandAndHand')
        self.assert_not_wrapped('PtrAndHand')
        self.assert_not_wrapped('MoreMasters')
        self.assert_not_wrapped('MoreMasterPointers')
        self.assert_not_wrapped('TempHLock')
        self.assert_not_wrapped('TempHUnlock')
        self.assert_not_wrapped('TempDisposeHandle')
        self.assert_not_wrapped('TempTopMem')
        self.assert_not_wrapped('HoldMemory')
        self.assert_not_wrapped('UnholdMemory')
        self.assert_not_wrapped('MakeMemoryResident')
        self.assert_not_wrapped('ReleaseMemoryData')
        self.assert_not_wrapped('MakeMemoryNonResident')
        self.assert_not_wrapped('FlushMemory')
        self.assert_not_wrapped('GZSaveHnd')
        self.assert_not_wrapped('TopMem')
        self.assert_not_wrapped('ReserveMem')
        self.assert_not_wrapped('PurgeSpace')
        self.assert_not_wrapped('PurgeSpaceTotal')
        self.assert_not_wrapped('PurgeSpaceContiguous')
        self.assert_not_wrapped('CheckAllHeaps')
        self.assert_not_wrapped('IsHeapValid')
        self.assert_not_wrapped('IsHandleValid')
        self.assert_not_wrapped('IsPointerValid')
        self.assert_not_wrapped('ApplicZone')
        self.assert_not_wrapped('MFTempNewHandle')
        self.assert_not_wrapped('MFMaxMem')
        self.assert_not_wrapped('MFFreeMem')
        self.assert_not_wrapped('MFTempHLock')
        self.assert_not_wrapped('MFTempHUnlock')
        self.assert_not_wrapped('MFTempDisposHandle')
        self.assert_not_wrapped('MFTopMem')
        self.assert_not_wrapped('ResrvMem')
        self.assert_not_wrapped('DisposPtr')
        self.assert_not_wrapped('DisposHandle')
        self.assert_not_wrapped('ReallocHandle')
        self.assert_not_wrapped('LMGetSysZone')
        self.assert_not_wrapped('LMSetSysZone')
        self.assert_not_wrapped('LMGetApplZone')
        self.assert_not_wrapped('LMSetApplZone')
        self.assert_not_wrapped('HLock')
        self.assert_not_wrapped('HLockHi')
        self.assert_not_wrapped('HUnlock')
        self.assert_not_wrapped('HSetRBit')
        self.assert_not_wrapped('HClrRBit')
        self.assert_not_wrapped('HGetState')
        self.assert_not_wrapped('HSetState')
        self.assert_not_wrapped('HPurge')
        self.assert_not_wrapped('HNoPurge')
        self.assert_not_wrapped('MoveHHi')
        self.assert_not_wrapped('TempHLock')
        self.assert_not_wrapped('TempHUnlock')
        self.assert_not_wrapped('HoldMemory')
        self.assert_not_wrapped('UnholdMemory')
        self.assert_not_wrapped('MakeMemoryResident')
        self.assert_not_wrapped('ReleaseMemoryData')
        self.assert_not_wrapped('MakeMemoryNonResident')
        self.assert_not_wrapped('FlushMemory')
        self.assert_not_wrapped('ReserveMem')
        self.assert_not_wrapped('PurgeSpace')
        self.assert_not_wrapped('PurgeSpaceTotal')
        self.assert_not_wrapped('PurgeSpaceContiguous')



if __name__ == "__main__":
    main()
