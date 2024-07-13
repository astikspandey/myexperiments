from transformers import pipeline
import language_tool_python

def correct_paragraph(paragraph):
    # Load the grammar correction model
    grammar_model = pipeline('text2text-generation', model='facebook/bart-large-cnn')
    
    # Load LanguageTool
    tool = language_tool_python.LanguageTool('en-US')

    # Use the grammar model to correct the paragraph
    correction = grammar_model(paragraph)[0]['generated_text']

    # Use LanguageTool for additional grammar checks
    matches = tool.check(correction)
    corrected_paragraph = language_tool_python.utils.correct(correction, matches)

    return corrected_paragraph

# Example usage
paragraph = "MY FAVROITE WRITER NAMEE IS sudha murthy. I LOVE HE SO BAD. SHE RIGTHS BOOKS AS LORD OF THE RINGS, CAPTAIN UNDERPANTS AND CAT KID COMIC. HE HUSBHAND NAEM SI ADHUS YHTRUM"

corrected = correct_paragraph(paragraph)
print("Corrected Paragraph:")
print(corrected)

