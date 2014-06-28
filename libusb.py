import ffi


l = ffi.open("libusb-1.0.so.0")

#int libusb_init(libusb_context **context)
libusb_init = l.func("i", "libusb_init", "p")
#const char *libusb_error_name(int errcode);
libusb_error_name = l.func("s", "libusb_error_name", "i")
#libusb_device_handle *libusb_open_device_with_vid_pid (libusb_context *ctx, uint16_t vendor_id, uint16_t product_id)
libusb_open_device_with_vid_pid = l.func("P", "libusb_open_device_with_vid_pid", "PHH")
#void libusb_close (libusb_device_handle *dev_handle)
libusb_close = l.func("v", "libusb_close", "P")
#int libusb_control_transfer(libusb_device_handle *dev_handle, uint8_t bmRequestType, uint8_t bRequest,
# uint16_t wValue, uint16_t wIndex, unsigned char *data, uint16_t wLength, unsigned int timeout)
libusb_control_transfer = l.func("i", "libusb_control_transfer", "PBBHHpHI")
#int libusb_get_string_descriptor_ascii(libusb_device_handle *dev,
#        uint8_t desc_index, unsigned char *data, int length);
libusb_get_string_descriptor_ascii = l.func("i", "libusb_get_string_descriptor_ascii", "PBpi")

#/** In: device-to-host */
LIBUSB_ENDPOINT_IN = 0x80
#/** Out: host-to-device */
LIBUSB_ENDPOINT_OUT = 0x00

# Request type bits of the "bmRequestType" field in control transfers.
LIBUSB_REQUEST_TYPE_STANDARD = (0x00 << 5)
LIBUSB_REQUEST_TYPE_CLASS = (0x01 << 5)
LIBUSB_REQUEST_TYPE_VENDOR = (0x02 << 5)
LIBUSB_REQUEST_TYPE_RESERVED = (0x03 << 5)

# Recipient bits of the "bmRequestType" field in control
# transfers. Values 4 through 31 are reserved. */
LIBUSB_RECIPIENT_DEVICE = 0x00
LIBUSB_RECIPIENT_INTERFACE = 0x01
LIBUSB_RECIPIENT_ENDPOINT = 0x02
LIBUSB_RECIPIENT_OTHER = 0x03

# Standard requests, as defined in table 9-3 of the USB2 specifications */
#/** Request status of the specific recipient */
LIBUSB_REQUEST_GET_STATUS = 0x00
#/** Clear or disable a specific feature */
LIBUSB_REQUEST_CLEAR_FEATURE = 0x01
#/* 0x02 is reserved */
#/** Set or enable a specific feature */
LIBUSB_REQUEST_SET_FEATURE = 0x03
#/* 0x04 is reserved */
#/** Set device address for all future accesses */
LIBUSB_REQUEST_SET_ADDRESS = 0x05
#/** Get the specified descriptor */
LIBUSB_REQUEST_GET_DESCRIPTOR = 0x06
#/** Used to update existing descriptors or add new descriptors */
LIBUSB_REQUEST_SET_DESCRIPTOR = 0x07
#/** Get the current device configuration value */
LIBUSB_REQUEST_GET_CONFIGURATION = 0x08

# * Descriptor types as defined by the USB specification. */
#/** Device descriptor. See libusb_device_descriptor. */
LIBUSB_DT_DEVICE = 0x01
#/** Configuration descriptor. See libusb_config_descriptor. */
LIBUSB_DT_CONFIG = 0x02
#/** String descriptor */
LIBUSB_DT_STRING = 0x03
#/** Interface descriptor. See libusb_interface_descriptor. */
LIBUSB_DT_INTERFACE = 0x04
#/** Endpoint descriptor. See libusb_endpoint_descriptor. */
LIBUSB_DT_ENDPOINT = 0x05
#/** HID descriptor */
LIBUSB_DT_HID = 0x21
