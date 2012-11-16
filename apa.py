def format_apa_style(full_name, year, title, city, state, publisher):
    """Format a single-author book citation APA-style.

    :param full_name: author's name
    :type full_name: :class:`str`
    :param year: year of publication
    :type year: :class:`int`
    :param title: title of the book
    :type title: :class:`str`
    :param city: city of publication
    :type city: :class:`str`
    :param state: state of publication (within USA)
    :type state: :class:`str`
    :param publisher: publication company
    :type publisher: :class:`str`
    :return: the formatted citation
    :rtype: :class:`str`
    """
    split_name = full_name.split()
    first_initial = split_name[0][0]
    last_name = split_name[1]
    return '{0}, {1}. ({2}). {3}. {4}, {5}: {6}.'.format(last_name, first_initial,
                                                         year, title,city,
                                                         state, publisher)
