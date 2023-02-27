import usb.core as usb

class EatonEcclipseController:
    usbHIDDevice = None


    def __init__(self) -> None:
        
        self.usbHIDDevice = usb.find(idVendor=0x0463, idProduct=0xffff)

        if self.usbHIDDevice is None:

            raise ValueError('Device not found')



    def TurnEcoPlugOn(self) -> None:
        self.sendSET_REPORT([0x19, 0x00], 0x319)
    def TurnEcoPlugOff(self) -> None:
        self.sendSET_REPORT([0x19, 0x01], 0x319)

    def sendSET_REPORT(self,Command: list,Register: int):
        self.usbHIDDevice.ctrl_transfer(0x21, 0x09, wValue=Register, wIndex=0x00, data_or_wLength=Command)
        return self.usbHIDDevice.ctrl_transfer(0xa1, 0x01, wValue=Register, wIndex=0x00, data_or_wLength=Command)
        
        