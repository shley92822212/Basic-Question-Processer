from random import randint


questions = ["Is Intelligent Systems a unit class we are considering?",
          "What are the contents covered by Databases?",
          "Give me a general reference of Intelligent Systems.",
          "Which unit that Winston belongs to?",
          "Does ginsberg include advanced techniques?",
          "Which unit that hull is good postgraduate study?"]

units = {"IS": "intelligent systems", "CS": "computer security", "DB": "databases"}

unit_caracteristics = {"intelligent systems": ["AI principles", "AI applications;"],
                    "computer security.": ["Security principles;", "security programming."],
                    "databases": ["Database principles;", "database applications."]}

unit_references = {"intelligent systems": ["winston", "ginsberg"],
                "computer security": ["mcnab", "kabay"],
                "databases": ["date", "krenke"]}
 
ref_types = ["general", "basic", "postgraduate", "advanced", "theoretical", "theoretical", "foundations"]

reference_types={"winston":{"general": "intelligent systems", "basic": "intelligent systems"},
               "ginsberg": {"postgraduate": "intelligent systems", "advanced": "intelligent systems"},
               "mcnab": {"general": "computer security", "advanced": "computer security"},
               "kabay": {"flexible": "yes", "postgraduate": "computer security", "advanced": "computer security"},
               "date": {"general": "databases", "basic": "databases"},
               "hull": {"theoretical": "databases", "advanced": ["databases", "intelligent systems"], "postgraduate": ["databases", "intelligent systems"], "theoretical foundations": "databases"}}


def is_unit(unit_name = None):
        if unit_name:
                print(">Yes.")
        else:  
                print(">No.")


def what(unit_name, context):
        if context == "content":
                for content in unit_caracteristics[unit_name]:
                        print(">", unit_name, " = ", content)
        elif context == "reference":
                for ref in unit_references[unit_name]:
                        print(">ref for ", unit_name, " = ", ref)

def give(unit_name, context):
        flag = False
        for key in reference_types:
                for key2 in reference_types[key]:
                        if key2 == context and reference_types[key][context] == unit_name:
                                print(">ref = ", key)
                                flag = True
        if not flag:
                print(">Error, could not find ", context, " reference for ", unit_name)


def which(ref_name, context):
        flag = False
        if context == "belong":
                for key in unit_references:
                        for ref in unit_references[key]:
                                if ref_name == ref:
                                        print(">unit = ", key)
                                        flag = True
        else:
                if type(reference_types[ref_name][context]) is str:

                        print(">unit = ", reference_types[ref_name][context])
                        flag = True
                else:
                        for string in reference_types[ref_name][context]:
                                print(">unit = ", string)
                                flag = True
        if not flag:
                print(">Error, connot find instance of ", ref_name, " with type (", context, ")")


def does(ref_name, context):
        if context in reference_types[ref_name]:
                if reference_types[ref_name][context]:
                        print(">Yes.")
        else:
                print(">No.")

# is - currently is quesitons only relate to if a unit is running or not
# what - currently what questions only relate to the content of a unit or what references a unit has
# which -
# does -
# give - 
def main():
        print("Welcome to reference advisor. (quit to exit) Please ask me a question like: ", questions[randint(0, len(questions) - 1)])
        user_input = "temp"
        first_word = None
        while "quit" not in user_input:
                user_input = input(">").lower()
                #check if there is a unit name in the question
                unit = None
                for key in units.keys():
                        if units[key] in user_input:
                                unit = units[key]
                                break
                # get the first word from the question, this helps decide what type of question it is
                first_word, rhs = user_input.split(" ", 1)

                # implement "is" questions
                if first_word == "is":
                        is_unit(unit)
                        continue

                # implement "what" questions
                if first_word == "what" and unit:
                        context = None
                        if "content" in user_input:
                                context = "content"
                        elif "reference" in user_input:
                                context = "reference"
                        what(unit, context)
                        continue

                # implement "give" questions
                if first_word == "give" and unit:
                        flag = False
                        for ref_type in ref_types:
                                if ref_type in user_input:
                                        context = ref_type
                                        flag = True
                        if context:
                                give(unit, context)
                                continue

                # get reference name
                ref_name = None
                for key in reference_types:
                        if key in user_input:
                                ref_name = key

                # implement "which" questions
                if first_word == "which" and ref_name:
                        context = None
                        if "belong" in user_input:
                                context = "belong"
                        else:
                                for ref_type in ref_types:
                                        if ref_type in user_input:
                                                context = ref_type
                        if context:
                                which(ref_name, context)
                                continue

                #implement "does" quesitons
                if first_word == "does" and ref_name:
                        context = None
                        for ref_type in ref_types:
                                if ref_type in user_input:
                                        context = ref_type
                        if context:
                                does(ref_name, context)
                                continue

                print("Sorry, I didnt understand that. You can ask questions like: ", questions[randint(0, len(questions))])



if __name__ == '__main__':
        print("running main")
        main()
print("Done!")
input("waiting for key press")