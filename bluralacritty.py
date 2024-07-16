from pywinauto import Application
from ctypes import c_int, Structure, POINTER, windll, byref, sizeof, cast, pointer
import sys


def is_win11():
    return sys.getwindowsversion().build > 20000


class ACCENT_POLICY(Structure):
    _fields_ = [
        ("AccentState", c_int),
        ("AccentFlags", c_int),
        ("GradientColor", c_int), 
        ("AnimationId", c_int)
    ]


class WINDOWCOMPOSITIONATTRIBDATA(Structure):
    _fields_ = [
        ("Attribute", c_int),
        ("Data", POINTER(ACCENT_POLICY)),
        ("SizeOfData", c_int)
    ]


def set_window_blur(hwnd):
    accent = ACCENT_POLICY()
    accent.AccentState = 3  # ACCENT_ENABLE_BLURBEHIND = 3

    if is_win11():
        accent.AccentFlags = 0x20 | 0x40  # COMBINE WITH ACCENT_ENABLE_BLURBEHIND & ACCENT_ENABLE_ACRYLICBLURBEHIND

    accent_data = WINDOWCOMPOSITIONATTRIBDATA()
    accent_data.Attribute = 19  # WCA_ACCENT_POLICY
    accent_data.Data = cast(pointer(accent), POINTER(ACCENT_POLICY))
    accent_data.SizeOfData = sizeof(accent)

    set_window_composition_attribute = windll.user32.SetWindowCompositionAttribute
    set_window_composition_attribute(hwnd, byref(accent_data))


def set_rounded_corners(hwnd):
    DWMWA_WINDOW_CORNER_PREFERENCE = 33
    DWMWCP_ROUND = 2

    windll.dwmapi.DwmSetWindowAttribute(
        hwnd,
        DWMWA_WINDOW_CORNER_PREFERENCE,
        byref(c_int(DWMWCP_ROUND)),
        sizeof(c_int)
    )


def apply_effects():
    hwnd = Application().connect(path="alacritty.exe").top_window().handle

    set_window_blur(hwnd)
    set_rounded_corners(hwnd)


if __name__ == "__main__":
    apply_effects()

