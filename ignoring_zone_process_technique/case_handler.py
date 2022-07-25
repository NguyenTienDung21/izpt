# only handle 1 rect and 1 ignnoring zone at 1 handler
import ignoring_zone_process_technique.rect_utils as rect_utils
from ignoring_zone_process_technique.points import Points
from ignoring_zone_process_technique.constant import TOP, LEFT, RIGHT, BOTTOM


def __one_corner_top_left_handler(rect_corners, intersect_rect):
    first_rectangle_corners = {
        "top_left": intersect_rect["top_right"],
        "top_right": rect_corners["top_right"],
        "bottom_right": Points(rect_corners["top_right"].x, intersect_rect["bottom_right"].y),
        "bottom_left": intersect_rect["bottom_right"]
    }
    second_rectangle_corners = {
        "top_left": intersect_rect["bottom_left"],
        "top_right": first_rectangle_corners["top_right"],
        "bottom_right": rect_corners["bottom_right"],
        "bottom_left": rect_corners["bottom_left"]
    }
    return [first_rectangle_corners, second_rectangle_corners]


def __one_corner_top_right_handler(rect_corners, intersect_rect):
    first_rectangle_corners = {
        "top_left": rect_corners["top_left"],
        "top_right": intersect_rect["top_left"],
        "bottom_right": intersect_rect["bottom_left"],
        "bottom_left" : Points(rect_corners["top_left"].x, intersect_rect["bottom_left"].y)
    }
    second_rectangle_corners = {
        "top_left": first_rectangle_corners["bottom_left"],
        "top_right": intersect_rect["bottom_right"],
        "bottom_right": rect_corners["bottom_right"],
        "bottom_left": rect_corners["bottom_left"]
    }
    return [first_rectangle_corners, second_rectangle_corners]


def __one_corner_bottom_right_handler(rect_corners, intersect_rect):
    first_rectangle_corners = {
        "top_left": rect_corners["top_left"],
        "top_right": rect_corners["top_right"],
        "bottom_right": intersect_rect["top_right"],
        "bottom_left": Points(rect_corners["top_left"].x, intersect_rect["top_left"].y)
    }
    second_rectangle_corners = {
        "top_left": first_rectangle_corners["bottom_left"],
        "top_right": intersect_rect["top_left"],
        "bottom_right": intersect_rect["bottom_left"],
        "bottom_left": rect_corners["bottom_left"]
    }
    return [first_rectangle_corners, second_rectangle_corners]


def __one_corner_bottom_left_handler(rect_corners, intersect_rect):
    first_rectangle_corners = {
        "top_left": rect_corners["top_left"],
        "top_right": rect_corners["top_right"],
        "bottom_right": Points(rect_corners["top_right"].x, intersect_rect["top_right"].y),
        "bottom_left": intersect_rect["top_left"]
    }
    second_rectangle_corners = {
        "top_left": intersect_rect["top_right"],
        "top_right": first_rectangle_corners["bottom_right"],
        "bottom_right": rect_corners["bottom_right"],
        "bottom_left": intersect_rect["bottom_right"]
    }
    return [first_rectangle_corners, second_rectangle_corners]


def one_corner_in_ignoring_zone_handler(rect_corners, ignoring_zone_corners):
    corner_type = rect_utils.get_point_rect_in_another(rect_corners, ignoring_zone_corners)[0]
    intersect_rect = rect_utils.get_intersect_rect(rect_corners, ignoring_zone_corners)
    """
        the top left corner in the ignoring zone
    """
    if corner_type == "top_left":
        return __one_corner_top_left_handler(rect_corners, intersect_rect)
    elif corner_type == "bottom_right":
        return __one_corner_bottom_right_handler(rect_corners, intersect_rect)
    elif corner_type == "bottom_left":
        return __one_corner_bottom_left_handler(rect_corners, intersect_rect)
    elif corner_type == "top_right":
        return __one_corner_top_right_handler(rect_corners, intersect_rect)


def __two_corner_top_handler(rect_corners, intersect_rect):
    remain_rectangle = {
        "top_left": intersect_rect["bottom_left"],
        "top_right": intersect_rect["bottom_right"],
        "bottom_right": rect_corners["bottom_right"],
        "bottom_left": rect_corners["bottom_left"]
    }
    return [remain_rectangle]


def __two_corner_bottom_handler(rect_corners, intersect_rect):
    remain_rectangle = {
        "top_left": rect_corners["top_left"],
        "top_right": rect_corners["top_right"],
        "bottom_right": intersect_rect["top_right"],
        "bottom_left": intersect_rect["top_left"]
    }
    return [remain_rectangle]


def __two_corner_left_handler(rect_corners, intersect_rect):
    remain_rectangle = {
        "top_left": intersect_rect["top_right"],
        "top_right": rect_corners["top_right"],
        "bottom_right": rect_corners["bottom_right"],
        "bottom_left": intersect_rect["bottom_right"]
    }
    return [remain_rectangle]


def __two_corner_right_handler(rect_corners, intersect_rect):
    remain_rectangle = {
        "top_left": rect_corners["top_left"],
        "top_right": intersect_rect["top_left"],
        "bottom_right": intersect_rect["bottom_left"],
        "bottom_left": rect_corners["bottom_left"]
    }
    return [remain_rectangle]


def two_corner_in_ignoring_zone_handler(rect_corners, ignoring_zone_corners):
    corners_in_ignoring_zones = rect_utils.get_point_rect_in_another(rect_corners, ignoring_zone_corners)
    corner_type_0 = corners_in_ignoring_zones[0]
    corner_type_1 = corners_in_ignoring_zones[1]
    intersect_rect = rect_utils.get_intersect_rect(rect_corners, ignoring_zone_corners)
    if corner_type_0 in TOP and corner_type_1 in TOP:
        return __two_corner_top_handler(rect_corners, intersect_rect)
    elif corner_type_0 in LEFT and corner_type_1 in LEFT:
        return __two_corner_left_handler(rect_corners, intersect_rect)
    elif corner_type_0 in RIGHT and corner_type_1 in RIGHT:
        return __two_corner_right_handler(rect_corners, intersect_rect)
    elif corner_type_0 in BOTTOM and corner_type_1 in BOTTOM:
        return __two_corner_bottom_handler(rect_corners, intersect_rect)


def __two_corner_top_in_rect_handler(rect_corners, intersect_rect):
    first_rectangle = {
        "top_left": rect_corners["top_left"],
        "top_right": Points(intersect_rect["top_left"].x, rect_corners["top_left"].y),
        "bottom_right": intersect_rect["bottom_left"],
        "bottom_left": rect_corners["bottom_left"]
    }
    second_rectangle = {
        "top_left": Points(intersect_rect["top_right"].x, rect_corners["top_left"].y),
        "top_right": rect_corners["top_right"],
        "bottom_right": rect_corners["bottom_right"],
        "bottom_left": intersect_rect["bottom_right"]
    }
    third_rectangle = {
        "top_left": first_rectangle["top_right"],
        "top_right": second_rectangle["top_left"],
        "bottom_right": intersect_rect["top_right"],
        "bottom_left": intersect_rect["top_left"]
    }
    return [first_rectangle, second_rectangle, third_rectangle]


def __two_corner_bottom_in_rect_handler(rect_corners, intersect_rect):
    first_rectangle = {
        "top_left": rect_corners["top_left"],
        "top_right": intersect_rect["top_left"],
        "bottom_right": Points(intersect_rect["top_left"].x, rect_corners["bottom_left"].y),
        "bottom_left": rect_corners["bottom_left"]
    }
    second_rectangle = {
        "top_left": intersect_rect["top_right"],
        "top_right": rect_corners["top_right"],
        "bottom_right": rect_corners["bottom_right"],
        "bottom_left": Points(intersect_rect["top_right"].x, rect_corners["bottom_right"].y)
    }
    third_rectangle = {
        "top_left": intersect_rect["bottom_left"],
        "top_right": intersect_rect["bottom_right"],
        "bottom_right": second_rectangle["bottom_left"],
        "bottom_left": first_rectangle["bottom_right"]
    }
    return [first_rectangle, second_rectangle, third_rectangle]


def __two_corner_right_in_rect_handler(rect_corners, intersect_rect):
    first_rectangle = {
        "top_left": rect_corners["top_left"],
        "top_right": rect_corners["top_right"],
        "bottom_right": Points(rect_corners["top_right"].x, intersect_rect["top_right"].y),
        "bottom_left": intersect_rect["top_left"]
    }
    second_rectangle = {
        "top_left": intersect_rect["bottom_left"],
        "top_right": Points(rect_corners["top_right"].x, intersect_rect["bottom_right"].y),
        "bottom_right": rect_corners["bottom_right"],
        "bottom_left": rect_corners["bottom_left"]
    }
    third_rectangle = {
        "top_left": intersect_rect["top_right"],
        "top_right": first_rectangle["bottom_right"],
        "bottom_right": second_rectangle["top_right"],
        "bottom_left": intersect_rect["bottom_right"]
    }
    return [first_rectangle, second_rectangle, third_rectangle]


def __two_corner_left_in_rect_handler(rect_corners, intersect_rect):
    first_rectangle = {
        "top_left": rect_corners["top_left"],
        "top_right": rect_corners["top_right"],
        "bottom_right": intersect_rect["top_right"],
        "bottom_left": Points(rect_corners["top_left"].x, intersect_rect["top_left"].y)
    }
    second_rectangle = {
        "top_left":Points(rect_corners["top_left"].x,intersect_rect["bottom_left"].y),
        "top_right":intersect_rect["bottom_right"],
        "bottom_right": rect_corners["bottom_right"],
        "bottom_left": rect_corners["bottom_left"]
    }
    third_rectangle = {
        "top_left": first_rectangle["bottom_left"],
        "top_right": intersect_rect["top_left"],
        "bottom_right": intersect_rect["bottom_left"],
        "bottom_left": second_rectangle["top_left"]
    }
    return [first_rectangle,second_rectangle,third_rectangle]


def two_ignoring_zone_corner_in_rect_handler(rect_corners, ignoring_zone_corners):
    corners_in_rect = rect_utils.get_point_rect_in_another(ignoring_zone_corners, rect_corners)
    corner_type_0 = corners_in_rect[0]
    corner_type_1 = corners_in_rect[1]
    intersect_rect = rect_utils.get_intersect_rect(rect_corners, ignoring_zone_corners)
    if corner_type_0 in TOP and corner_type_1 in TOP:
        return __two_corner_top_in_rect_handler(rect_corners, intersect_rect)
    elif corner_type_0 in LEFT and corner_type_1 in LEFT:
        return __two_corner_left_in_rect_handler(rect_corners, intersect_rect)
    elif corner_type_0 in RIGHT and corner_type_1 in RIGHT:
        return __two_corner_right_in_rect_handler(rect_corners, intersect_rect)
    elif corner_type_0 in BOTTOM and corner_type_1 in BOTTOM:
        return __two_corner_bottom_in_rect_handler(rect_corners, intersect_rect)


def ignoring_zone_in_rect_handler(rect_corners, ignoring_zone_corners):
    first_rectangle = {
        "top_left": rect_corners["top_left"],
        "top_right": rect_corners["top_right"],
        "bottom_right": Points(rect_corners["top_right"].x, ignoring_zone_corners["top_right"].y),
        "bottom_left": Points(rect_corners["top_left"].x, ignoring_zone_corners["top_left"].y)
    }
    second_rectangle = {
        "top_left": Points(rect_corners["bottom_left"].x, ignoring_zone_corners["bottom_right"].y),
        "top_right": Points(rect_corners["bottom_right"].x, ignoring_zone_corners["bottom_right"].y),
        "bottom_right": rect_corners["bottom_right"],
        "bottom_left": rect_corners["bottom_left"]
    }
    third_rectangle = {
        "top_left": first_rectangle["bottom_left"],
        "top_right": ignoring_zone_corners["top_left"],
        "bottom_right": ignoring_zone_corners["bottom_left"],
        "bottom_left": second_rectangle["top_left"]
    }
    fourth_rectangle = {
        "top_left": ignoring_zone_corners["top_right"],
        "top_right": first_rectangle["bottom_right"],
        "bottom_right": second_rectangle["top_right"],
        "bottom_left": ignoring_zone_corners["bottom_right"]
    }
    return [first_rectangle, second_rectangle,third_rectangle, fourth_rectangle]


def check_rect_cross_vertical(rect_corners, ignoring_zone_corners):
    width_rect = rect_corners["top_right"].x - rect_corners["top_left"].x
    width_ignore = ignoring_zone_corners["top_right"].x - ignoring_zone_corners["top_left"].x
    if width_rect < width_ignore :
        return True
    return False


def crossing_zone_rect_vertical_handler(rect_corners, intersect_rect):
    first_rectangle = {
        "top_left": rect_corners["top_left"],
        "top_right": rect_corners["top_right"],
        "bottom_right": intersect_rect["top_right"],
        "bottom_left": intersect_rect["top_left"]
    }
    second_rectangle = {
        "top_left": intersect_rect["bottom_left"],
        "top_right": intersect_rect["bottom_right"],
        "bottom_right": rect_corners["bottom_right"],
        "bottom_left": rect_corners["bottom_left"]
    }
    return [first_rectangle, second_rectangle]


def crossing_zone_rect_horizontal_handler(rect_corners, instersect_rect):
    first_rectangle = {
        "top_left": rect_corners["top_left"],
        "top_right": instersect_rect["top_left"],
        "bottom_right": instersect_rect["bottom_left"],
        "bottom_left": rect_corners["bottom_left"]
    }
    second_rectangle = {
        "top_left": instersect_rect["top_right"],
        "top_right": rect_corners["top_right"],
        "bottom_right": rect_corners["bottom_right"],
        "bottom_left": instersect_rect["bottom_right"]
    }
    return [first_rectangle, second_rectangle]


def crossing_zone_handler(rect_corners, ignoring_zone_corners):
    intersect_rect = rect_utils.get_intersect_rect(rect_corners, ignoring_zone_corners)
    if check_rect_cross_vertical(rect_corners,ignoring_zone_corners):
        return crossing_zone_rect_vertical_handler(rect_corners, intersect_rect)
    return crossing_zone_rect_horizontal_handler(rect_corners, intersect_rect)

