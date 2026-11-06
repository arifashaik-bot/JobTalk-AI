import streamlit as st
import re

# Page configuration
st.set_page_config(
    page_title="JobTalk AI",
    page_icon="💼",
    layout="centered"
)

# Application title and description
st.title("💼 JobTalk AI")
st.subheader("Interview Language Adapter")
st.write(
    "Turn your everyday sentences into clear, professional "
    "and interview-ready English."
)

st.divider()

# Get user input
user_text = st.text_area(
    "Enter your sentence or interview answer",
    placeholder="Example: i happy with what i have",
    height=130
)

# Select language style
style = st.selectbox(
    "Choose your preferred style",
    [
        "Interview Style",
        "Professional Style",
        "Simple English"
    ]
)


# Correct common grammar mistakes
def improve_grammar(text):
    text = text.strip()
    text = re.sub(r"\s+", " ", text)

    replacements = [
        (r"\bi happy\b", "I am happy"),
        (r"\bi sad\b", "I am sad"),
        (r"\bi interested on\b", "I am interested in"),
        (r"\bi good in\b", "I am good at"),
        (r"\bi knowed\b", "I knew"),
        (r"\bi done\b", "I have completed"),
        (
            r"\bi made some projects\b",
            "I have worked on several projects"
        ),
        (
            r"\bi know python\b",
            "I have knowledge of Python"
        ),
        (r"\bi am having\b", "I have"),
        (r"\bi have a knowledge\b", "I have knowledge"),
        (r"\bi want to learn\b", "I would like to learn"),
        (r"\bi don't know\b", "I am not familiar with"),
        (r"\bi cant\b", "I cannot"),
        (r"\bi can’t\b", "I cannot"),
        (r"\bi wanna\b", "I want to"),
        (r"\bi gotta\b", "I have to"),
    ]

    for pattern, replacement in replacements:
        text = re.sub(
            pattern,
            replacement,
            text,
            flags=re.IGNORECASE
        )

    # Capitalize the first letter
    if text:
        text = text[0].upper() + text[1:]

    # Add punctuation if missing
    if text and text[-1] not in ".!?":
        text += "."

    return text


# Adapt the answer to the selected style
def adapt_answer(text, style):
    corrected = improve_grammar(text)

    if style == "Simple English":
        return corrected

    if style == "Professional Style":
        replacements = [
            (
                r"\bI am happy with what I have\b",
                "I am satisfied with what I have."
            ),
            (
                r"\bI have knowledge of Python\b",
                "I possess knowledge of Python."
            ),
            (
                r"\bI have worked on several projects\b",
                "I have practical experience working on several projects."
            ),
            (
                r"\bI want to learn\b",
                "I am eager to learn"
            ),
            (
                r"\bI like\b",
                "I am interested in"
            ),
            (
                r"\bI am good at\b",
                "I have strong skills in"
            ),
        ]

        for pattern, replacement in replacements:
            corrected = re.sub(
                pattern,
                replacement,
                corrected,
                flags=re.IGNORECASE
            )

        return corrected

    if style == "Interview Style":
        replacements = [
            (
                r"\bI am happy with what I have\b",
                "I am grateful for my current experiences and remain motivated to grow."
            ),
            (
                r"\bI have knowledge of Python\b",
                "I have a foundation in Python and am interested in applying my skills to practical projects."
            ),
            (
                r"\bI have worked on several projects\b",
                "I have gained practical experience through project work and have continued developing my technical skills."
            ),
            (
                r"\bI want to learn\b",
                "I am eager to learn and develop my skills further"
            ),
            (
                r"\bI like\b",
                "I am particularly interested in"
            ),
            (
                r"\bI am good at\b",
                "One of my strengths is"
            ),
        ]

        for pattern, replacement in replacements:
            corrected = re.sub(
                pattern,
                replacement,
                corrected,
                flags=re.IGNORECASE
            )

        return corrected

    return corrected


# Improve and display the answer
if st.button("✨ Improve My Answer", use_container_width=True):

    if not user_text.strip():
        st.warning("Please enter a sentence first.")

    else:
        result = adapt_answer(user_text, style)

        st.success("Your adapted answer is ready!")

        st.markdown("### Original Answer")
        st.info(user_text.strip())

        st.markdown(f"### {style} — Improved Answer")
        st.write(result)

        # Provide a copy-friendly output box
        st.text_area(
            "Copy your improved answer",
            value=result,
            height=120
        )

# Provide example sentences
with st.expander("💡 Try These Example Sentences"):
    st.write("Example 1: i happy with what i have")
    st.write("Example 2: i know python and i made some projects")
    st.write("Example 3: i want to learn new technologies")
    st.write("Example 4: i good in communication")
    st.write("Example 5: i like solving problems")

# Footer
st.divider()
st.caption(
    "JobTalk AI | A rule-based prototype for interview language adaptation"
)