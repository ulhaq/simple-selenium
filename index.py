def to_kb(data):
    rs = {}
    for key, value in data.items():
        if value[1] == 'GB':
            rs[key] = float(value[0])*1000000

        if value[1] == 'MB':
            rs[key] = float(value[0])*1000

        if value[1] == 'KB':
            rs[key] = float(value[0])

    return rs
