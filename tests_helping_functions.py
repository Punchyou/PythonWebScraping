from HN_Data import HNData

def initialize_hn_valid_object():
    """Initialize the data object with valid data."""
    hn_data_obj = HNData("Sherlock", "Doyle", "https://news.ycombinator.com/", 34, 20, 3)
    return hn_data_obj

def initialize_hn_obj_invalid_title_empty():
    """ Initialize an object with invalid title, an empty string."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.title = ""
    return hn_data_obj

def initialize_hn_obj_invalid_title_number():
    """ Initialiaze an object with invalid title, a number."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.title = 7
    return hn_data_obj

def initialize_hn_obj_invalid_title_too_long():
    """Initialiaze an object with invalid title, with too many characters."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.title = "I had seen little of Holmes lately. My marriage had drifted us away from each other. My own complete happiness, and the home-centred interests which rise up around the man who first finds himself master of his own establishment, were sufficient to absorb all my attention, while Holmes..."
    return hn_data_obj

def initialize_hn_obj_invalid_author_name_empty():
    """ Initialize an object with invalid author's name, an empty string."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.author = ""
    return hn_data_obj

def initialize_hn_obj_invalid_author_name_number():
    """ Initialize an object with invalid author's name, a number."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.author = 7
    return hn_data_obj

def initialize_hn_obj_invalid_author_name_too_long():
    """ Initialize an object with invalid author's name, too many charasters."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.author = "I had seen little of Holmes lately. My marriage had drifted us away from each other. My own complete happiness, and the home-centred interests which rise up around the man who first finds himself master of his own establishment, were sufficient to absorb all my attention, while Holmes..."
    return hn_data_obj

def initialize_hn_obj_invalid_points_character():
    """ Initialize an object with points as characters."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.points = "5"
    return hn_data_obj

def initialize_hn_obj_invalid_points_negative_number():
    """ Initialize an object with invalid points, as negative numbers."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.points = -20
    return hn_data_obj

def initialize_hn_obj_invalid_points_not_integer():
    """ Initialize an object with invalid points, as decimal."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.points = 2.5
    return hn_data_obj

def initialize_hn_obj_invalid_comments_character():
    """ Initialize an object with number of comments, as characters."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.comments = "5"
    return hn_data_obj

def initialize_hn_obj_invalid_comments_negative_number():
    """ Initialize an object with invalid number of comments, as a negative numbers."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.comments = -20
    return hn_data_obj

def initialize_hn_obj_invalid_comments_not_integer():
    """ Initialize an object with invalid points, as a decimal."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.comments = 2.5
    return hn_data_obj

def initialize_hn_obj_invalid_rank_character():
    """ Initialize an object with rank as characters."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.rank = "5"
    return hn_data_obj

def initialize_hn_obj_invalid_rank_negative_number():
    """ Initialize an object with invalid rank, as a negative numbers."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.rank = -20
    return hn_data_obj

def initialize_hn_obj_invalid_rank_not_integer():
    """ Initialize an object with invalid rank, as a decimal."""
    hn_data_obj = initialize_hn_valid_object()
    hn_data_obj.rank = 2.5
    return hn_data_obj