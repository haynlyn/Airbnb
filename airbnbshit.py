import re, pyperclip


def money_to_float(price_with_dollar_sign_and_commas):
  try:
    numbers = re.compile(r'([\d.]+)')
    return float(''.join(numbers.findall(str(price_with_dollar_sign_and_commas)))) 
  except:
    return np.nan

def count_words(string):
  return len(string.split(' '))


# This function might have to be permanently added to the main program since you can't read in a column as a set.
# This function had been applied. Shortly after having done so, it had been discovered that you cannot hash a set, so you cannot group on it.
    # Perhaps transform each set into a list and then sort and convert to string. This way, you can hash it and therefore aggregate on it.
def str_to_set(string_of_set):
  string_of_set = string_of_set.strip('{').strip('}')
  set_of_string_of_set = set(string_of_set.split(','))
  return set_of_string_of_set


def time_ago_to_days(string):
  try:
    one_word = {'never': np.nan,
                'today': 0.0,
                'yesterday': 1.0}
    return one_word[string]
  except:
    phrase = re.compile(r'([\d\D]+) (\w+) ago')
    pre_days = phrase.findall(string)[0]
    time_length = {'day': 1.0,
                   'week': 7.0, 
                   'month': 30.0}
    try:
      return float(pre_days[0]) * time_length[pre_days[1].strip('s')]
    except:
      return 1 * time_length[pre_days[1].strip('s')]

def str_to_percent(string):
  try:
    return float(string[:-1])/100
  except:
    return np.nan




