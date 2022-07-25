import cv2
from ignoring_zone_process_technique.process_zones import process_rect_list_with_ignore_zone_list


def draw_rects(blank_image, ignoring_zones_list, result, sample_rect):
    blank_image = cv2.rectangle(blank_image,(sample_rect[0], sample_rect[1]),(sample_rect[2], sample_rect[3]),(0,0,255),2)
    for zone in ignoring_zones_list:
        blank_image =  cv2.rectangle(blank_image,(zone[0], zone[1]),(zone[2], zone[3]),(0,255,0),2)
    for rect in result:
        blank_image = cv2.rectangle(blank_image,(rect[0], rect[1]),(rect[2], rect[3]),(255,0,0),2)
    return  blank_image


def test_process_zone(sample_rect, blank_image):
    ignoring_zones_list = [
        [0, 500, 600, 900],
        # [400,400,900,900]
    ]
    result = process_rect_list_with_ignore_zone_list([sample_rect], ignoring_zones_list)
    blank_image = draw_rects(blank_image, ignoring_zones_list, result, sample_rect)
    cv2.imwrite("tests/result.jpg",blank_image)


def test_process_zone_top_left(sample_rect, blank_image):
    ignoring_zones_list = [
        [0, 0, 600, 600],
    ]
    result = process_rect_list_with_ignore_zone_list([sample_rect], ignoring_zones_list)
    blank_image = draw_rects(blank_image, ignoring_zones_list, result, sample_rect)
    cv2.imwrite("tests/result_top_left.jpg",blank_image)


def test_process_zone_top_right(sample_rect, blank_image):
    ignoring_zones_list = [
        [600,0 , 900, 600],
    ]
    result = process_rect_list_with_ignore_zone_list([sample_rect], ignoring_zones_list)
    blank_image = draw_rects(blank_image, ignoring_zones_list, result, sample_rect)
    cv2.imwrite("tests/result_top_right.jpg",blank_image)


def test_two_corner_rect_top(sample_rect_vertical, blank_image):
    ignoring_zones_list = [
        [0,100 , 600, 300],
    ]
    result = process_rect_list_with_ignore_zone_list([sample_rect_vertical], ignoring_zones_list)
    blank_image = draw_rects(blank_image, ignoring_zones_list, result, sample_rect_vertical)
    cv2.imwrite("tests/result_two_corners_rect_top.jpg",blank_image)


def test_two_corner_rect_bottom(sample_rect_vertical, blank_image):
    ignoring_zones_list = [
        [0,700 , 600, 1000],
    ]
    result = process_rect_list_with_ignore_zone_list([sample_rect_vertical], ignoring_zones_list)
    blank_image = draw_rects(blank_image, ignoring_zones_list, result, sample_rect_vertical)
    cv2.imwrite("tests/result_two_corners_rect_bottom.jpg",blank_image)


def test_two_corner_rect_left(sample_rect_horizontal, blank_image):
    ignoring_zones_list = [
        [0,100, 300, 900 ]
    ]
    result = process_rect_list_with_ignore_zone_list([sample_rect_horizontal], ignoring_zones_list)
    blank_image = draw_rects(blank_image, ignoring_zones_list, result, sample_rect_horizontal)
    cv2.imwrite("test/result_two_corners_rect_left.jpg",blank_image)


def test_two_corner_rect_right(sample_rect_horizontal, blank_image):
    ignoring_zones_list = [
        [600,100, 900, 900 ]
    ]
    result = process_rect_list_with_ignore_zone_list([sample_rect_horizontal], ignoring_zones_list)
    blank_image = draw_rects(blank_image, ignoring_zones_list, result, sample_rect_horizontal)
    cv2.imwrite("test/result_two_corners_rect_right.jpg",blank_image)


def test_process_zone_bottom_right(sample_rect, blank_image):
    ignoring_zones_list = [
        [600,600, 900,900]
    ]
    result = process_rect_list_with_ignore_zone_list([sample_rect], ignoring_zones_list)
    blank_image = draw_rects(blank_image, ignoring_zones_list, result, sample_rect)
    cv2.imwrite("test/result_bottom_right.jpg",blank_image)

def test_process_zone_cross(sample_rect_vertical, blank_image):
    ignoring_zones_list = [
      [100,500, 900, 600],
        [400,300, 500,800]
    ]
    result = process_rect_list_with_ignore_zone_list([sample_rect_vertical], ignoring_zones_list)
    blank_image = draw_rects(blank_image, ignoring_zones_list, result, sample_rect_vertical)
    cv2.imwrite("tests/result_zone_cross.jpg",blank_image)

def test_process_ignoring_zone_in_rect(sample_rect,blank_image):
    ignoring_zones_list = [
        [450, 450, 550, 550]
    ]
    result = process_rect_list_with_ignore_zone_list([sample_rect], ignoring_zones_list)
    blank_image = draw_rects(blank_image, ignoring_zones_list, result, sample_rect)
    cv2.imwrite("tests/result_zone_in_rect.jpg", blank_image)


def test_process_2_corner_ignoring_zone_left_in_rect(sample_rect, blank_image):
    ignoring_zones_list = [
        [200,600, 500,700]
    ]
    result = process_rect_list_with_ignore_zone_list([sample_rect], ignoring_zones_list)
    blank_image = draw_rects(blank_image, ignoring_zones_list, result, sample_rect)
    cv2.imwrite("tests/result_2_zone_in_rect_left.jpg", blank_image)


def test_process_2_corner_ignoring_zone_right_in_rect(sample_rect, blank_image):
    ignoring_zones_list = [
        [600,600, 900,700]
    ]
    result = process_rect_list_with_ignore_zone_list([sample_rect], ignoring_zones_list)
    blank_image = draw_rects(blank_image, ignoring_zones_list, result, sample_rect)
    cv2.imwrite("tests/result_2_zone_in_rect_right.jpg", blank_image)


def test_process_2_corner_ignoring_zone_bottom_in_rect(sample_rect, blank_image):
    ignoring_zones_list = [
        [600,600, 700,900]
    ]
    result = process_rect_list_with_ignore_zone_list([sample_rect], ignoring_zones_list)
    blank_image = draw_rects(blank_image, ignoring_zones_list, result, sample_rect)
    cv2.imwrite("tests/result_2_zone_in_rect_bottom.jpg", blank_image)


