t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def final_sort(chars="?!:;,. "):
    def sorting(func):
        def wrapper(*args):
            res = func(*args)
            for el in chars:
                if el in res:
                    res = res.replace(el, '-')
            global t
            for key in t.keys():
                res = res.replace(key, t[key])
            return res

        return wrapper
    return sorting


def convert(st):
    st = st.lower()
    new = st.replace('-', ' ').split()
    n = '-'.join(new)
    return n


s = input()

convert = final_sort(chars="?!:;,. ")(convert)

print(convert(s))
