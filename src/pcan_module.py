# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
try:
    from . import _pcan_module
except:
    import _pcan_module

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class intArray(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _pcan_module.intArray_swiginit(self, _pcan_module.new_intArray(nelements))
    __swig_destroy__ = _pcan_module.delete_intArray

    def __getitem__(self, index):
        return _pcan_module.intArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _pcan_module.intArray___setitem__(self, index, value)

    def cast(self):
        return _pcan_module.intArray_cast(self)

    @staticmethod
    def frompointer(t):
        return _pcan_module.intArray_frompointer(t)

# Register intArray in _pcan_module:
_pcan_module.intArray_swigregister(intArray)

def intArray_frompointer(t):
    return _pcan_module.intArray_frompointer(t)

CAN_BAUD_1M = _pcan_module.CAN_BAUD_1M
CAN_BAUD_500K = _pcan_module.CAN_BAUD_500K
CAN_BAUD_250K = _pcan_module.CAN_BAUD_250K
CAN_BAUD_125K = _pcan_module.CAN_BAUD_125K
CAN_BAUD_100K = _pcan_module.CAN_BAUD_100K
CAN_BAUD_50K = _pcan_module.CAN_BAUD_50K
CAN_BAUD_20K = _pcan_module.CAN_BAUD_20K
CAN_BAUD_10K = _pcan_module.CAN_BAUD_10K
CAN_BAUD_5K = _pcan_module.CAN_BAUD_5K
CAN_INIT_TYPE_ST = _pcan_module.CAN_INIT_TYPE_ST
CAN_INIT_TYPE_EX = _pcan_module.CAN_INIT_TYPE_EX

def CAN_Open(*args):
    return _pcan_module.CAN_Open(*args)

def CAN_Init(hHandle, wBTR0BTR1, nCANMsgType):
    return _pcan_module.CAN_Init(hHandle, wBTR0BTR1, nCANMsgType)

def CAN_Close(hHandle):
    return _pcan_module.CAN_Close(hHandle)

def CAN_Status(hHandle):
    return _pcan_module.CAN_Status(hHandle)

def CAN_Write(hHandle, pMsgBuff):
    return _pcan_module.CAN_Write(hHandle, pMsgBuff)

def LINUX_CAN_Write_Timeout(hHandle, pMsgBuff, nMicroSeconds):
    return _pcan_module.LINUX_CAN_Write_Timeout(hHandle, pMsgBuff, nMicroSeconds)

def CAN_Read(hHandle, pMsgBuff):
    return _pcan_module.CAN_Read(hHandle, pMsgBuff)

def LINUX_CAN_Read(hHandle, pMsgBuff):
    return _pcan_module.LINUX_CAN_Read(hHandle, pMsgBuff)

def LINUX_CAN_Read_Timeout(hHandle, pMsgBuff, nMicroSeconds):
    return _pcan_module.LINUX_CAN_Read_Timeout(hHandle, pMsgBuff, nMicroSeconds)

def CAN_ResetFilter(hHandle):
    return _pcan_module.CAN_ResetFilter(hHandle)

def CAN_MsgFilter(hHandle, FromID, ToID, nCANMsgType):
    return _pcan_module.CAN_MsgFilter(hHandle, FromID, ToID, nCANMsgType)

def LINUX_CAN_FileHandle(hHandle):
    return _pcan_module.LINUX_CAN_FileHandle(hHandle)

def LINUX_CAN_Extended_Status(hHandle, nPendingReads, nPendingWrites):
    return _pcan_module.LINUX_CAN_Extended_Status(hHandle, nPendingReads, nPendingWrites)

def CAN_VersionInfo(hHandle, lpszTextBuff):
    return _pcan_module.CAN_VersionInfo(hHandle, lpszTextBuff)

def nGetLastError():
    return _pcan_module.nGetLastError()

def LINUX_CAN_Open(szDeviceName, nFlag):
    return _pcan_module.LINUX_CAN_Open(szDeviceName, nFlag)

def LINUX_CAN_Statistics(hHandle, diag):
    return _pcan_module.LINUX_CAN_Statistics(hHandle, diag)

def LINUX_CAN_BTR0BTR1(hHandle, dwBitRate):
    return _pcan_module.LINUX_CAN_BTR0BTR1(hHandle, dwBitRate)
HW_ISA = _pcan_module.HW_ISA
HW_DONGLE_SJA = _pcan_module.HW_DONGLE_SJA
HW_DONGLE_SJA_EPP = _pcan_module.HW_DONGLE_SJA_EPP
HW_DONGLE_PRO = _pcan_module.HW_DONGLE_PRO
HW_DONGLE_PRO_EPP = _pcan_module.HW_DONGLE_PRO_EPP
HW_ISA_SJA = _pcan_module.HW_ISA_SJA
HW_PCI = _pcan_module.HW_PCI
HW_USB = _pcan_module.HW_USB
HW_PCCARD = _pcan_module.HW_PCCARD
HW_USB_PRO = _pcan_module.HW_USB_PRO
HW_USB_PRO_FD = _pcan_module.HW_USB_PRO_FD
HW_USB_FD = _pcan_module.HW_USB_FD
HW_PCI_FD = _pcan_module.HW_PCI_FD
HW_USB_X6 = _pcan_module.HW_USB_X6
CAN_MAX_STANDARD_ID = _pcan_module.CAN_MAX_STANDARD_ID
CAN_MAX_EXTENDED_ID = _pcan_module.CAN_MAX_EXTENDED_ID
CAN_ERR_OK = _pcan_module.CAN_ERR_OK
CAN_ERR_XMTFULL = _pcan_module.CAN_ERR_XMTFULL
CAN_ERR_OVERRUN = _pcan_module.CAN_ERR_OVERRUN
CAN_ERR_BUSLIGHT = _pcan_module.CAN_ERR_BUSLIGHT
CAN_ERR_BUSHEAVY = _pcan_module.CAN_ERR_BUSHEAVY
CAN_ERR_BUSOFF = _pcan_module.CAN_ERR_BUSOFF
CAN_ERR_QRCVEMPTY = _pcan_module.CAN_ERR_QRCVEMPTY
CAN_ERR_QOVERRUN = _pcan_module.CAN_ERR_QOVERRUN
CAN_ERR_QXMTFULL = _pcan_module.CAN_ERR_QXMTFULL
CAN_ERR_REGTEST = _pcan_module.CAN_ERR_REGTEST
CAN_ERR_NOVXD = _pcan_module.CAN_ERR_NOVXD
CAN_ERR_RESOURCE = _pcan_module.CAN_ERR_RESOURCE
CAN_ERR_ILLPARAMTYPE = _pcan_module.CAN_ERR_ILLPARAMTYPE
CAN_ERR_ILLPARAMVAL = _pcan_module.CAN_ERR_ILLPARAMVAL
CAN_ERRMASK_ILLHANDLE = _pcan_module.CAN_ERRMASK_ILLHANDLE
MSGTYPE_STANDARD = _pcan_module.MSGTYPE_STANDARD
MSGTYPE_RTR = _pcan_module.MSGTYPE_RTR
MSGTYPE_EXTENDED = _pcan_module.MSGTYPE_EXTENDED
MSGTYPE_SELFRECEIVE = _pcan_module.MSGTYPE_SELFRECEIVE
MSGTYPE_STATUS = _pcan_module.MSGTYPE_STATUS
VERSIONSTRING_LEN = _pcan_module.VERSIONSTRING_LEN
class TPCANInit(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    wBTR0BTR1 = property(_pcan_module.TPCANInit_wBTR0BTR1_get, _pcan_module.TPCANInit_wBTR0BTR1_set)
    ucCANMsgType = property(_pcan_module.TPCANInit_ucCANMsgType_get, _pcan_module.TPCANInit_ucCANMsgType_set)
    ucListenOnly = property(_pcan_module.TPCANInit_ucListenOnly_get, _pcan_module.TPCANInit_ucListenOnly_set)

    def __init__(self):
        _pcan_module.TPCANInit_swiginit(self, _pcan_module.new_TPCANInit())
    __swig_destroy__ = _pcan_module.delete_TPCANInit

# Register TPCANInit in _pcan_module:
_pcan_module.TPCANInit_swigregister(TPCANInit)

class TPCANMsg(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ID = property(_pcan_module.TPCANMsg_ID_get, _pcan_module.TPCANMsg_ID_set)
    MSGTYPE = property(_pcan_module.TPCANMsg_MSGTYPE_get, _pcan_module.TPCANMsg_MSGTYPE_set)
    LEN = property(_pcan_module.TPCANMsg_LEN_get, _pcan_module.TPCANMsg_LEN_set)
    DATA = property(_pcan_module.TPCANMsg_DATA_get, _pcan_module.TPCANMsg_DATA_set)

    def __init__(self):
        _pcan_module.TPCANMsg_swiginit(self, _pcan_module.new_TPCANMsg())
    __swig_destroy__ = _pcan_module.delete_TPCANMsg

# Register TPCANMsg in _pcan_module:
_pcan_module.TPCANMsg_swigregister(TPCANMsg)

class TPCANRdMsg(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Msg = property(_pcan_module.TPCANRdMsg_Msg_get, _pcan_module.TPCANRdMsg_Msg_set)
    dwTime = property(_pcan_module.TPCANRdMsg_dwTime_get, _pcan_module.TPCANRdMsg_dwTime_set)
    wUsec = property(_pcan_module.TPCANRdMsg_wUsec_get, _pcan_module.TPCANRdMsg_wUsec_set)

    def __init__(self):
        _pcan_module.TPCANRdMsg_swiginit(self, _pcan_module.new_TPCANRdMsg())
    __swig_destroy__ = _pcan_module.delete_TPCANRdMsg

# Register TPCANRdMsg in _pcan_module:
_pcan_module.TPCANRdMsg_swigregister(TPCANRdMsg)

class TPSTATUS(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    wErrorFlag = property(_pcan_module.TPSTATUS_wErrorFlag_get, _pcan_module.TPSTATUS_wErrorFlag_set)
    nLastError = property(_pcan_module.TPSTATUS_nLastError_get, _pcan_module.TPSTATUS_nLastError_set)

    def __init__(self):
        _pcan_module.TPSTATUS_swiginit(self, _pcan_module.new_TPSTATUS())
    __swig_destroy__ = _pcan_module.delete_TPSTATUS

# Register TPSTATUS in _pcan_module:
_pcan_module.TPSTATUS_swigregister(TPSTATUS)

class TPDIAG(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    wType = property(_pcan_module.TPDIAG_wType_get, _pcan_module.TPDIAG_wType_set)
    dwBase = property(_pcan_module.TPDIAG_dwBase_get, _pcan_module.TPDIAG_dwBase_set)
    wIrqLevel = property(_pcan_module.TPDIAG_wIrqLevel_get, _pcan_module.TPDIAG_wIrqLevel_set)
    dwReadCounter = property(_pcan_module.TPDIAG_dwReadCounter_get, _pcan_module.TPDIAG_dwReadCounter_set)
    dwWriteCounter = property(_pcan_module.TPDIAG_dwWriteCounter_get, _pcan_module.TPDIAG_dwWriteCounter_set)
    dwIRQcounter = property(_pcan_module.TPDIAG_dwIRQcounter_get, _pcan_module.TPDIAG_dwIRQcounter_set)
    dwErrorCounter = property(_pcan_module.TPDIAG_dwErrorCounter_get, _pcan_module.TPDIAG_dwErrorCounter_set)
    wErrorFlag = property(_pcan_module.TPDIAG_wErrorFlag_get, _pcan_module.TPDIAG_wErrorFlag_set)
    nLastError = property(_pcan_module.TPDIAG_nLastError_get, _pcan_module.TPDIAG_nLastError_set)
    nOpenPaths = property(_pcan_module.TPDIAG_nOpenPaths_get, _pcan_module.TPDIAG_nOpenPaths_set)
    szVersionString = property(_pcan_module.TPDIAG_szVersionString_get, _pcan_module.TPDIAG_szVersionString_set)

    def __init__(self):
        _pcan_module.TPDIAG_swiginit(self, _pcan_module.new_TPDIAG())
    __swig_destroy__ = _pcan_module.delete_TPDIAG

# Register TPDIAG in _pcan_module:
_pcan_module.TPDIAG_swigregister(TPDIAG)

class TPBTR0BTR1(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    dwBitRate = property(_pcan_module.TPBTR0BTR1_dwBitRate_get, _pcan_module.TPBTR0BTR1_dwBitRate_set)
    wBTR0BTR1 = property(_pcan_module.TPBTR0BTR1_wBTR0BTR1_get, _pcan_module.TPBTR0BTR1_wBTR0BTR1_set)

    def __init__(self):
        _pcan_module.TPBTR0BTR1_swiginit(self, _pcan_module.new_TPBTR0BTR1())
    __swig_destroy__ = _pcan_module.delete_TPBTR0BTR1

# Register TPBTR0BTR1 in _pcan_module:
_pcan_module.TPBTR0BTR1_swigregister(TPBTR0BTR1)

class TPEXTENDEDSTATUS(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    wErrorFlag = property(_pcan_module.TPEXTENDEDSTATUS_wErrorFlag_get, _pcan_module.TPEXTENDEDSTATUS_wErrorFlag_set)
    nLastError = property(_pcan_module.TPEXTENDEDSTATUS_nLastError_get, _pcan_module.TPEXTENDEDSTATUS_nLastError_set)
    nPendingReads = property(_pcan_module.TPEXTENDEDSTATUS_nPendingReads_get, _pcan_module.TPEXTENDEDSTATUS_nPendingReads_set)
    nPendingWrites = property(_pcan_module.TPEXTENDEDSTATUS_nPendingWrites_get, _pcan_module.TPEXTENDEDSTATUS_nPendingWrites_set)

    def __init__(self):
        _pcan_module.TPEXTENDEDSTATUS_swiginit(self, _pcan_module.new_TPEXTENDEDSTATUS())
    __swig_destroy__ = _pcan_module.delete_TPEXTENDEDSTATUS

# Register TPEXTENDEDSTATUS in _pcan_module:
_pcan_module.TPEXTENDEDSTATUS_swigregister(TPEXTENDEDSTATUS)

class TPMSGFILTER(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    FromID = property(_pcan_module.TPMSGFILTER_FromID_get, _pcan_module.TPMSGFILTER_FromID_set)
    ToID = property(_pcan_module.TPMSGFILTER_ToID_get, _pcan_module.TPMSGFILTER_ToID_set)
    MSGTYPE = property(_pcan_module.TPMSGFILTER_MSGTYPE_get, _pcan_module.TPMSGFILTER_MSGTYPE_set)

    def __init__(self):
        _pcan_module.TPMSGFILTER_swiginit(self, _pcan_module.new_TPMSGFILTER())
    __swig_destroy__ = _pcan_module.delete_TPMSGFILTER

# Register TPMSGFILTER in _pcan_module:
_pcan_module.TPMSGFILTER_swigregister(TPMSGFILTER)

SF_GET_SERIALNUMBER = _pcan_module.SF_GET_SERIALNUMBER
SF_GET_HCDEVICENO = _pcan_module.SF_GET_HCDEVICENO
SF_SET_HCDEVICENO = _pcan_module.SF_SET_HCDEVICENO
class TPEXTRAPARAMS(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    nSubFunction = property(_pcan_module.TPEXTRAPARAMS_nSubFunction_get, _pcan_module.TPEXTRAPARAMS_nSubFunction_set)
    func = property(_pcan_module.TPEXTRAPARAMS_func_get)

    def __init__(self):
        _pcan_module.TPEXTRAPARAMS_swiginit(self, _pcan_module.new_TPEXTRAPARAMS())
    __swig_destroy__ = _pcan_module.delete_TPEXTRAPARAMS

# Register TPEXTRAPARAMS in _pcan_module:
_pcan_module.TPEXTRAPARAMS_swigregister(TPEXTRAPARAMS)

class pcan_extra_params_func(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    dwSerialNumber = property(_pcan_module.pcan_extra_params_func_dwSerialNumber_get, _pcan_module.pcan_extra_params_func_dwSerialNumber_set)
    ucHCDeviceNo = property(_pcan_module.pcan_extra_params_func_ucHCDeviceNo_get, _pcan_module.pcan_extra_params_func_ucHCDeviceNo_set)

    def __init__(self):
        _pcan_module.pcan_extra_params_func_swiginit(self, _pcan_module.new_pcan_extra_params_func())
    __swig_destroy__ = _pcan_module.delete_pcan_extra_params_func

# Register pcan_extra_params_func in _pcan_module:
_pcan_module.pcan_extra_params_func_swigregister(pcan_extra_params_func)

PCAN_MAGIC_NUMBER = _pcan_module.PCAN_MAGIC_NUMBER
MYSEQ_START = _pcan_module.MYSEQ_START

def open_can(dev):
    return _pcan_module.open_can(dev)

def close_can():
    return _pcan_module.close_can()

def get_version_info():
    return _pcan_module.get_version_info()

def configure_can():
    return _pcan_module.configure_can()

def read_can_msg():
    return _pcan_module.read_can_msg()

def send_can_msg(num_elements):
    return _pcan_module.send_can_msg(num_elements)

cvar = _pcan_module.cvar

