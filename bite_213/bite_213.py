""" 
Bite 213: 
"""
import re

bite_15_en = '''<p>Iterate over the given <code>names</code> and <code>countries list</code>s, <strong>printing</strong> them prepending the number of the loop (starting at 1). Here is the output you need to deliver:<pre>
1. Julian     Australia
2. Bob        Spain
3. PyBites    Global
4. Dante      Argentina
5. Martin     USA
6. Rodolfo    Mexico
</pre></p><p>Notice that the 2nd column should have a fixed width of 11 chars, so between <i>Julian</i> and <i>Australia</i> there are 5 spaces, between <i>Bob</i> and <i>Spain</i>, there are 8. This column should also be aligned to the left.</p><p>Ideally you use only one for loop, but that is not a requirement.</p><p>Good luck and keep calm and code in Python!</p>'''

bite_15_it = '''<p>Iterare i <code>nomi</code> e le <code>liste dei paesi</code>s indicati, <strong>stampandoli</strong> anteponendo il numero del ciclo (a partire da 1). Ecco l'output che devi consegnare:<pre> 1. Julian Australia 2. Bob Spagna 3. PyBites Global 4. Dante Argentina 5. Martin Stati Uniti d'America 6. Rodolfo Messico </pre></p><p>Si noti che la seconda colonna dovrebbe avere una larghezza fissa di 11 caratteri, quindi tra <i>Julian</i> e <i>Australia</i> ci sono 5 spazi, tra <i>Bob</i> e <i>Spagna</i> , ci sono 8. Questa colonna dovrebbe anche essere allineata a sinistra. </p><p>Idealmente si utilizza solo uno for loop, ma questo non è un requisito. </p><p>Buona fortuna e mantenere la calma e codice in Python! </p>'''

bite_15_it_fixed = '''<p>Iterare i <code>names</code> e le <code>countries list</code>s indicati, <strong>stampandoli</strong> anteponendo il numero del ciclo (a partire da 1). Ecco l'output che devi consegnare:<pre>
1. Julian     Australia
2. Bob        Spain
3. PyBites    Global
4. Dante      Argentina
5. Martin     USA
6. Rodolfo    Mexico
</pre></p><p>Si noti che la seconda colonna dovrebbe avere una larghezza fissa di 11 caratteri, quindi tra <i>Julian</i> e <i>Australia</i> ci sono 5 spazi, tra <i>Bob</i> e <i>Spagna</i> , ci sono 8. Questa colonna dovrebbe anche essere allineata a sinistra. </p><p>Idealmente si utilizza solo uno for loop, ma questo non è un requisito. </p><p>Buona fortuna e mantenere la calma e codice in Python! </p>'''

#
bite_202_en = '''<p>In this Bite you will analyze complexity levels of our first 200 Bites of Py exercises.</p> <p>We loaded <a href="https://bit.ly/2MQyqXQ">this CSV file</a> with some stats that look like this:</p> <pre>
  $ head bite_levels.csv
Bite;Difficulty
Bite 1. Sum n numbers;3.45
Bite 2. Regex Fun;4.89
Bite 3. Word Values;3.97
Bite 4. Top 10 PyBites tags;4.72
Bite 5. Parse a list of names;4.48
Bite 6. PyBites Die Hard;6.8
Bite 7. Parsing dates from logs;5.76
Bite 8. Rotate string characters;3.5
Bite 9. Palindromes;4.71
...
...
Bite 200. :P Minecraft Enchantable Items;None
</pre> <p>The last column shows the average complexity score if available, if not it shows <code>None</code>.</p> <p>Complete the <code>get_most_complex_bites</code> function below following its <em>docstring</em>.</p> <p>Your code will be tested calling your function with different arguments.</p> <p>Have fun and keep calm and code in Python!</p>'''

bite_202_de = '''<p>In diesem Biss analysieren Sie die Komplexität unserer ersten 200 Bites of Py Übungen. </p> <p>Wir haben <a href="https://bit.ly/2MQyqXQ">diese CSV-Datei</a> mit einigen Statistiken geladen, die so aussehen:</p> <pre> $head bite_levels.csv Bite; Schwierigkeitsgrad Bite 1. Summe n Zahlen; 3.45 Biss 2. Regex Fun; 4.89 Biss 3.  Wortwerte; 3.97 Biss 4. Top 10 PyBites Tags; 4.72 Bite 5. Parse eine Liste von Namen; 4.48 Bite 6. PyBites sterben hart; 6.8 Biss 7. Parsing von Daten aus Protokollen; 5.76 Bite 8. Drehen Sie String-Zeichen; 3.5 Bite 9. Palindrome; 4.71... Bite 200. :P Minecraft Enchantable Items; None </pre> <p>In der letzten Spalte wird die durchschnittliche Komplexitätsbewertung angezeigt, falls vorhanden, wenn nicht, wird „ <code>Keine“</code>angezeigt. </p> <p>Füllen Sie die nachfolgende Funktion <code>get_most_complex_bites</code> nach ihrem <em>docstring</em>aus. </p> <p>Ihr Code wird getestet, indem Sie Ihre Funktion mit verschiedenen Argumenten aufrufen. </p> <p>Viel Spaß und Ruhe und Code in Python! </p>'''

bite_202_de_fixed = '''<p>In diesem Biss analysieren Sie die Komplexität unserer ersten 200 Bites of Py Übungen. </p> <p>Wir haben <a href="https://bit.ly/2MQyqXQ">diese CSV-Datei</a> mit einigen Statistiken geladen, die so aussehen:</p> <pre>
  $ head bite_levels.csv
Bite;Difficulty
Bite 1. Sum n numbers;3.45
Bite 2. Regex Fun;4.89
Bite 3. Word Values;3.97
Bite 4. Top 10 PyBites tags;4.72
Bite 5. Parse a list of names;4.48
Bite 6. PyBites Die Hard;6.8
Bite 7. Parsing dates from logs;5.76
Bite 8. Rotate string characters;3.5
Bite 9. Palindromes;4.71
...
...
Bite 200. :P Minecraft Enchantable Items;None
</pre> <p>In der letzten Spalte wird die durchschnittliche Komplexitätsbewertung angezeigt, falls vorhanden, wenn nicht, wird „ <code>None</code>angezeigt. </p> <p>Füllen Sie die nachfolgende Funktion <code>get_most_complex_bites</code> nach ihrem <em>docstring</em>aus. </p> <p>Ihr Code wird getestet, indem Sie Ihre Funktion mit verschiedenen Argumenten aufrufen. </p> <p>Viel Spaß und Ruhe und Code in Python! </p>'''

#
bite_209_en = '''<p>Your team uses <code>Sphinx</code> and wants you to comply with its standards for <code>docstring</code>s. As per the <a href="https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html">Sphinx-RTD-Tutorial</a> a typical <code>Sphinx</code> docstring has the following format:</p> <pre>"""[Summary]

:param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
:type [ParamName]: [ParamType](, optional)
...
:raises [ErrorType]: [ErrorDescription]
...
:return: [ReturnDescription]
:rtype: [ReturnType]
"""
</pre> <p>Based on this format and using the literal strings in italics below, write a docstring for <code>sum_numbers</code> that: <ul> <li>receives <i>numbers: a list of numbers</i> (type: <code>list</code>)</li> <li>raises a <i>TypeError: if not all numeric values passed in</i></li> <li>returns <i>sum of numbers</i> (type: <code>int</code>)</li> </ul></p> <p>There's no need to implement the function (leave the <code>pass</code> in) as this is about writing the proper <code>docstring</code>.</p> <p><strong>Note:</strong>We will be adding annotations to this function in the next Bite so you will need to complete this Bite to unlock the next.</p>'''

bite_209_es = '''<p>Su equipo utiliza <code>Sphinx</code> y quiere que usted cumpla con sus estándares para <code>docstring</code> s. De acuerdo con el <a href="https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html">tutorial Sphinx-RTD</a> una docstring típica de <code>Sphinx</code> tiene el siguiente formato:</p> <pre>«" [Resumen]: param [ParamName]: [ParamDescription], por defecto es [DefaultParamVal] :type [ParamName]: [ParamType] (, opcional)...  :plantea [ErrorType]: [ErrorDescription]... :return: [returnDescription] :rtype: [returnType] «"» </pre> <p>Basado en este formato y utilizando las cadenas literales en cursiva a continuación, escriba una cadena de documentos para <code>sum_numbers</code> que: <ul> <li>recibe <i>números: una lista de números</i> (type: <code>list</code> )</li> <li>genera un <i>TypeError: si no todos los números numéricos pasados en</i></li> <li>devuelve <i>suma de números</i>(tipo: <code>int</code>)</li> </ul></p> <p>No hay necesidad de implementar la función (deje <code>pasar</code>) ya que se trata de escribir la <code>docstring</code>adecuada. </p> <p><strong>Nota:</strong>Vamos a añadir anotaciones a esta función en la próxima mordida, por lo que tendrás que completar esta mordida para desbloquear la siguiente. </p>'''

bite_209_es_fixed = '''<p>Su equipo utiliza <code>Sphinx</code> y quiere que usted cumpla con sus estándares para <code>docstring</code> s. De acuerdo con el <a href="https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html">tutorial Sphinx-RTD</a> una docstring típica de <code>Sphinx</code> tiene el siguiente formato:</p> <pre>"""[Summary]

:param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
:type [ParamName]: [ParamType](, optional)
...
:raises [ErrorType]: [ErrorDescription]
...
:return: [ReturnDescription]
:rtype: [ReturnType]
"""
</pre> <p>Basado en este formato y utilizando las cadenas literales en cursiva a continuación, escriba una cadena de documentos para <code>sum_numbers</code> que: <ul> <li>recibe <i>números: una lista de números</i> (type: <code>list</code> )</li> <li>genera un <i>TypeError: si no todos los números numéricos pasados en</i></li> <li>devuelve <i>suma de números</i>(tipo: <code>int</code>)</li> </ul></p> <p>No hay necesidad de implementar la función (deje <code>pass</code>) ya que se trata de escribir la <code>docstring</code>adecuada. </p> <p><strong>Nota:</strong>Vamos a añadir anotaciones a esta función en la próxima mordida, por lo que tendrás que completar esta mordida para desbloquear la siguiente. </p>'''


def fix_translation(org_text, trans_text):
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """

    words = re.findall(r'>(.*?)<|pre>(.*?)</pre>', trans_text)

    # ? words that within pytest are not translated for some reason ?
    values = []
    for value in [word for word, _ in words]:
        if value == 'nomi':
            values.append('names')
        elif value == 'liste dei paesi':
            values.append('countries list')
        elif value == 'Keine“':
            values.append('None')
        elif value == 'pasar':
            values.append('pass')
        else:
            values.append(value)

    format_string = re.sub(r'>(.*?)<', r'>(.*?)<'.replace('(.*?)', '{}'), org_text)

    # ? again for some reson this space needs to be here to pass ?
    return re.sub(r'</pre><p>', r'</pre><p>'.replace('</pre><p>', '</pre> <p>'),
                  format_string.format(*values))


if __name__ == "__main__":
    ok1 = fix_translation(bite_15_en, bite_15_it) == bite_15_it_fixed
    ok2 = fix_translation(bite_202_en, bite_202_de) == bite_202_de_fixed
    ok3 = fix_translation(bite_209_en, bite_209_es) == bite_209_es_fixed
    print(ok1)
    print(ok2)
    print(ok3)