"""
    Augmenters that do augmentation for one or more certain classes
"""

import numpy as np

def do_assert(condition, message="Assertion failed."):
    """
    Function that behaves equally to an `assert` statement, but raises an
    Exception.
    This is added because `assert` statements are removed in optimized code.
    It replaces `assert` statements throughout the library that should be
    kept even in optimized code.
    Parameters
    ----------
    condition : bool
        If False, an exception is raised.
    message : str, optional
        Error message.
    """
    if not condition:
        raise AssertionError(str(message))

def _crop_prevent_zero_size(height, width, crop_top, crop_right, crop_bottom, crop_left):
    remaining_height = height - (crop_top + crop_bottom)
    remaining_width = width - (crop_left + crop_right)
    if remaining_height < 1:
        regain = abs(remaining_height) + 1
        regain_top = regain // 2
        regain_bottom = regain // 2
        if regain_top + regain_bottom < regain:
            regain_top += 1

        if regain_top > crop_top:
            diff = regain_top - crop_top
            regain_top = crop_top
            regain_bottom += diff
        elif regain_bottom > crop_bottom:
            diff = regain_bottom - crop_bottom
            regain_bottom = crop_bottom
            regain_top += diff

        do_assert(regain_top <= crop_top)
        do_assert(regain_bottom <= crop_bottom)

        crop_top = crop_top - regain_top
        crop_bottom = crop_bottom - regain_bottom

    if remaining_width < 1:
        regain = abs(remaining_width) + 1
        regain_right = regain // 2
        regain_left = regain // 2
        if regain_right + regain_left < regain:
            regain_right += 1

        if regain_right > crop_right:
            diff = regain_right - crop_right
            regain_right = crop_right
            regain_left += diff
        elif regain_left > crop_left:
            diff = regain_left - crop_left
            regain_left = crop_left
            regain_right += diff

        do_assert(regain_right <= crop_right)
        do_assert(regain_left <= crop_left)

        crop_right = crop_right - regain_right
        crop_left = crop_left - regain_left

    return crop_top, crop_right, crop_bottom, crop_left


image =

height_image =
width_image =


# params for crop
height =
width =
crop_top =
crop_right =
crop_bottom =
crop_left =

crop_top, crop_right, crop_bottom, crop_left = \
    _crop_prevent_zero_size(height, width, crop_top, crop_right, crop_bottom, crop_left)

arr_cr = image[crop_top:height_image-crop_bottom, crop_left:width_image-crop_right, :]

# params for pad
pad_top = int(crop_top)
pad_right = int(crop_right)
pad_bottom = int(crop_bottom)
pad_left = int(crop_left)
pad_cval = 255 # intended to be white

pad_cval = np.clip(np.round(pad_cval), 0, 255).astype(np.uint8)

if any([pad_top > 0, pad_right > 0, pad_bottom > 0, pad_left > 0]):
    if arr_cr.ndim == 2:
        pad_vals = ((pad_top, pad_bottom), (pad_left, pad_right))
    else:
        pad_vals = ((pad_top, pad_bottom), (pad_left, pad_right), (0, 0))

    arr_cr_pa = np.pad(arr_cr, pad_vals, mode="constant", constant_values=0)
else:
    arr_cr_pa = arr_cr

arr_cr_pa = np.pad(arr_cr, pad_vals, mode="constant", constant_values=pad_cval)