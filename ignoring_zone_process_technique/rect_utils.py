from ignoring_zone_process_technique.points import Points

def validate_rect_params(rect1, rect2):
    if rect1 is None or len(rect1) == 0 :
        return False
    if rect2 is None or len(rect2) == 0 :
        return False


def extract_corners(rect):
    if rect is None or len(rect) == 0 :
        return {}
    top_left =Points(rect[0], rect[1])
    top_right = Points(rect[2], rect[1])
    bottom_right = Points(rect[2],rect[3])
    bottom_left = Points(rect[0],rect[3])
    return {
        "top_left": top_left,
        "top_right": top_right,
        "bottom_right": bottom_right,
        "bottom_left": bottom_left
    }


def check_intersect_by_corners(corners1, corners2):
    return not (
                corners1["bottom_right"].x <= corners2["top_left"].x or corners1["top_left"].x >= corners2["bottom_right"]
                or corners1["bottom_right"].y >= corners2["top_left"].y or corners1["top_left"].y <= corners2["bottom_right"].y
                )


def get_point_rect_in_another(corners1, corners2):
    point_list = []
    for key, value in corners1.items() :
        if corners2["top_left"].x < value.x < corners2["bottom_right"].x and \
                corners2["top_left"].y < value.y < corners2["bottom_right"].y:
            point_list.append(key)
    return point_list


def get_intersect_rect(corners1, corners2):
    x_top_left = max(corners1["top_left"].x, corners2["top_left"].x)
    y_top_left = max(corners1["top_left"].y, corners2["top_left"].y)
    x_bottom_right = min(corners1["bottom_right"].x, corners2["bottom_right"].x)
    y_bottom_right = min(corners1["bottom_right"].y, corners2["bottom_right"].y)
    return {
        "top_left": Points(x_top_left, y_top_left),
        "top_right": Points(x_bottom_right, y_top_left),
        "bottom_right": Points(x_bottom_right, y_bottom_right),
        "bottom_left": Points(x_top_left, y_bottom_right)
    }


def convert_to_old_format_rect(corners):
    print(corners)
    return [corners["top_left"].x, corners["top_left"].y, corners["bottom_right"].x, corners["bottom_right"].y]
