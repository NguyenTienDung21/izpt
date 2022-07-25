# define cases constant
import ignoring_zone_process_technique.rect_utils as rect_utils
from enum import Enum
class Cases(Enum):
    CASE_ONE_CORNER_IN_IGNORING_ZONE = 0
    CASE_TWO_CORNERS_IN_IGNORING_ZONE = 1
    CASE_FOUR_CORNERS_IN_IGNORING_ZONE = 2
    CASE_TWO_IGNORE_CORNERS_IN_RECT = 3
    CASE_FOUR_IGNORE_CORNERS_IN_RECT = 4
    CASE_CROSS_ZONES =5


def check_case(rect_corners, ignore_zone_corners):
    point_in_ignore = rect_utils.get_point_rect_in_another(rect_corners, ignore_zone_corners)
    point_in_rect = rect_utils.get_point_rect_in_another(ignore_zone_corners, rect_corners)
    if len(point_in_ignore) == 1:
        return Cases.CASE_ONE_CORNER_IN_IGNORING_ZONE
    elif len(point_in_ignore) == 2:
        return Cases.CASE_TWO_CORNERS_IN_IGNORING_ZONE
    elif len(point_in_ignore) == 4:
        return Cases.CASE_FOUR_CORNERS_IN_IGNORING_ZONE
    elif len(point_in_rect) == 2:
        return Cases.CASE_TWO_IGNORE_CORNERS_IN_RECT
    elif len(point_in_rect) == 4:
        return Cases.CASE_FOUR_IGNORE_CORNERS_IN_RECT
    elif len(point_in_rect) == 0 and len(point_in_ignore) == 0:
        return Cases.CASE_CROSS_ZONES