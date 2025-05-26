"""
BONUS:

4) Tarea de vocabulario: el participante es presentado con una 
palabra y debe elegir su definición de un grupo de opciones.


"""



# 4) Tarea de vocabulario (funciones necesarias)

import wordfreq
import wikipediaapi


def get_frequent_word(language='es', index=0):
    # Función que obtiene palabras de uso frecuente
    base_n = 200
    words = wordfreq.top_n_list(language, base_n+index)
    return words[base_n+index-1]

def get_wikipedia_definition(word, language='es'):
    # Función que obtiene definiciones
    wiki_wiki = wikipediaapi.Wikipedia(
        language=language,
        user_agent='MyApp/1.0 (https://example.com/myapp)'  # Replace with your actual user-agent
    )
    page = wiki_wiki.page(word)
    if page.exists():
        return page.summary
    else:
        return 'not-found'

def remove_word_from_definitions(definition, word):
  definition = definition.replace(word, 'XX')
  definition = definition.replace(word.upper(), 'XX')
  definition = definition.replace(word.upper(), 'XX')
  definition = definition.replace(word.title(), 'XX')
  return definition

def get_words_and_definitions(start=0, top_n=10):
  print('Obteniendo palabras y su significado...')

  frequent_words = []
  definitions = []

  counter = 0

  while len(frequent_words) < top_n:

    # Get frequent word
    word = get_frequent_word('es', start+counter)

    # Obtain definition from Wikipedia
    definition = get_wikipedia_definition(word, 'es')

    if definition != 'not-found':
      frequent_words.append(word)
      definitions.append(definition)

    counter += 1

  # Remove word from definitions
  definitions = [remove_word_from_definitions(definitions[i], frequent_words[i]) for i in range(len(definitions))]

  return frequent_words, definitions

"""Siguiente"""

frequent_words, definitions = get_words_and_definitions(start=0, top_n=10)

for i in range(len(frequent_words)):
  print('Palabra: ', frequent_words[i])
  print('Definicion: ', definitions[i])
  print()

"""Siguiente"""

# 4) Tarea de vocabulario
def run_vocabulary_test(n_words=3, start=0, top_n=10):
  pass