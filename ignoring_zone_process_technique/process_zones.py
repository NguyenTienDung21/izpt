from ignoring_zone_process_technique.cases import Cases, check_case
import ignoring_zone_process_technique.case_handler as  case_handler
import ignoring_zone_process_technique.rect_utils as rect_utils


def process_zones(rect, ignoring_zone):
    corners_rect = rect_utils.extract_corners(rect)
    corners_ignoring_zone = rect_utils.extract_corners(ignoring_zone)
    case = check_case(corners_rect,corners_ignoring_zone)
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


def process_rect_list_with_ignoring_zone(rect_list, ignoring_zone):
    new_rects = []
    for rect in rect_list:
        result =[rect_utils.convert_to_old_format_rect(item) for item in process_zones(rect, ignoring_zone)]

        if result is not None and len(result) > 0 :
            new_rects += result
    return new_rects

def process_rect_list_with_ignore_zone_list(rect_list, ignoring_zone_list):
    new_rect_list = rect_list
    for zone in ignoring_zone_list:
        new_rect_list =  process_rect_list_with_ignoring_zone(new_rect_list, zone)

    return new_rect_list
