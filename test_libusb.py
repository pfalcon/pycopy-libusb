from libusb import *


print(libusb_init(None))
h = libusb_open_device_with_vid_pid(None, 0x064e, 0xa136)
print(h)

b = bytearray(1024)

s = libusb_control_transfer(h, LIBUSB_ENDPOINT_IN, LIBUSB_REQUEST_GET_DESCRIPTOR, 0x0100, 0, b, len(b), 1000)
print(s)
if s < 0:
    print(libusb_error_name(s))
print(b[:s])

s = libusb_get_string_descriptor_ascii(h, 1, b, len(b))
print(s)
print(b[:s])
