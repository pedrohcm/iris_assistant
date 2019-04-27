import wolframalpha as w
import datetime as dt
import getpass as gp
import wikipedia as wp

def getUserName():
    name = gp.getuser().capitalize()
    return name

def getSaudationMessage():
    message = ""
    current_hour = dt.datetime.now().hour
    message = "Good morning, " if current_hour < 12 else ("Good afternoon, " if current_hour < 18 else "Good evening")
    message += getUserName()
    return message

def getWAResults(query):
    app_id = "HGVY68-EG353WJ3EE"
    client = w.Client(app_id)
    result = client.query(input)
    return next(result.results).text

def getWPResults(query):
    wp.set_lang("pt")
    return wp.summary(query, sentences=2)

def getQueryResults(query):
    results = getUserName() + ", here is what i found: \n\n"
    try:
        results += getWAResults(query) + "\n" + "Source: Wolfram Alpha"
    except:
        results += getWPResults(query) + "\n" + "Source: Wikipedia"
    finally:
        return results + "\n"

want = "yes"
print getSaudationMessage() + "\n"
while(want == "yes"):
    input = raw_input("Question: ")
    print("")
    print(getQueryResults(input))
    print("")
    print("I hope that was what you were looking for :) \n")
    want = raw_input("Wanna ask some other things? (yes/no): ")
