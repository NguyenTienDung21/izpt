from cases import Cases
import case_handler
import rect_utils


def process_zones(rect, ignoring_zone, case):
    corners_rect = rect_utils.extract_corners(rect)
    corners_ignoring_zone = rect_utils.extract_corners(ignoring_zone)
    if case == Cases.CASE_ONE_CORNER_IN_IGNORING_ZONE:
        return case_handler.one_corner_in_ignoring_zone_handler(corners_rect, corners_ignoring_zone)
    elif case == Cases.CASE_TWO_CORNERS_IN_IGNORING_ZONE:
        return case_handler.two_corner_in_ignoring_zone_handler(corners_rect, corners_ignoring_zone)
    elif case == Cases.CASE_FOUR_CORNERS_IN_IGNORING_ZONE:
        return ()
    elif case == Cases.CASE_TWO_IGNORE_CORNERS_IN_RECT:
        return case_handler.two_ignoring_zone_corner_in_rect_handler(corners_rect, corners_ignoring_zone)
    elif case == Cases.CASE_FOUR_IGNORE_CORNERS_IN_RECT:
        return case_handler.ignoring_zone_in_rect_handler(corners_rect, corners_ignoring_zone)
    elif case == Cases.CASE_CROSS_ZONES:
        return case_handler.crossing_zone_handler(corners_rect, corners_ignoring_zone)