def unique_name(mentors):
    all_list = []
    for m in mentors:
        all_list.extend(m)
    all_names_list = []
    for mentor in all_list:
        name = ''.join(mentor.split()[0])
        all_names_list.append(name)
    unique_names = set(all_names_list)

    all_names_sorted = sorted(unique_names)
    return f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}'


def super_names(mentors, courses):
    mentors_names = []
    for m in mentors:
        course_names = []
        for name in m:
            course_names.append(name.split()[0])
        mentors_names.append(course_names)

    pairs = []
    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            if id2 == id1:
                continue

            intersection_set = set(mentors_names[id1]) & set(mentors_names[id2])
            if len(intersection_set) > 0:
                pair = {courses[id1], courses[id2]}
                if pair not in pairs:
                    pairs.append(pair)
                    all_names_sorted = sorted(intersection_set)
                    return f"На курсах {courses[id1]} и {courses[id2]} преподают: {', '.join(all_names_sorted)}"


def top_name(mentors):
    all_list = []
    for m in mentors:
        all_list.extend(m)

    all_names_list = []
    for mentor in all_list:
        name = ''.join(mentor.split()[0])
        all_names_list.append(name)

    unique_names = set(all_names_list)

    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)])

    popular.sort(key=lambda x: x[1], reverse=True)

    top_3 = popular[0:3]
    top_3_list = []
    for i in top_3:
        top_3_list.append(f'{i[0]}: {i[1]} раз(а), ')
    return "".join(top_3_list).strip(', ')
