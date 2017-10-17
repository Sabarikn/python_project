def flatten_dict(a,ky=None, result=None):
    """Flattens a nested dict."""
    if result is None:
        result = {}
    if isinstance(a,dict):
      for x in a.keys():
        if '.' in x:
          flatten_dict(a[x],x.split('.'),result)
        else:
          result[x]=a[x]
    else:
      if len(ky)==1:
          result[ky[0]]=a
          return result
      elif ky[0] not in result:
          result[ky[0]]={}
          flatten_dict(a,ky[1:],result[ky[0]])
      else:
          flatten_dict(a,ky[1:],result[ky[0]])

    return result

