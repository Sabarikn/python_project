def flatten_dict(a,key=None, result=None):
    """Flattens a nested dict."""
    if result is None:
        result = {}

    for x in a.keys():
        if isinstance(a[x], dict):
            flatten_dict(a[x],x, result)
        elif key==None:
            result[x]=a[x]
        else:
            result[key+'.'+x]=a[x]

    return result


