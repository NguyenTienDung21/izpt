import cv2
from ignoring_zone_process_technique.process_zones import process_rect_list_with_ignore_zone_list




def test_process_zone(sample_rect, blank_image):
    ignoring_zones_list = [
        [0, 500, 600, 900],
        # [400,400,900,900]
    ]
    result = process_rect_list_with_ignore_zone_list([sample_rect], ignoring_zones_list)
    for zone in ignoring_zones_list:
        blank_image =  cv2.rectangle(blank_image,(zone[0], zone[1]),(zone[2], zone[3]),(0,255,0),2)
    for rect in result:
        blank_image = cv2.rectangle(blank_image,(rect[0], rect[1]),(rect[2], rect[3]),(255,0,0),2)
    cv2.imwrite("result.jpg",blank_image)

def test_process_zone_cross(sample_rect_vertical, blank_image):
    ignoring_zones_list = [
      [100,500, 900, 600],
        [400,300, 500,800]
    ]
    result = process_rect_list_with_ignore_zone_list([sample_rect_vertical], ignoring_zones_list)
    for zone in ignoring_zones_list:
        blank_image =  cv2.rectangle(blank_image,(zone[0], zone[1]),(zone[2], zone[3]),(0,255,0),2)
    for rect in result:
        blank_image = cv2.rectangle(blank_image,(rect[0], rect[1]),(rect[2], rect[3]),(255,0,0),2)
    cv2.imwrite("result_zone_cross.jpg",blank_image)